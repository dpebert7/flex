import csv
import random
from datetime import datetime, timedelta

# Number of rows in the fact table
num_rows = 10000000

# Dimension table data
colors = ['Crimson', 'Azure', 'Emerald', 'Goldenrod', 'Amethyst']
locations = ['Johannesburg', 'Cape Town', 'Durban', 'Pretoria', 'Port Elizabeth', 'Bloemfontein',
             'East London', 'Nelspruit', 'Pietermaritzburg']

# Generate fact table data
fact_data = []
start_date = datetime(2013, 1, 1)
end_date = datetime(2022, 12, 31)

date_range = (end_date - start_date).days + 1
dates = [start_date + timedelta(days=i) for i in range(date_range)]
random.shuffle(dates)

for i in range(num_rows):
    date = dates[i % date_range].date()
    color_key = i % len(colors) + 1  # ColorKey based on list index
    color = colors[color_key-1 % len(colors)]
    location_key = i % len(locations) + 1
    location = locations[location_key-1 % len(locations)]
    
    if color == 'Azure':
        value = round(random.normalvariate(150, 10), 2)
    elif color == 'Emerald':
        value = round(random.normalvariate(400, 10), 2)
    else:
        value = round(random.normalvariate(200, 10), 2)

    if location == 'Pietermaritzburg':
        value = value*2
    elif location == 'Cape Town':
        value = value + 25
    elif location == 'Durban':
        value = value/2
    elif location == 'Nelspruit':
        value = value - 50

    # Add some random noise
    value += random.uniform(-50, 50)

    fact_data.append((date, color_key, location_key, round(value, 2)))

# Write fact table data to CSV file
with open('fact_table.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'ColorKey', 'LocationKey', 'Value'])  # Write header
    writer.writerows(fact_data)

print("Fact table generation completed.")

# Generate dimension table data
dimension_data = []

# DimDate table
for i, date in enumerate(dates):
    dimension_data.append((i + 1, date))

with open('dim_date.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['DateKey', 'Date'])  # Write header
    writer.writerows(dimension_data)

# DimColor table
dimension_data = []
for i, color in enumerate(colors):
    dimension_data.append((i + 1, color))

with open('dim_color.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ColorKey', 'Color'])  # Write header
    writer.writerows(dimension_data)

# DimLocation table
dimension_data = []
for i, location in enumerate(locations):
    dimension_data.append((i + 1, location))

with open('dim_location.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['LocationKey', 'Location'])  # Write header
    writer.writerows(dimension_data)

print("Dimension table generation completed.")
