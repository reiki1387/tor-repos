import pandas as pd

# Load data (replace with your file path)
water_quality = pd.read_csv("water_quality.docx")
fish_population = pd.read_csv("fish_population.docx")

# Clean and analyze
water_quality_summary = water_quality.groupby("Site ID").agg({
    "Temperature (°C)": ["mean", "max"],
    "pH": ["mean", "min"],
    "Dissolved Oxygen (mg/L)": ["mean", "min"]
})

fish_summary = fish_population.groupby("Species").agg({
    "Count": "sum",
    "Average Size (cm)": "mean"
})

# Save to new files
water_quality_summary.to_csv("water_quality_summary.csv")
fish_summary.to_csv("fish_summary.csv")