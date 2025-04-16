{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMj7Z3tud/fmko5eEyHM3or"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"62EuJxy7dk5N"},"outputs":[],"source":["# MAVEN MEGA MART DATA ANALYTICS PROJECT\n","# --------------------------------------\n","# Tools: Python, Pandas, NumPy\n","\n","import numpy as np\n","import pandas as pd\n","\n","# --------------------------------------\n","# STEP 1: Load Data\n","# --------------------------------------\n","transactions = pd.read_csv(\"project_transactions.csv\")\n","demographics = pd.read_csv(\"hh_demographic.csv\")\n","products = pd.read_csv(\"product.csv\")\n","\n","# --------------------------------------\n","# STEP 2: Product-Level Analysis\n","# --------------------------------------\n","\n","# Requirement 1: Create Discount Columns\n","transactions['TOTAL_DISCOUNT'] = transactions['RETAIL_DISC'] + transactions['COUPON_DISC']\n","transactions['PERCENTAGE_DISCOUNT'] = transactions['TOTAL_DISCOUNT'] / transactions['SALES_VALUE']\n","\n","# Drop individual discount columns\n","transactions.drop(columns=['RETAIL_DISC', 'COUPON_DISC', 'COUPON_MATCH_DISC'], inplace=True)\n","\n","# Requirement 2: Calculate Overall Statistics\n","total_sales = transactions['SALES_VALUE'].sum()\n","total_discount = transactions['TOTAL_DISCOUNT'].sum()\n","overall_percentage_discount = total_discount / total_sales\n","total_quantity = transactions['QUANTITY'].sum()\n","sales_per_basket = total_sales // transactions['BASKET_ID'].nunique()\n","sales_per_household = total_sales // transactions['household_key'].nunique()\n","\n","# Print KPIs\n","print(\"----- PRODUCT ANALYSIS KPIs -----\\n\")\n","print(\"Total Sales Value:\", total_sales)\n","print(\"Total Discount Given:\", total_discount)\n","print(\"Overall Percentage Discount:\", overall_percentage_discount)\n","print(\"Total Quantity Sold:\", total_quantity)\n","print(\"Average Sales per Basket:\", sales_per_basket)\n","print(\"Average Sales per Household:\", sales_per_household)\n","print(\"\\n---------------------------------\\n\")\n","\n","# --------------------------------------\n","# STEP 3: Acquisition Target Analysis\n","# --------------------------------------\n","\n","# Keep only necessary columns\n","transaction_subset = transactions[['household_key', 'BASKET_ID', 'PRODUCT_ID', 'QUANTITY', 'SALES_VALUE']]\n","\n","# Convert to efficient datatypes\n","transaction_subset[['QUANTITY', 'PRODUCT_ID']] = transaction_subset[['QUANTITY', 'PRODUCT_ID']].astype(np.int32)\n","\n","# Keep only required demographic columns\n","demographics = demographics[['household_key', 'AGE_DESC', 'INCOME_DESC', 'HH_COMP_DESC']]\n","\n","# Group transaction data by household and calculate total sales\n","household_sales = transaction_subset.groupby('household_key')['SALES_VALUE'].sum().reset_index()\n","\n","# Join household sales with demographic information\n","demographic_sales = household_sales.merge(demographics, on='household_key', how='inner')\n","\n","# Display top 5 rows of joined demographic-sales data\n","print(\"----- DEMOGRAPHIC SALES DATA -----\")\n","print(demographic_sales.head())\n","print(\"----------------------------------\\n\")\n","\n","# --------------------------------------\n","# STEP 4: Product Demographic Analysis\n","# --------------------------------------\n","\n","# Filter only required columns from product data\n","product_info = products[['PRODUCT_ID', 'DEPARTMENT']]\n","\n","# Merge product with transaction and demographic data\n","product_merged = transaction_subset.merge(product_info, on='PRODUCT_ID', how='inner')\n","product_demo_merged = product_merged.merge(demographics, on='household_key', how='inner')\n","\n","# Display top 5 rows of final merged data\n","print(\"----- PRODUCT DEMOGRAPHIC DATA -----\")\n","print(product_demo_merged.head())\n","print(\"------------------------------------\")\n"]}]}