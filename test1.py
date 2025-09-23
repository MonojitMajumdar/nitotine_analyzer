import pandas as pd

# Read the Excel file
data = pd.read_excel("layer_CV.xlsx", skiprows=2)

# Define the setups
setups = ["bare", "Mxene", "Mxene + AuNPs", "Mxene + AuNPs + nic"]

# Create an empty DataFrame to store the transformed data
transformed_data = pd.DataFrame(columns=["setup", "voltage", "current"])

# Process each setup
for i, setup in enumerate(setups):
    # Extract voltage and current columns for the current setup
    voltage_col = data.columns[i * 2]  # Voltage column (e.g., 0, 2, 4, 6)
    current_col = data.columns[i * 2 + 1]  # Current column (e.g., 1, 3, 5, 7)
    
    # Create a DataFrame for this setup
    setup_df = pd.DataFrame({
        "setup": [setup] * len(data),
        "voltage": data[voltage_col],
        "current": data[current_col]
    })
    
    # Append to the main DataFrame
    transformed_data = pd.concat([transformed_data, setup_df], ignore_index=True)

# Drop any rows with NaN values
transformed_data = transformed_data.dropna()

# Save to CSV without trailing commas
transformed_data.to_csv("C:/Python313/transformed_layer_cv.csv", 
                        index=False, 
                        header=True, 
                        lineterminator='\n')
print("CSV file created successfully at C:/Python313/transformed_layer_cv.csv")