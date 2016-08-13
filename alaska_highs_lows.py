import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'chapter_16/sitka_weather_2014.csv'
# open the file and store the resulting file object in f
with open(filename) as f:
    # call csv.reader() and pass it the file object as an argument to create a
    # reader object associated with a file, and save it into reader variable
    reader = csv.reader(f)
    # csv module next() function returns the next line in the file when passed
    # the reader object, which contains the file headers
    header_row = next(reader)
    # empty lists to store dates and high temp values
    dates, highs, lows = [], [], []
    for row in reader:
        # properly read and format dates
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # read high values and convert from string to int
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

# plot data
fig = plt.figure(dpi=128, figsize=(10,6))
# pass list of high temps and plot in red
plt.plot(dates, highs, c='red')
# pass list of low temps and plot in blue
plt.plot(dates, lows, c='blue')
# shading an area in the chart between highs and lows
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# formatting details
plt.title("Daily high and low temperatures - 2014", fontsize=24)
# add dates in x axis in pretty format
plt.xlabel('', fontsize=16)
# draw the date labels diagonally to prevent overlap
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
