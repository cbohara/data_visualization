import pygal
from die import Die

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(5000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# create a histogram
hist = pygal.Bar()
# histogram details/styling
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# add a series of values to the chart
hist.add('D6 + D10', frequencies)
# render the chart to a SVG file
hist.render_to_file('diff_die_visual.svg')
