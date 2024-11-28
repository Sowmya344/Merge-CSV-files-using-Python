import streamlit as st
import pandas as pd
from datetime import datetime

# Create a Streamlit app title
st.title("Merge CSV Files by Common Columns and Date")

# Create a file uploader to upload multiple CSV files
uploaded_files = st.file_uploader("Upload CSV files", type="csv", accept_multiple_files=True)

# Check if files are uploaded
if uploaded_files:
    # Initialize an empty list to store the dataframes
    dataframes = []
    date_column_name = None

    # Loop through each file and read it into a dataframe
    for file in uploaded_files:
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")

    # Check if we have dataframes loaded
    if dataframes:
        # Find the common columns among all dataframes
        common_columns = set(dataframes[0].columns)
        for df in dataframes[1:]:
            common_columns &= set(df.columns)

        # Check if common columns are found
        if common_columns:
            # Convert the common columns set to a sorted list
            common_columns = sorted(list(common_columns))

            # Identify the date column (assuming the date column is common)
            for column in common_columns:
                if 'date' in column.lower():  # Identify a column with 'date' in its name
                    date_column_name = column
                    break

            if date_column_name:
                # Ensure all dataframes are sorted by the date column
                for df in dataframes:
                    if date_column_name in df.columns:
                        df[date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce')  # Ensure proper datetime conversion
                        df.sort_values(by=date_column_name, inplace=True)

                # Merge the dataframes by common columns
                merged_df = pd.concat([df[common_columns] for df in dataframes], ignore_index=True)

                # Sort the merged dataframe by the date column to ensure final ordering from oldest to newest
                merged_df.sort_values(by=date_column_name, inplace=True)

                # Display a preview of the merged data
                st.subheader("Preview of Merged Data (Sorted by Date)")
                st.dataframe(merged_df.head())  # Show the first few rows of the merged dataframe

                # Create a new CSV file with the merged data
                @st.cache_data
                def convert_df(df):
                    return df.to_csv(index=False)

                csv = convert_df(merged_df)

                # Create a download button to download the new CSV file
                st.download_button(
                    label="Download merged CSV file",
                    data=csv,
                    file_name="merged_data.csv",
                    mime="text/csv",
                )
            else:
                st.error("No common date column found between the CSV files.")
        else:
            st.error("No common columns found between the CSV files.")
    else:
        st.error("No valid data loaded from the CSV files.")
