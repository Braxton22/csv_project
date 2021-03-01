# Import Modules
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Create a list of files to iterate through
Files = ["sitka_weather_2018_simple.csv", "death_valley_2018_simple.csv"]

# Create subplots
fig, a = plt.subplots(2)

# Create a list to store names for figure title
Names = []

# Create a variable for the figure title to add on to
Title = "Temperature comparison between"

# Iterate with len(Files) as the condition, so twice (indices 0 and 1)
for F in range(len(Files)):

    # Create lists for highs, lows, dates
    Highs = []
    Lows = []
    Dates = []

    # Create dictionary for the indices
    indices = {}

    # Open File
    File = open(Files[F], "r")
    csv_file = csv.reader(File, delimiter=",")

    # Designate header row
    header_row = next(csv_file)

    # Set the indices to be based on the column header
    for index, column_header in enumerate(header_row):
        indices[column_header] = index

    # Iterate through the csv file
    for row in csv_file:
        try:
            # store highs, lows, dates and name in variables
            high = int(row[indices["TMAX"]])
            low = int(row[indices["TMIN"]])
            converted_date = datetime.strptime(row[indices["DATE"]], "%Y-%m-%d")
            Name = row[indices["NAME"]]
            # if the name isn't in the names list, append to it
            if Name not in Names:
                Names.append(Name)
        # If you run into a value error, print the line thats missing the data
        except ValueError:
            print(f"Missing data for {converted_date}")
        else:
            # append to lists
            Highs.append(int(row[indices["TMAX"]]))
            Lows.append(int(row[indices["TMIN"]]))
            Dates.append(converted_date)

    # Close File
    File.close

    # Plot and fill between, set the title for each graph
    a[F].plot(Dates, Highs, c="red")
    a[F].plot(Dates, Lows, c="blue")
    a[F].fill_between(Dates, Highs, Lows, facecolor="blue", alpha=0.1)
    a[F].set_title(Name)

    if F > 0:
        Title += " " + "and " + Names[F]
    else:
        Title += " " + Names[F]


# Set the size of the figure so that it is immediately sized correctly
fig.set_size_inches(15, 6)

# Use the title variable to set the figure title
fig.suptitle(Title)

# Format the x dates
fig.autofmt_xdate()

# Show the figure
plt.show()
