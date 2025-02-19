import pandas as pd
from fpdf import FPDF

# Read data from CSV
csv_file = "data.csv"  # Ensure this file exists in the same directory
df = pd.read_csv(csv_file)

# Perform basic analysis
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

# Generate PDF report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Sales Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Summary
pdf.cell(200, 10, f"Total Sales: {total_sales}", ln=True)
pdf.cell(200, 10, f"Total Profit: {total_profit}", ln=True)
pdf.cell(200, 10, f"Average Sales: {average_sales:.2f}", ln=True)
pdf.cell(200, 10, f"Average Profit: {average_profit:.2f}", ln=True)
pdf.ln(10)

# Add Table Header
pdf.set_font("Arial", "B", 12)
pdf.cell(60, 10, "Date", border=1, align="C")
pdf.cell(60, 10, "Sales", border=1, align="C")
pdf.cell(60, 10, "Profit", border=1, align="C")
pdf.ln()

# Add Table Data
pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(60, 10, str(row["Date"]), border=1, align="C")
    pdf.cell(60, 10, str(row["Sales"]), border=1, align="C")
    pdf.cell(60, 10, str(row["Profit"]), border=1, align="C")
    pdf.ln()

# Save PDF
pdf.output("sales_report.pdf")
print("PDF Report Generated: sales_report.pdf")
