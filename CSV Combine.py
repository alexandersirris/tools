!pip install xlsxwriter
import pandas as pd
import os

def combine_csvs_to_excel(folder_path, output_excel_path):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(output_excel_path, engine='xlsxwriter')

    # Iterate through each CSV file in the specified folder
    for csv_file in os.listdir(folder_path):
        if csv_file.endswith('.csv'):
            file_path = os.path.join(folder_path, csv_file)
            # Read CSV file into a pandas dataframe
            df = pd.read_csv(file_path)

            # Write dataframe to an Excel sheet named after the CSV file
            df.to_excel(writer, sheet_name=os.path.splitext(csv_file)[0], index=False)

    # Save the Excel file
    writer.save()

# Example usage
folder_path = '/content/drive/MyDrive/Trading/Stock Picks/Back Test Data/8) Enhanced Day Trading Strategy 7.0'  # Replace with the path to your folder containing CSV files
output_excel_path = '/content/drive/MyDrive/Trading/Stock Picks/Back Test Data/8) Enhanced Day Trading Strategy 7.0/combined_excel.xlsx'  # Replace with your desired output Excel file path

combine_csvs_to_excel(folder_path, output_excel_path)
