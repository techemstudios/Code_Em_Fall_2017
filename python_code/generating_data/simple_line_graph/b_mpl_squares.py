"""
Plotting a simple line graph with matplotlib.

Now changing the type of label and thickness of the graph.

"""

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# Set thickness of line
plt.plot(squares, linewidth = 5)

# Set chart title and labeling the axes
plt.title("Square Numbers", fontsize = 28)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()


