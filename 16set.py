# Import necessary libraries
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates

# Define the x and y values for the candlestick chart
x = [11, 12, 13, 14]
ohlc_data = [
    (mdates.date2num(x[0]), 10, 12, 9, 11),
    (mdates.date2num(x[1]), 11, 13, 10, 12),
    (mdates.date2num(x[2]), 12, 14, 11, 13),
    (mdates.date2num(x[3]), 13, 15, 12, 14),
]

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the candlestick chart using the candlestick_ohlc function
candlestick_ohlc(ax, ohlc_data, width=0.5, colorup='green', colordown='red')

# Draw a trend line connecting the higher lows
ax.plot(x, [9, 10, 11, 12], color='blue', linestyle='--', label='Trend line')

# Format the x-axis as dates
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Add a title, labels, and a legend
ax.set_title('Candlestick Chart with Trend Line')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.legend()

# Show the plot
plt.show()
