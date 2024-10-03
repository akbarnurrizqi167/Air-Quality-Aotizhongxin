import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium

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

# Menambahkan Peta dengan Folium
st.subheader("Peta Distribusi Konsentrasi PM2.5")
map_center = [39.9042, 116.4074]  # Koordinat Beijing, China
m = folium.Map(location=map_center, zoom_start=11)

# Menambahkan kolom latitude dan longitude untuk lokasi yang diketahui
df['latitude'] = 39.9042
df['longitude'] = 116.4074

# Menambahkan titik-titik berdasarkan PM2.5
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(m)

st_folium(m, width=600, height=300)

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
