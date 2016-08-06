import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# s = argument sets the size of the dots
# c = dot color (default blue)
# can define custom colors usin RGB color model by passing in a tuple of decimals
# edgecolor (default black diameter)
# plt.scatter(x_values, y_values, c=(0.8, 0, 0.8), edgecolor='none', s=40)

# a colormap is a series of colors in a gradient that moves from a starting to
# ending color
# colormaps are used in visualizations to emphasize a pattern in the data
# ex: low vaues = light colors, high values = darker colors
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, edgecolor='none', s=40)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# simply display plot
plt.show()

# automatically save the plot to a file
# first argument specifies filename
# second argument trims extra whitespace from the plot
# plt.savefig('square_plot.png', bbox_inches='tight')
