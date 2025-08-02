import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium
import numpy as np
from aotizhongxin_geojson import aotizhongxin_geojson, monitoring_points

# Judul Aplikasi
st.title("Air Quality Analysis Dashboard")

# Deskripsi Singkat
st.write(
    """
    ## Analisis Kualitas Udara
    Dashboard ini menampilkan hasil analisis kualitas udara berdasarkan dataset Air Quality.
    Dataset ini berisi informasi konsentrasi polutan seperti PM2.5, PM10, SO2, NO2, CO, O3, serta faktor lingkungan lain seperti suhu, kelembaban, dan kecepatan angin.
    """
)

# Sesuaikan path dataset di sini
dataset_path = 'data/PRSA_Data_Aotizhongxin_20130301-20170228.csv'  # Sesuaikan path sesuai lokasi file CSV Anda

# Memuat dataset yang sudah dianalisis sebelumnya
try:
    df = pd.read_csv(dataset_path)
except FileNotFoundError:
    st.error(f"File CSV tidak ditemukan di lokasi: {dataset_path}. Pastikan path sudah benar dan file CSV tersedia.")
    st.stop()

# Menampilkan data awal
st.subheader("Data Awal")
st.dataframe(df.head())

# Menampilkan statistik deskriptif
st.subheader("Statistik Deskriptif")
st.write(df.describe())

# Mengonversi kolom 'year', 'month', dan 'day' menjadi kolom datetime jika ada
if 'year' in df.columns and 'month' in df.columns and 'day' in df.columns:
    # Buat kolom 'date' dari 'year', 'month', 'day'
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    # Buat kolom 'year' yang sesuai
    df['year'] = df['date'].dt.year
elif 'date' in df.columns:
    # Jika ada kolom 'date', gunakan langsung untuk mendapatkan 'year'
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
else:
    st.write("Dataset tidak memiliki kolom 'year', 'month', 'day', atau 'date'. Pastikan dataset memiliki salah satu kolom ini.")

# Visualisasi 1: Distribusi Konsentrasi PM2.5
st.subheader("Distribusi Konsentrasi PM2.5")
plt.figure(figsize=(10, 6))
sns.histplot(df['PM2.5'].dropna(), bins=30, kde=True, color='skyblue')
plt.title("Distribusi Konsentrasi PM2.5")
plt.xlabel("PM2.5 Concentration")
plt.ylabel("Frequency")
st.pyplot(plt)

# Visualisasi 2: Tren Tahunan PM2.5
if 'year' in df.columns:
    st.subheader("Tren Tahunan PM2.5")
    yearly_avg_pm25 = df.groupby('year')['PM2.5'].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_avg_pm25.index, yearly_avg_pm25.values, marker='o', linestyle='-', color='purple')
    plt.title("Rata-Rata Tahunan Konsentrasi PM2.5")
    plt.xlabel("Tahun")
    plt.ylabel("Rata-Rata PM2.5")
    st.pyplot(plt)
else:
    st.write("Kolom 'year' tidak tersedia, tidak dapat menampilkan tren tahunan.")

# Visualisasi 3: Korelasi antar Polutan
st.subheader("Korelasi Antar Polutan")
plt.figure(figsize=(10, 8))
sns.heatmap(df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Matriks Korelasi Konsentrasi Polutan")
st.pyplot(plt)

# Visualisasi 4: Scatter Plot PM2.5 vs Suhu
st.subheader("Hubungan PM2.5 dengan Suhu")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['TEMP'], y=df['PM2.5'], hue=df['PM2.5'], palette='viridis')
plt.title("Scatter Plot: PM2.5 vs Suhu")
plt.xlabel("Suhu (°C)")
plt.ylabel("PM2.5 Concentration")
st.pyplot(plt)

# Menambahkan Peta dengan Folium dan GeoJSON
st.subheader("Peta Distribusi Konsentrasi PM2.5 - Area Aotizhongxin")

# Membuat peta dengan center di Aotizhongxin
map_center = [39.9042, 116.4074]  # Koordinat Aotizhongxin, Beijing
m = folium.Map(location=map_center, zoom_start=13)

