# MAVEN MEGA MART DATA ANALYTICS PROJECT
# --------------------------------------
# Tools: Python, Pandas, NumPy

import numpy as np
import pandas as pd

# --------------------------------------
# STEP 1: Load Data
# --------------------------------------
transactions = pd.read_csv("project_transactions.csv")
demographics = pd.read_csv("hh_demographic.csv")
products = pd.read_csv("product.csv")

# --------------------------------------
# STEP 2: Product-Level Analysis
# --------------------------------------

# Requirement 1: Create Discount Columns
transactions['TOTAL_DISCOUNT'] = transactions['RETAIL_DISC'] + transactions['COUPON_DISC']
transactions['PERCENTAGE_DISCOUNT'] = transactions['TOTAL_DISCOUNT'] / transactions['SALES_VALUE']

# Drop individual discount columns
transactions.drop(columns=['RETAIL_DISC', 'COUPON_DISC', 'COUPON_MATCH_DISC'], inplace=True)

# Requirement 2: Calculate Overall Statistics
total_sales = transactions['SALES_VALUE'].sum()
total_discount = transactions['TOTAL_DISCOUNT'].sum()
overall_percentage_discount = total_discount / total_sales
total_quantity = transactions['QUANTITY'].sum()
sales_per_basket = total_sales // transactions['BASKET_ID'].nunique()
sales_per_household = total_sales // transactions['household_key'].nunique()

# Print KPIs
print("----- PRODUCT ANALYSIS KPIs -----\n")
print("Total Sales Value:", total_sales)
print("Total Discount Given:", total_discount)
print("Overall Percentage Discount:", overall_percentage_discount)
print("Total Quantity Sold:", total_quantity)
print("Average Sales per Basket:", sales_per_basket)
print("Average Sales per Household:", sales_per_household)
print("\n---------------------------------\n")

# --------------------------------------
# STEP 3: Acquisition Target Analysis
# --------------------------------------

# Keep only necessary columns
transaction_subset = transactions[['household_key', 'BASKET_ID', 'PRODUCT_ID', 'QUANTITY', 'SALES_VALUE']]

# Convert to efficient datatypes
transaction_subset[['QUANTITY', 'PRODUCT_ID']] = transaction_subset[['QUANTITY', 'PRODUCT_ID']].astype(np.int32)

# Keep only required demographic columns
demographics = demographics[['household_key', 'AGE_DESC', 'INCOME_DESC', 'HH_COMP_DESC']]

# Group transaction data by household and calculate total sales
household_sales = transaction_subset.groupby('household_key')['SALES_VALUE'].sum().reset_index()

# Join household sales with demographic information
demographic_sales = household_sales.merge(demographics, on='household_key', how='inner')

# Display top 5 rows of joined demographic-sales data
print("----- DEMOGRAPHIC SALES DATA -----")
print(demographic_sales.head())
print("----------------------------------\n")

# --------------------------------------
# STEP 4: Product Demographic Analysis
# --------------------------------------

# Filter only required columns from product data
product_info = products[['PRODUCT_ID', 'DEPARTMENT']]

# Merge product with transaction and demographic data
product_merged = transaction_subset.merge(product_info, on='PRODUCT_ID', how='inner')
product_demo_merged = product_merged.merge(demographics, on='household_key', how='inner')

# Display top 5 rows of final merged data
print("----- PRODUCT DEMOGRAPHIC DATA -----")
print(product_demo_merged.head())
print("------------------------------------")
