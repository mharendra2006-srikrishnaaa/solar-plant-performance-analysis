import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

irradiance = []
for d in dates:
    month = d.month
    base = [3.2, 3.8, 4.5, 5.2, 5.8, 6.1, 5.9, 5.7, 5.0, 4.3, 3.5, 3.0]
    val = base[month - 1] + np.random.normal(0, 0.4)
    irradiance.append(max(0, val))

temperature = []
for d in dates:
    month = d.month
    base = [24, 26, 29, 33, 36, 38, 37, 36, 34, 31, 27, 24]
    val = base[month - 1] + np.random.normal(0, 1.5)
    temperature.append(round(val, 1))

irradiance = np.array(irradiance)
temperature = np.array(temperature)

# Power output drops slightly at high temperature (realistic)
power_output = (irradiance * 18.5) * (1 - 0.004 * (temperature - 25))
power_output = power_output + np.random.normal(0, 2, len(dates))
power_output = np.clip(power_output, 0, None).round(2)

# Inject 15 fault/underperformance days
fault_indices = np.random.choice(len(dates), 15, replace=False)
power_output[fault_indices] *= np.random.uniform(0.3, 0.6, 15)

df = pd.DataFrame({
    "date": dates,
    "irradiance_kwh_m2": np.round(irradiance, 3),
    "temperature_c": temperature,
    "power_output_kw": power_output,
})

df["month"] = df["date"].dt.month_name()
df["day_of_week"] = df["date"].dt.day_name()

df.to_csv("solar_plant_data.csv", index=False)
print("Dataset created successfully!")
print(df.head())