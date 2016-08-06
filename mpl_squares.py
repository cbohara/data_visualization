# import pyplot module using the alias plt
import matplotlib.pyplot as plt

# first x value defaults to 0, so we are overriding default first point to 1
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# first parameter specifies x values, second parameter specifies y values
plt.plot(input_values, squares, linewidth=5)

# set chart title and lable axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
