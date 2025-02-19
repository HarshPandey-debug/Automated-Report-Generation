# Automated Report Generation

## Overview
This Python script reads data from a CSV file, analyzes it using Pandas, and generates a formatted PDF report using the **FPDF** library. The report includes key insights such as total sales, total profit, and a tabular representation of the data.

## Features
- Reads data from a CSV file.
- Cleans and processes the data.
- Calculates key metrics (Total Sales, Total Profit, Averages).
- Generates a well-formatted PDF report.

## Prerequisites
Make sure you have the following installed:

```sh
pip install pandas fpdf
```

## CSV File Format
Ensure your CSV file (`data.csv`) follows this format:

```
Date,Sales,Profit
2024-02-01,1500,200
2024-02-02,1800,250
2024-02-03,2100,300
```

## Usage
1. Place the `data.csv` file in the same directory as the script.
2. Run the script:

```sh
python automated_report.py
```

3. The generated PDF report (`sales_report.pdf`) will be saved in the same directory.

## Troubleshooting
### KeyError: 'Sales'
- Run this command to check column names:

```python
print(df.columns)
```
- Ensure column names match exactly (`Sales`, `Profit`).
- Strip spaces if necessary:

```python
df.columns = df.columns.str.strip()
```

## Customization
- Modify the CSV file path if needed:

```python
csv_file = "path/to/your/file.csv"
```
- Adjust the number formatting in the PDF:

```python
pdf.cell(200, 10, f"Average Sales: {average_sales:.2f}", ln=True)
```

## License
This project is open-source. Feel free to modify and distribute it.

---