# Menghitung statistik PM2.5 untuk distribusi warna
pm25_stats = df['PM2.5'].describe()
pm25_min = pm25_stats['min']
pm25_max = pm25_stats['max']
pm25_mean = pm25_stats['mean']

# Fungsi untuk menentukan warna berdasarkan tingkat PM2.5
def get_color_for_pm25(pm25_value):
    if pd.isna(pm25_value):
        return 'gray'
    elif pm25_value <= 35:  # Baik
        return 'green'
    elif pm25_value <= 75:  # Sedang
        return 'yellow'
    elif pm25_value <= 115:  # Tidak sehat untuk sensitif
        return 'orange'
    elif pm25_value <= 150:  # Tidak sehat
        return 'red'
    else:  # Sangat tidak sehat
        return 'purple'

# Simulasi data untuk setiap area (karena data asli hanya dari satu stasiun)
np.random.seed(42)  # Untuk konsistensi hasil
area_data = []

for point in monitoring_points:
    # Simulasi variasi data berdasarkan lokasi dan waktu
    base_pm25 = df['PM2.5'].mean()
    area_factor = np.random.uniform(0.8, 1.2)  # Faktor variasi area
    area_pm25 = base_pm25 * area_factor
    
    area_data.append({
        'area_id': point['area_id'],
        'station_name': point['name'],
        'lat': point['lat'],
        'lon': point['lon'],
        'avg_pm25': area_pm25,
        'avg_temp': df['TEMP'].mean() + np.random.uniform(-2, 2),
        'avg_humidity': np.random.uniform(40, 80)
    })

area_df = pd.DataFrame(area_data)

# Menambahkan layer GeoJSON dengan warna berdasarkan konsentrasi PM2.5
for i, feature in enumerate(aotizhongxin_geojson['features']):
    area_id = feature['properties']['area_id']
    area_info = area_df[area_df['area_id'] == area_id].iloc[0]
    
    # Warna berdasarkan tingkat PM2.5
    color = get_color_for_pm25(area_info['avg_pm25'])
    
    folium.GeoJson(
        feature,
        style_function=lambda x, color=color: {
            'fillColor': color,
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.6,
        },
        popup=folium.Popup(
            f"""
            <b>{feature['properties']['name']}</b><br>
            Stasiun: {area_info['station_name']}<br>
            Rata-rata PM2.5: {area_info['avg_pm25']:.1f} μg/m³<br>
            Rata-rata Suhu: {area_info['avg_temp']:.1f}°C<br>
            Kelembaban: {area_info['avg_humidity']:.1f}%
            """,
            max_width=300
        ),
        tooltip=f"{feature['properties']['name']}: PM2.5 = {area_info['avg_pm25']:.1f} μg/m³"
    ).add_to(m)

# Menambahkan marker untuk setiap stasiun monitoring
for _, area in area_df.iterrows():
    color = get_color_for_pm25(area['avg_pm25'])
    
    folium.CircleMarker(
        location=[area['lat'], area['lon']],
        radius=8,
        color='black',
        fill=True,
        fillColor=color,
        fillOpacity=0.8,
        popup=folium.Popup(
            f"""
            <b>{area['station_name']}</b><br>
            PM2.5: {area['avg_pm25']:.1f} μg/m³<br>
            Suhu: {area['avg_temp']:.1f}°C<br>
            Kelembaban: {area['avg_humidity']:.1f}%
            """,
            max_width=200
        ),
        tooltip=f"{area['station_name']}"
    ).add_to(m)

