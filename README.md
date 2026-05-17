# Solar Power Plant Performance Analysis

## Project Overview
This project performs a complete data-driven performance analysis of a 100 kW solar power plant using one full year of operational data (2023). It simulates the work done by O&M (Operations & Maintenance) engineers in the solar energy industry.

## Tools & Technologies
- Python 3.x
- Pandas — data manipulation and analysis
- NumPy — numerical computations
- Matplotlib — data visualization
- Seaborn — statistical plotting

## Key Objectives
- Analyse daily and monthly solar power generation trends
- Study the relationship between solar irradiance and power output
- Investigate the impact of ambient temperature on plant efficiency
- Detect underperforming and fault days using performance ratio analysis

## Analysis Performed

### 1. Daily Power Output Trend
Plotted the full year of daily generation data to identify seasonal variation and anomalies.

### 2. Monthly Average Power Output
Bar chart showing monthly averages — June is the best performing month, December the worst, consistent with Tamil Nadu's solar irradiance pattern.

### 3. Irradiance vs Power Output
Scatter plot showing strong positive correlation between irradiance and output. Temperature is encoded as color — higher temperatures slightly reduce output.

### 4. Fault Detection
Using Performance Ratio (PR) analysis, 15 underperforming days were identified where output dropped below 70% of the monthly average — flagged for maintenance review.

### 5. Temperature vs Performance Ratio
Trend line confirms negative temperature coefficient — as ambient temperature rises, panel efficiency slightly decreases (consistent with -0.4%/°C standard silicon PV behavior).

## Key Results
| Metric | Value |
|--------|-------|
| Total days analysed | 365 |
| Total energy generated | 30,080.5 kWh |
| Average daily output | 82.41 kW |
| Peak output day | 2023-06-29 (132.36 kW) |
| Underperforming days detected | 15 |
| Best performing month | June |
| Worst performing month | December |

## Project Structure
solar_analysis_project/
│
├── create_data.py          # Generates realistic solar plant dataset
├── analysis.py             # Main analysis and visualization script
├── solar_plant_data.csv    # Generated dataset (365 days)
└── output_graphs/
├── 01_daily_power_output.png
├── 02_monthly_avg_power.png
├── 03_irradiance_vs_power.png
├── 04_fault_detection.png
└── 05_temperature_vs_performance.png

## Real-World Relevance
This analysis mirrors the daily workflow of solar O&M engineers who monitor plant performance, detect faults, and generate performance reports. The PR-based fault detection approach is used in industry-standard SCADA monitoring systems.

## Author
Harendra — B.E. Electrical and Electronics Engineering  
Sri Krishna College of Technology, Coimbatore  
Batch: 2024–2028