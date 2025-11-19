# 💊 Pharmacy Data Analyzer

A **Python and Streamlit-based interactive tool** for pharmacy data analysis.  
This project helps pharmacies analyze sales, monitor stock levels, track medicine expiries, and predict recommended stock for the next month. The app provides **charts, summaries, and downloadable reports** to make data-driven decisions easier.

---

## **Table of Contents**

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Required Columns in Excel](#required-columns-in-excel)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Limitations](#limitations)  
7. [Future Improvements](#future-improvements)  

---

## **Features**

- Upload any pharmacy Excel file (`.xlsx` or `.xls`)  
- **Sales Summary**: Total sales, total profit, total quantity sold  
- **Charts**:
  - Sales trend over time  
  - Top-selling medicines  
  - Category-wise profit analysis  
- **Alerts**:
  - Low stock items  
  - Medicines expiring in the next 60 days  
- **Stock Prediction**: Recommended stock for next month, considering current sales and seasonal adjustments (basic logic implemented)  
- Download **filtered Excel data** and **analysis report in PDF**  
- Fully interactive dashboard with **filters**:
  - Date range  
  - Medicine name  
  - Category  

---

## **Project Structure**
├─ app.py # Streamlit app interface
├─ main.py # Core analysis and data handling
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
│
├─ analyzer/ # Analysis scripts
│ └─ stock_prediction.py # Recommended stock calculation
│
├─ visualizer/ # Plotting scripts
│ ├─ sales_plot.py
│ ├─ top_medicines.py
│ ├─ category_plot.py
│ └─ common.py
│
├─ data/ # Sample Excel files (optional)
└─ outputs/ # Generated charts and outputs (optional)


---

## **Required Columns in Excel**

To perform all analyses, the following columns should be present in the uploaded Excel file:

| Column Name       | Description                             |
|------------------|-----------------------------------------|
| Date             | Date of sale                             |
| Medicine Name    | Name of the medicine                     |
| Category         | Medicine category (e.g., Painkiller)    |
| Quantity Sold    | Quantity sold in units                   |
| Sale Price       | Total sale price                         |
| Cost Price       | Purchase cost                             |
| Stock Left       | Remaining stock in inventory             |
| Expiry Date      | Expiry date of the medicine              |

> ⚠️ If any columns are missing, the corresponding analysis will be skipped.

---

## **Installation**

1. Clone the repository:

bash
git clone https://github.com/<your-username>/Pharmacy-Data-Analyzer.git
cd Pharmacy-Data-Analyzer
#Usage
streamlit run app.py
Upload your pharmacy Excel file (.xlsx or .xls)

Apply filters on the sidebar:

Date range

Medicine name

Category

View charts, alerts, and summaries

Download filtered Excel data or PDF report
Limitations

Seasonal trends and next-month stock predictions are basic logic only; for higher accuracy, an ML model is recommended.

Analysis depends on required columns; missing columns will skip certain sections.

Only .xlsx or .xls files are supported.

Large Excel files may slow down performance.
Future Improvements

Implement ML-based sales forecasting for seasonal trends

Add interactive web app deployment for multiple pharmacies

Include location-based sales and stock analysis

Add automated email notifications for low stock or expiring medicines

Add more advanced charts and KPIs for pharmacy management
