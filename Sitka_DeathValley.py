# Import Modules
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Read Death Valley File, set to read mode
Death_Valley_File = open("death_valley_2018_simple.csv", "r")
Death_Valley_csv_file = csv.reader(Death_Valley_File, delimiter=",")

# Print out header labels and their indices for easier reference
header_row = next(Death_Valley_csv_file)
for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

# Create Dates List
dates = []

# Create High/Low Lists
DeathValleyLows = []
DeathValleyHighs = []

# Iterate through csv file and append temperatures and dates to their respective list
# If the iteration runs into a valueerror, print out that there is missing data
for row in Death_Valley_csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        DeathValleyHighs.append(int(row[4]))
        DeathValleyLows.append(int(row[5]))
        dates.append(converted_date)

# Close death valley file
Death_Valley_File.close()

# Open Sitka File, set to read mode
Sitka_File = open("sitka_weather_2018_simple.csv", "r")
Sitka_csv_file = csv.reader(Sitka_File, delimiter=",")
header_row2 = next(Sitka_csv_file)

for index, column_header in enumerate(header_row2):
    print("Index:", index, "Column Name:", column_header)

# Create High/Low Lists
SitkaLows = []
SitkaHighs = []

# Iterate through and append to lists
for row in Sitka_csv_file:
    SitkaHighs.append(int(row[5]))
    SitkaLows.append(int(row[6]))

# Close file
Sitka_File.close()

# Create two subplots
fig, a = plt.subplots(1)
a.plot(dates, SitkaHighs, c="red")
a.plot(dates, SitkaLows, c="blue")
a[1].plot(dates, DeathValleyHighs, c="red")
a[1].plot(dates, DeathValleyLows, c="blue")

plt.show()