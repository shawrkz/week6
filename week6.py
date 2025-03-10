from collections import defaultdict

# Sales data
data = [
    {'region': 'North America', 'product': 'widgets', 'sales': 150},
    {'region': 'North America', 'product': 'bobbles', 'sales': 200},
    {'region': 'Europe', 'product': 'widgets', 'sales': 120},
    {'region': 'Europe', 'product': 'bobbles', 'sales': 180},
    {'region': 'Asia', 'product': 'widgets', 'sales': 300},
    {'region': 'Asia', 'product': 'bobbles', 'sales': 250},
    {'region': 'North America', 'product': 'widgets', 'sales': 175},
    {'region': 'North America', 'product': 'bobbles', 'sales': 220},
    {'region': 'Europe', 'product': 'widgets', 'sales': 130},
    {'region': 'Europe', 'product': 'bobbles', 'sales': 190},
    {'region': 'Asia', 'product': 'widgets', 'sales': 310},
    {'region': 'Asia', 'product': 'bobbles', 'sales': 260},
    {'region': 'North America', 'product': 'widgets', 'sales': 160},
    {'region': 'North America', 'product': 'bobbles', 'sales': 210},
    {'region': 'Europe', 'product': 'widgets', 'sales': 140},
    {'region': 'Europe', 'product': 'bobbles', 'sales': 200},
    {'region': 'Asia', 'product': 'widgets', 'sales': 320},
    {'region': 'Asia', 'product': 'bobbles', 'sales': 270},
    {'region': 'North America', 'product': 'widgets', 'sales': 155},
    {'region': 'North America', 'product': 'bobbles', 'sales': 215},
    {'region': 'Europe', 'product': 'widgets', 'sales': 135},
    {'region': 'Europe', 'product': 'bobbles', 'sales': 205},
    {'region': 'Asia', 'product': 'widgets', 'sales': 330},
    {'region': 'Asia', 'product': 'bobbles', 'sales': 280},
    {'region': 'North America', 'product': 'widgets', 'sales': 165},
    {'region': 'North America', 'product': 'bobbles', 'sales': 225},
    {'region': 'Europe', 'product': 'widgets', 'sales': 145},
    {'region': 'Europe', 'product': 'bobbles', 'sales': 210},
    {'region': 'Asia', 'product': 'widgets', 'sales': 340},
    {'region': 'Asia', 'product': 'bobbles', 'sales': 290},
    {'region': 'North America', 'product': 'widgets', 'sales': 170},
]

# Calculate total sales
total_sales = sum(item['sales'] for item in data)
print("Total sales:", total_sales)

# Calculate sales by region
region_sales = defaultdict(int)
for item in data:
    region_sales[item['region']] += item['sales']

# Get top three regions by overall products sold
top_three_regions = sorted(region_sales.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top three regions by overall products sold:", top_three_regions)

# Calculate sales by product
product_sales = defaultdict(int)
for item in data:
    product_sales[item['product']] += item['sales']

# Determine which product sold more
if product_sales['bobbles'] > product_sales['widgets']:
    print("Bobbles sold more.")
else:
    print("Widgets sold more.")

# Calculate revenue for each product
bobbles_price = 10.99
widgets_price = 15.99

bobbles_revenue = product_sales['bobbles'] * bobbles_price
widgets_revenue = product_sales['widgets'] * widgets_price

print("Bobbles revenue:", bobbles_revenue)
print("Widgets revenue:", widgets_revenue)

# Determine which product made the most revenue
if bobbles_revenue > widgets_revenue:
    print("Bobbles made the most revenue.")
else:
    print("Widgets made the most revenue.")

# Find the region and product with the least sales
min_sales = min(data, key=lambda x: x['sales'])
print("Region and product that sold the least:", min_sales)