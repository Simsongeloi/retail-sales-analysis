import csv

# Read sales data from the CSV file
sales = {}

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        region = row["Region"]
        amount = int(row["Monthly_Sales"])
        sales[region] = amount

# Calculate sales statistics
total_sales = sum(sales.values())
average_sales = total_sales / len(sales)

# Identify highest and lowest performing regins
highest_region = max(sales, key=sales.get)
lowest_region = min(sales, key=sales.get)

# Identifying region with Above or Below Average.
above_average_regions = [region for region, amount in sales.items() if amount > average_sales]
below_average_regions = [region for region, amount in sales.items() if amount < average_sales]


# Display the report
print("NORTHSTAR RETAIL SALES REPORT")
print("-----------------------------")

for region, amount in sales.items():
    print(f"{region}: ${amount:,.2f}")

print("-----------------------------")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Sales: ${average_sales:,.2f}")
print(f"Highest Performing Region: {highest_region} (${sales[highest_region]:,.2f})")
print(f"Lowest Performing Region: {lowest_region} (${sales[lowest_region]:,.2f})")
print(f"Regions Above Average: {', '.join(above_average_regions)}")
print(f"Regions Below Average: {', '.join(below_average_regions)}")
