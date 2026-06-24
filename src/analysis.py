import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\practice_git\data\clean_sales.csv")

# Basic Metrics
total_revenue = df["amount"].sum()
max_order = df["amount"].max()
avg_order = df["amount"].mean()

# Customer-wise Revenue
customer_revenue = df.groupby("customer")["amount"].sum()

# Top Customer
top_customer = customer_revenue.idxmax()
top_customer_revenue = customer_revenue.max()

print("\n===== SALES SUMMARY =====")

print("\nRevenue by Customer:")
print(customer_revenue)

print(f"\nTotal Revenue      : {total_revenue:.2f}")
print(f"Highest Order      : {max_order:.2f}")
print(f"Average Order      : {avg_order:.2f}")

print("\nTop Customer:")
print(f"{top_customer} ({top_customer_revenue:.2f})")

print("\n=========================")