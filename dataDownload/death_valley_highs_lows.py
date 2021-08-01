import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily maximum and min temperature in 2018\nDeath valley in California", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("temperature(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
