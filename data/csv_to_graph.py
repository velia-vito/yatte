import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# 1. Load and Clean
df = pd.read_csv("1024_2_measure_mk.csv", encoding="utf-8", skiprows=1)
df.columns = df.columns.str.strip()

df["words"] = pd.to_numeric(df["words"], errors="coerce")
df["split_time"] = pd.to_numeric(df["split_time"], errors="coerce")

df = df.dropna()

# 2. Smoothing
df["smoothed"] = savgol_filter(df["split_time"], window_length=76, polyorder=3)

# 3. Find Threshold Crossing Points
thresholds_ms = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
crossing_points = {}

for ms in thresholds_ms:
    micros = ms * 1000
    matches = df[df["smoothed"] >= micros]
    if not matches.empty:
        first_match = matches.iloc[0]
        crossing_points[ms] = (first_match["words"], first_match["smoothed"])

# 4. Plot
plt.figure(figsize=(14, 8))

plt.plot(
    df["words"], df["split_time"], color="gray", alpha=0.1, label="Raw Data (Jitter)"
)
plt.plot(
    df["words"], df["smoothed"], color="#1f77b4", linewidth=2, label="Performance Trend"
)

# 5. Add Threshold Markers
cmap = mpl.colormaps["viridis"]
colors = cmap(np.linspace(0, 1, len(thresholds_ms)))

for i, ms in enumerate(thresholds_ms):
    y_val = ms * 1000
    color = colors[i]
    plt.axhline(y=y_val, color="red", linestyle="--", alpha=0.3)

    if ms in crossing_points:
        word_count, _ = crossing_points[ms]
        plt.axvline(x=word_count, color=color, linestyle="-.", alpha=0.6)

        plt.annotate(
            f"{int(word_count)} words",
            xy=(word_count, y_val),
            xytext=(10, 10 if i % 2 == 0 else -25),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->", color=color),
            fontsize=9,
            fontweight="bold",
            color=color,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color, alpha=0.8),
        )

plt.xlabel("Word Count (N)")
plt.ylabel("Latency (μs)")
plt.title("Dart Atom Measurement: Latency Threshold Analysis", fontsize=14)
plt.legend(loc="upper left")
plt.grid(True, which="both", linestyle=":", alpha=0.4)
plt.tight_layout()

print("Calculation complete. Opening plot window...")
plt.show()
