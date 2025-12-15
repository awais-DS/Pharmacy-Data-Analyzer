import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Sales'] = df['Quantity'] * df['Price']
    return df

def total_revenue(df):
    return df['Total_Sales'].sum()

def top_selling_medicines(df, n=5):
    return (
        df.groupby('Medicine')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

def category_wise_sales(df):
    return df.groupby('Category')['Total_Sales'].sum()

def daily_sales(df):
    return df.groupby('Date')['Total_Sales'].sum()

def low_stock_medicines(df, threshold=20):
    stock = df.groupby('Medicine')['Quantity'].sum()
    return stock[stock < threshold]

def plot_daily_sales(daily_sales_data):
    plt.figure()
    plt.plot(daily_sales_data)
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Daily Pharmacy Sales Trend")
    plt.show()

def main():
    file_path = "pharmacy_sales.csv"
    df = load_data(file_path)

    print("Total Pharmacy Revenue:", total_revenue(df))

    print("\nTop Selling Medicines:")
    print(top_selling_medicines(df))

    print("\nCategory-wise Sales:")
    print(category_wise_sales(df))

    print("\nLow Stock Medicines:")
    print(low_stock_medicines(df))

    plot_daily_sales(daily_sales(df))

if __name__ == "__main__":
    main()
