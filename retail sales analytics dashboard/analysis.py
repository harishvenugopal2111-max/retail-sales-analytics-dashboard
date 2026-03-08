import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\VENKATESH\OneDrive\Desktop\retail sales analytics dashboard\sales_data.csv")

print("Dataset:")
print(data)

# Total sales
total_sales = data["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by product
sales_product = data.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(sales_product)

# Sales by region
sales_region = data.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(sales_region)

# Product sales chart
sales_product.plot(kind="bar", title="Sales by Product")
plt.ylabel("Sales")
plt.show()

# Region sales chart
sales_region.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.show()