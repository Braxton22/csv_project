# changing the fiel to include all the data for the year of 2018
# change the title to - Daily high and low temperatures - 2018
# extract
from datetime import datetime
import csv
import matplotlib.pyplot as plt

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# The enumerate() function returns both the index of each item and the value of each item as you loop through a list
for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


lows = []
highs = []
dates = []
for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[6]))

fig = plt.figure()

# plot highs on a chart with dates
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Daily high temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


fig.autofmt_xdate()

plt.show()

# Matplotlib's pyplot API has a convenience function called subplots() which is a utility wrapper and helps in creating common layouts of subplots, including enclosing figure object, in a single call.

fig2, a = plt.subplots(2)
a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")
plt.show()
