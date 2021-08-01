import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # # get every number's index and values by function enumerate
    # for index, column_header in enumerate(header_row):Daily maximum temperature in July 2018
    #     print(column_header, index)

    # reader read the file data by line,split by ","
    highs, dates, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(date)
        highs.append(high)
        lows.append(low)

    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    ax.set_title("Daily maximum and min temperature in 2018", fontsize=24)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("temperature(F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
