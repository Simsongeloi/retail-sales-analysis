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

# Display the report
print("NORTHSTAR RETAIL SALES REPORT")
print("-----------------------------")

for region, amount in sales.items():
    print(f"{region}: ${amount:,.2f}")

print("-----------------------------")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Sales: ${average_sales:,.2f}")