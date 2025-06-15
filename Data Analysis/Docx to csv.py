from docx import Document
import pandas as pd

# Load the Word document
doc = Document(r"C:\Users\FRED\Desktop\MSE800 Exercises\Data Analysis\Data_Analytics_Assessment_1_Data_Set.docx")

# Initialize empty lists for data
water_quality_data = []
fish_population_data = []

# Flags to identify tables
current_table = None

for table in doc.tables:
    # Check the first row to determine table type
    first_row_text = [cell.text.strip() for cell in table.rows[0].cells]
    
    if "Water Quality Data" in " ".join(first_row_text):
        current_table = "water_quality"
        headers = [cell.text.strip() for cell in table.rows[1].cells]  # Assumes headers are in row 1
        for row in table.rows[2:]:  # Skip header rows
            row_data = [cell.text.strip() for cell in row.cells]
            if any(row_data):  # Skip empty rows
                water_quality_data.append(row_data)
    
    elif "Fish Population Data" in " ".join(first_row_text):
        current_table = "fish_population"
        headers = [cell.text.strip() for cell in table.rows[1].cells]
        for row in table.rows[2:]:
            row_data = [cell.text.strip() for cell in row.cells]
            if any(row_data):
                fish_population_data.append(row_data)

# Convert to DataFrames
df_water = pd.DataFrame(water_quality_data, columns=headers)
df_fish = pd.DataFrame(fish_population_data, columns=headers)

# Save to CSV
df_water.to_csv("water_quality.csv", index=False)
df_fish.to_csv("fish_population.csv", index=False)

print("CSV files saved successfully!")