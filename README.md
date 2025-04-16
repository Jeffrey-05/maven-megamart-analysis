# Maven-Megamart-Analysis
Retail Data Analysis using Pandas and NumPy on Maven Mega Mart
# Maven Mega Mart Data Analysis

## Project Overview

This project involves analyzing retail transaction data from **Maven Mega Mart** to derive insights into customer behavior, sales trends, and product-level performance. The analysis is carried out using **Python** libraries **Pandas** and **NumPy**.

### Key Objectives:
- Explore and analyze transaction data from Maven Mega Mart.
- Calculate total and percentage discounts applied on products.
- Aggregate and analyze sales performance by product, household, and demographics.
- Merge transaction data with product and household demographic information.

## Tools Used
- **Python** (Pandas, NumPy)
- **Google Colab ** (optional for exploratory analysis and visualization)
- **CSV** (for dataset storage and management)

## Dataset Information

The datasets used for this project are:
1. **project_transactions.csv**: Contains transaction details including sales value, quantity, discounts, and product-related information.
2. **hh_demographic.csv**: Includes household demographic details like age, income, and household composition.
3. **product.csv**: Contains product-level details such as product ID and department.

### Key Columns:
- **RETAIL_DISC**: Retail discount applied to products.
- **COUPON_DISC**: Coupon discount applied to products.
- **SALES_VALUE**: Total sales value of the transaction.
- **QUANTITY**: Quantity of items sold in a transaction.
- **HOUSEHOLD_KEY**: Unique identifier for each household.
- **PRODUCT_ID**: Unique identifier for each product.
- **DEPARTMENT**: The department the product belongs to.


Project Outputs
The analysis produces valuable insights into:

Sales Insights:

Total sales value

Total discount applied

Overall discount percentage

Total quantity sold

Total sales value per basket

Total sales value per household

Demographic Insights:

Aggregated sales data by household, segmented by demographic data (age, income, family composition).

Product Insights:

Department-wise sales data.

Product-level performance.

Analysis Breakdown
Requirement 1: Column Creations
Created two new columns:

TOTAL_DISCOUNT: Sum of retail and coupon discounts.

PERCENTAGE_DISCOUNT: Ratio of total discounts to sales value.

Dropped the individual discount columns (RETAIL_DISC, COUPON_DISC, COUPON_MATCH_DISC).

Requirement 2: Overall Statistics
Calculated:

Total sales value (SALES_VALUE)

Total discount applied (TOTAL_DISCOUNT)

Overall discount percentage

Total quantity sold

Total sales value per basket and household.

Requirement 3: Demographic Insights
Aggregated the sales data by household_key and merged it with the demographic data.

Performed inner joins with product and demographic tables to segment sales performance by household characteristics.

Requirement 4: Product Demographics
Joined product-level data with transaction and demographic data to analyze product performance within different demographic segments.

Project Goals
This analysis is designed to provide insights into:

Sales Performance: Identifying products and households contributing to overall sales.

Discount Impact: Understanding how retail and coupon discounts affect sales performance.

Demographic Trends: Analyzing purchasing behavior across various demographic groups.