# Menambahkan legenda
legend_html = '''
<div style="position: fixed; 
            bottom: 50px; left: 50px; width: 200px; height: 140px; 
            background-color: white; border:2px solid grey; z-index:9999; 
            font-size:14px; padding: 10px">
<p><b>Kualitas Udara PM2.5</b></p>
<p><i class="fa fa-circle" style="color:green"></i> Baik (≤35 μg/m³)</p>
<p><i class="fa fa-circle" style="color:yellow"></i> Sedang (36-75 μg/m³)</p>
<p><i class="fa fa-circle" style="color:orange"></i> Tidak Sehat Sensitif (76-115 μg/m³)</p>
<p><i class="fa fa-circle" style="color:red"></i> Tidak Sehat (116-150 μg/m³)</p>
<p><i class="fa fa-circle" style="color:purple"></i> Sangat Tidak Sehat (>150 μg/m³)</p>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Menampilkan peta
st_folium(m, width=800, height=500)

# Menampilkan tabel statistik area
st.subheader("Statistik PM2.5 per Area")
display_df = area_df[['station_name', 'avg_pm25', 'avg_temp', 'avg_humidity']].copy()
display_df.columns = ['Stasiun', 'Rata-rata PM2.5 (μg/m³)', 'Rata-rata Suhu (°C)', 'Kelembaban (%)']
display_df = display_df.round(1)
st.dataframe(display_df, use_container_width=True)

# Visualisasi tambahan: Chart perbandingan PM2.5 antar area
st.subheader("Perbandingan PM2.5 Antar Area")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Bar chart PM2.5 per area
bars = ax1.bar(area_df['station_name'], area_df['avg_pm25'], 
               color=[get_color_for_pm25(pm25) for pm25 in area_df['avg_pm25']])
ax1.set_title('Rata-rata PM2.5 per Area')
ax1.set_ylabel('PM2.5 (μg/m³)')
ax1.tick_params(axis='x', rotation=45)

# Menambahkan label nilai di atas bar
for bar, value in zip(bars, area_df['avg_pm25']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{value:.1f}', ha='center', va='bottom')

# Scatter plot PM2.5 vs Suhu per area
scatter = ax2.scatter(area_df['avg_temp'], area_df['avg_pm25'], 
                     c=[get_color_for_pm25(pm25) for pm25 in area_df['avg_pm25']], 
                     s=100, alpha=0.7)
ax2.set_title('Hubungan PM2.5 vs Suhu per Area')
ax2.set_xlabel('Suhu (°C)')
ax2.set_ylabel('PM2.5 (μg/m³)')

# Menambahkan label untuk setiap titik
for i, txt in enumerate(area_df['station_name']):
    ax2.annotate(txt, (area_df['avg_temp'].iloc[i], area_df['avg_pm25'].iloc[i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=8)

plt.tight_layout()
st.pyplot(fig)

# Visualisasi distribusi temporal (menggunakan data asli)
st.subheader("Distribusi Temporal PM2.5")

# Distribusi per bulan
if 'month' in df.columns:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Box plot per bulan
    monthly_data = df.groupby('month')['PM2.5'].apply(list).reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    monthly_pm25 = [df[df['month'] == i]['PM2.5'].dropna().values for i in range(1, 13)]
    bp = ax1.boxplot(monthly_pm25, labels=month_names)
    ax1.set_title('Distribusi PM2.5 per Bulan')
    ax1.set_ylabel('PM2.5 (μg/m³)')
    ax1.tick_params(axis='x', rotation=45)
    
    # Heatmap per jam dan bulan
    if 'hour' in df.columns:
        pivot_data = df.groupby(['month', 'hour'])['PM2.5'].mean().unstack()
        sns.heatmap(pivot_data, cmap='YlOrRd', cbar_kws={'label': 'PM2.5 (μg/m³)'}, ax=ax2)
        ax2.set_title('Heatmap PM2.5: Bulan vs Jam')
        ax2.set_xlabel('Jam')
        ax2.set_ylabel('Bulan')
    
    plt.tight_layout()
    st.pyplot(fig)

# Menampilkan kesimpulan
st.write(
    """
    ## Kesimpulan
    Berdasarkan hasil analisis, beberapa poin penting yang dapat disimpulkan adalah:
    1. Konsentrasi PM2.5 bervariasi dari tahun ke tahun dan cenderung mengalami kenaikan pada bulan-bulan tertentu.
    2. Terdapat korelasi yang signifikan antara beberapa polutan, seperti PM2.5 dan PM10.
    3. Suhu memiliki hubungan dengan konsentrasi PM2.5, yang dapat mengindikasikan pengaruh kondisi lingkungan terhadap kualitas udara.
    """
)
