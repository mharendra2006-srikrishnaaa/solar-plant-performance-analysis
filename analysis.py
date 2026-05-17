import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────
os.makedirs("output_graphs", exist_ok=True)
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 150

df = pd.read_csv("solar_plant_data.csv", parse_dates=["date"])

month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)

# ── Graph 1: Daily Power Output across the year ────────
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(df["date"], df["power_output_kw"], color="#2196F3", linewidth=0.8, alpha=0.8)
ax.fill_between(df["date"], df["power_output_kw"], alpha=0.15, color="#2196F3")
ax.set_title("Daily Power Output — 100 kW Solar Plant (2023)", fontsize=14, fontweight="bold")
ax.set_xlabel("Date")
ax.set_ylabel("Power Output (kW)")
plt.tight_layout()
plt.savefig("output_graphs/01_daily_power_output.png")
plt.close()
print("Graph 1 saved")

# ── Graph 2: Monthly Average Power Output ─────────────
monthly = df.groupby("month", observed=True)["power_output_kw"].mean().reset_index()
fig, ax = plt.subplots(figsize=(12, 5))
bars = ax.bar(monthly["month"], monthly["power_output_kw"],
              color=sns.color_palette("YlOrRd", 12), edgecolor="white")
ax.set_title("Monthly Average Power Output (kW)", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Avg Power Output (kW)")
ax.set_xticklabels(monthly["month"], rotation=45, ha="right")
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}", ha="center", va="bottom", fontsize=8)
plt.tight_layout()
plt.savefig("output_graphs/02_monthly_avg_power.png")
plt.close()
print("Graph 2 saved")

# ── Graph 3: Irradiance vs Power Output (scatter) ─────
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(df["irradiance_kwh_m2"], df["power_output_kw"],
                     c=df["temperature_c"], cmap="RdYlGn_r",
                     alpha=0.6, s=20, edgecolors="none")
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Temperature (°C)")
ax.set_title("Irradiance vs Power Output\n(color = temperature)", fontsize=13, fontweight="bold")
ax.set_xlabel("Solar Irradiance (kWh/m²)")
ax.set_ylabel("Power Output (kW)")
plt.tight_layout()
plt.savefig("output_graphs/03_irradiance_vs_power.png")
plt.close()
print("Graph 3 saved")

# ── Graph 4: Underperformance / Fault Detection ────────
monthly_avg = df.groupby("month", observed=True)["power_output_kw"].transform("mean")
df["expected"] = monthly_avg
df["performance_ratio"] = df["power_output_kw"] / df["expected"]
df["status"] = df["performance_ratio"].apply(
    lambda x: "Underperforming" if x < 0.7 else "Normal"
)
fig, ax = plt.subplots(figsize=(14, 5))
colors = df["status"].map({"Normal": "#4CAF50", "Underperforming": "#F44336"})
ax.scatter(df["date"], df["power_output_kw"], c=colors, s=15, alpha=0.8)
ax.set_title("Fault Detection — Underperforming Days Highlighted", fontsize=14, fontweight="bold")
ax.set_xlabel("Date")
ax.set_ylabel("Power Output (kW)")
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor="#4CAF50", label="Normal"),
                   Patch(facecolor="#F44336", label="Underperforming")]
ax.legend(handles=legend_elements)
plt.tight_layout()
plt.savefig("output_graphs/04_fault_detection.png")
plt.close()
print("Graph 4 saved")

# ── Graph 5: Temperature Effect on Efficiency ─────────
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df["temperature_c"], df["performance_ratio"],
           alpha=0.5, color="#FF7043", s=20, edgecolors="none")
z = np.polyfit(df["temperature_c"], df["performance_ratio"], 1)
p = np.poly1d(z)
x_line = np.linspace(df["temperature_c"].min(), df["temperature_c"].max(), 100)
ax.plot(x_line, p(x_line), color="black", linewidth=1.5, linestyle="--", label="Trend line")
ax.set_title("Temperature vs Performance Ratio", fontsize=13, fontweight="bold")
ax.set_xlabel("Ambient Temperature (°C)")
ax.set_ylabel("Performance Ratio")
ax.legend()
plt.tight_layout()
plt.savefig("output_graphs/05_temperature_vs_performance.png")
plt.close()
print("Graph 5 saved")

# ── Summary Statistics ─────────────────────────────────
print("\n========== PROJECT SUMMARY ==========")
print(f"Total days analysed     : {len(df)}")
print(f"Total energy generated  : {df['power_output_kw'].sum():.1f} kWh")
print(f"Average daily output    : {df['power_output_kw'].mean():.2f} kW")
print(f"Peak output day         : {df.loc[df['power_output_kw'].idxmax(), 'date'].date()} "
      f"({df['power_output_kw'].max():.2f} kW)")
print(f"Underperforming days    : {(df['status'] == 'Underperforming').sum()}")
print(f"Best month              : {df.groupby('month', observed=True)['power_output_kw'].mean().idxmax()}")
print(f"Worst month             : {df.groupby('month', observed=True)['power_output_kw'].mean().idxmin()}")
print("======================================")
print("\nAll 5 graphs saved to output_graphs/ folder")