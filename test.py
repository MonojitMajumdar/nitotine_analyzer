import streamlit as st
import pandas as pd

st.set_page_config(page_title="Nicotine Analyzer", layout="wide")

st.title("Nicotine Analyzer - Layer CV Processor")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file (xlsx)", type=["xlsx"])

if uploaded_file:
    # Read Excel file, skip first 2 rows like your original code
    data = pd.read_excel(uploaded_file, skiprows=2)

    # Define setups
    setups = ["bare", "Mxene", "Mxene + AuNPs", "Mxene + AuNPs + nic"]

    # Create transformed dataframe
    transformed_data = pd.DataFrame(columns=["setup", "voltage", "current"])

    for i, setup in enumerate(setups):
        # Extract columns safely
        voltage_col = data.columns[i * 2]
        current_col = data.columns[i * 2 + 1]

        setup_df = pd.DataFrame({
            "setup": [setup] * len(data),
            "voltage": data[voltage_col],
            "current": data[current_col]
        })

        transformed_data = pd.concat([transformed_data, setup_df], ignore_index=True)

    # Drop missing values
    transformed_data = transformed_data.dropna()

    # Show dataframe inside app
    st.subheader("Transformed Data")
    st.dataframe(transformed_data)

    # Prepare CSV for download
    csv = transformed_data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="transformed_layer_cv.csv",
        mime="text/csv"
    )
else:
    st.info(" Please upload an Excel file to process.")
