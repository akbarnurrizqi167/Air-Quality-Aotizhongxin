# 🌍 Air Quality Analysis Dashboard - Aotizhongxin Station

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://air-quality-aotizhongxin.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Overview

This project presents a comprehensive Air Quality Analysis Dashboard for the Aotizhongxin monitoring station in Beijing, China. The dashboard provides interactive visualizations and in-depth analysis of air pollution data from 2013 to 2017, featuring advanced mapping capabilities with GeoJSON integration and real-time data exploration tools.

**Live Dashboard**: [air-quality-aotizhongxin.streamlit.app](https://air-quality-aotizhongxin.streamlit.app/)

## 🎯 Key Features

### 📊 Interactive Dashboard
- **Real-time Data Visualization**: Interactive charts and graphs using Streamlit
- **Geographic Mapping**: Advanced map visualization with Folium and GeoJSON integration
- **Multi-area Analysis**: Simulated data distribution across 5 monitoring zones
- **Temporal Analysis**: Time-series analysis with hourly, daily, and seasonal patterns

### 🗺️ Advanced Mapping
- **GeoJSON Integration**: Custom geographic boundaries for Aotizhongxin area
- **Color-coded Visualization**: Air quality index-based color mapping
- **Interactive Markers**: Detailed popup information for each monitoring point
- **Legend and Controls**: User-friendly navigation and data interpretation

### 📈 Comprehensive Analytics
- **Statistical Analysis**: Descriptive statistics and correlation analysis
- **Trend Analysis**: Multi-year trend visualization and pattern recognition
- **Environmental Correlation**: Relationship analysis between pollutants and weather factors
- **Data Distribution**: Histogram and box plot visualizations

## 🏗️ Project Structure

```
Air-Quality-Aotizhongxin/
├── 📊 AirQualityAotizhongxin.ipynb    # Jupyter notebook with detailed analysis
├── 📁 dashboard/                       # Streamlit dashboard application
│   ├── dashboard.py                   # Main dashboard application
│   ├── aotizhongxin_geojson.py       # GeoJSON data and coordinates
│   └── requirements.txt               # Dashboard dependencies
├── 📁 data/                           # Dataset directory
│   └── PRSA_Data_Aotizhongxin_20130301-20170228.csv
├── 📄 README.md                       # Project documentation
├── 📄 requirements.txt                # Main project dependencies
└── 📄 url.txt                         # Deployed application URL
```

## 🔧 Technologies Used

### Backend & Analysis
- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Statistical visualization

### Frontend & Visualization
- **Streamlit**: Web application framework
- **Folium**: Interactive mapping
- **Plotly**: Advanced interactive charts
- **GeoJSON**: Geographic data representation

### Deployment
- **Streamlit Cloud**: Application hosting
- **Git**: Version control

## 📊 Dataset Information

**Source**: Beijing Multi-Site Air-Quality Data  
**Station**: Aotizhongxin  
**Period**: March 1, 2013 - February 28, 2017  
**Records**: 35,064 hourly measurements  

### Data Variables
| Variable | Description | Unit |
|----------|-------------|------|
| PM2.5 | Fine particulate matter | μg/m³ |
| PM10 | Coarse particulate matter | μg/m³ |
| SO2 | Sulfur dioxide | μg/m³ |
| NO2 | Nitrogen dioxide | μg/m³ |
| CO | Carbon monoxide | mg/m³ |
| O3 | Ozone | μg/m³ |
| TEMP | Temperature | °C |
| PRES | Pressure | hPa |
| DEWP | Dew point | °C |
| RAIN | Precipitation | mm |
| WSPM | Wind speed | m/s |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akbarnurrizqi167/Air-Quality-Aotizhongxin.git
   cd Air-Quality-Aotizhongxin
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter Notebook Analysis**
   ```bash
   jupyter notebook AirQualityAotizhongxin.ipynb
   ```

4. **Launch Dashboard Application**
   ```bash
   cd dashboard
   streamlit run dashboard.py
   ```

The dashboard will open in your browser at `http://localhost:8501`

## 📱 Dashboard Usage

### Navigation
1. **Data Overview**: View raw data and descriptive statistics
2. **Visualizations**: Explore various charts and graphs
3. **Geographic Analysis**: Interactive map with air quality distribution
4. **Temporal Analysis**: Time-series patterns and trends
5. **Correlation Analysis**: Relationship between variables

### Interactive Features
- **Filter Data**: Select specific time periods and pollutants
- **Zoom & Pan**: Navigate the interactive map
- **Hover Information**: Get detailed data on hover
- **Download**: Export visualizations and filtered data

## 🔍 Key Insights

### Air Quality Patterns
- **Seasonal Variation**: Higher PM2.5 concentrations during winter months
- **Daily Cycles**: Peak pollution levels during rush hours
- **Weather Correlation**: Strong inverse relationship with wind speed

### Geographic Distribution
- **Hot Spots**: Identification of high-pollution zones
- **Spatial Patterns**: Pollution concentration mapping
- **Monitoring Coverage**: Multi-point analysis across the region

## 🛠️ Development

### Local Development Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Run tests (if available)
pytest tests/

# Start development server
streamlit run dashboard/dashboard.py --server.runOnSave true
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

- [ ] Real-time data integration
- [ ] Machine learning predictions
- [ ] Mobile-responsive design
- [ ] Additional monitoring stations
- [ ] API development
- [ ] Automated reporting

## 📝 Research Questions

This project addresses two key research questions:

1. **How is the distribution of PM2.5 pollutant concentrations in the Aotizhongxin area from 2013 to 2017?**
2. **What environmental factors most influence PM2.5 pollutant levels?**

## 👨‍💻 Author

**Akbar Nur Rizqi**  
- Email: akbarnurrizqi167@gmail.com
- Dicoding ID: akbarrizqi167
- GitHub: [@akbarnurrizqi167](https://github.com/akbarnurrizqi167)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Beijing Municipal Environmental Monitoring Center for the dataset
- Streamlit team for the amazing framework
- Folium contributors for mapping capabilities
- Open source community for various tools and libraries

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/akbarnurrizqi167/Air-Quality-Aotizhongxin/issues) page
2. Create a new issue with detailed information
3. Contact the author via email

---

**⭐ Star this repository if you find it helpful!**
