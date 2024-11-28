# README: Merge CSV Files by Common Columns and Date

## Overview

This Streamlit application allows users to upload multiple CSV files, automatically identifies common columns (including a date column), merges the files based on those columns, and sorts the resulting dataset by date. The application then provides an option to download the merged CSV file. It is useful for combining data from multiple sources that share common attributes, such as sales reports, logs, or time-series data. I created this project for my big data project where I had to merge multiple files and had proble,s hence i wrote this code so itll be an easier job to merge files. 

### Key Features:
- **Upload Multiple CSV Files:** Upload as many CSV files as needed.
- **Automatic Identification of Common Columns:** The app detects columns that are common across all uploaded CSV files.
- **Date Handling:** The application identifies a common date column (if present) and ensures the merged data is sorted chronologically.
- **Merge and Sort Data:** Data from multiple CSV files is merged based on common columns and sorted by the date column.
- **Download Merged Data:** Once the data is merged, you can download the result as a new CSV file.

## Requirements

Before running the project, ensure that the following Python libraries are installed:
- `streamlit` – for creating the web interface.
- `pandas` – for data manipulation and handling CSV files.
- `datetime` – for handling date columns.

You can install the required libraries by running:

```bash
pip install streamlit pandas
```

## Usage

### 1. **Run the Streamlit App:**

To launch the Streamlit app, open a terminal and run the following command:

```bash
streamlit run app.py
```

Replace `app.py` with the filename of the Python script if you saved it with a different name.

### 2. **Upload CSV Files:**

- Click on the file uploader and select one or more CSV files from your computer.
- The app will automatically read the uploaded files and check for common columns among them.

### 3. **Merge and Sort Data:**

- If the uploaded CSV files contain common columns (including a date column), the app will merge the data based on those columns.
- It will then sort the data by the identified date column in ascending order, from the oldest to the newest.

### 4. **Preview and Download Merged Data:**

- The merged dataset will be displayed as a preview in the app.
- If you are satisfied with the merged data, you can download it by clicking the "Download merged CSV file" button.

### 5. **Error Handling:**
- If no common columns are found between the files, or if no date column is identified, the app will display an error message.

## Code Breakdown

### File Upload and Reading:
The app uses `streamlit`'s `file_uploader` widget to allow users to upload multiple CSV files. Each file is read into a pandas DataFrame using `pd.read_csv()`.

### Common Columns Identification:
The app compares the columns of all uploaded files to identify common columns. If a common date column is present, it is used to sort the data.

### Sorting and Merging:
Once the common columns are identified, the app merges the DataFrames using `pd.concat()` and sorts them by the date column using `sort_values()`.

### Data Conversion and Download:
The app provides an option to download the merged data as a new CSV file. This is achieved by converting the pandas DataFrame to CSV format using `to_csv()` and providing a download link with `st.download_button()`.

## Example Output

### Merged Data Preview:

| Date       | Column 1   | Column 2   | Column 3   |
|------------|------------|------------|------------|
| 2024-01-01 | Value A1   | Value B1   | Value C1   |
| 2024-01-02 | Value A2   | Value B2   | Value C2   |
| 2024-01-03 | Value A3   | Value B3   | Value C3   |

### Download Button:
Once the data is merged, a "Download merged CSV file" button will appear, allowing you to save the merged CSV file to your local machine.

## Contributing

Contributions to this project are welcome! If you find any bugs, issues, or have suggestions for enhancements, please feel free to submit an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This app is intended for personal or educational use. Ensure that any data uploaded and processed complies with your organization’s privacy and data handling policies.
