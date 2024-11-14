from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two a D6
die_1 = Die()
die_2 = Die()

results = []

# Make some rolls and store them in a list.
for roll_num in range(1000):  # Roll the Die 1,000
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling  one D6 1000', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')