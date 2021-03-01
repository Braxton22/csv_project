# changing the fiel to include all the data for the year of 2018
# change the title to - Daily high and low temperatures - 2018
# extract
from datetime import datetime
import csv

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# The enumerate() function returns both the index of each item and the value of each item as you loop through a list
for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


lows = []
highs = []
dates = []
for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print("Missing data for ", converted_date)
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(converted_date)


import matplotlib.pyplot as plt

fig = plt.figure()

# plot highs on a chart with dates
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Daily high temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)

fig.autofmt_xdate()

plt.show()
