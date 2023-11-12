---

# Data Processing Toolkit

## Overview
This repository contains two powerful Python scripts designed for efficient data processing:
1. **PDF File Splitter**: Splits a large PDF file into smaller segments based on a specified maximum file size.
2. **CSV File Combiner**: Combines multiple CSV files into a single Excel workbook, with each CSV file as a separate sheet.

These tools are ideal for handling large data files, making data management tasks more manageable and streamlined.

## Installation
To run these scripts, you will need Python installed on your system, along with some additional libraries. You can install the required libraries using the following commands:

```bash
pip install pikepdf
pip install pandas xlsxwriter
```

## Scripts

### PDF File Splitter
- **Purpose**: Splits a PDF into smaller files.
- **Usage**: Provide the path to your PDF and the maximum file size for each segment.
- **Example**:

  ```python
  split_pdf("path_to_pdf.pdf", max_size_mb=25)
  ```

### CSV File Combiner
- **Purpose**: Combines multiple CSV files into a single Excel workbook.
- **Usage**: Specify the folder containing CSV files and the desired output path for the Excel workbook.
- **Example**:

  ```python
  folder_path = 'path_to_csv_folder'
  output_excel_path = 'output_file.xlsx'
  combine_csvs_to_excel(folder_path, output_excel_path)
  ```

## Getting Started
To get started with these scripts:
1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed.
3. Follow the usage examples provided for each script.

## Contributing
Contributions to this repository are welcome. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to make contributions.
