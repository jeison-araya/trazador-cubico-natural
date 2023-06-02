import matplotlib.pyplot as plt
from app.schemas import Interval
from app.natural_cubic_trazer import NaturalCubicTracer
import numpy as np

S_1 = Interval(x=[1, 2, 5, 6, 7, 8, 10, 13, 17],
               y=[3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])

S_2 = Interval(x=[17, 20, 23, 24, 25, 27, 27.7],
               y=[4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1])

S_3 = Interval(x=[27.7, 28, 29, 30],
               y=[4.1, 4.3, 4.1, 3.0])

S = NaturalCubicTracer(intervals=[S_1, S_2, S_3])

S.show_info()


x = []
y = []

for i in np.arange(1.0, 30.0, 1):
    x.append(i)
    y.append(S.aproximate(x=i))

# Set the x-axis and y-axis values
plt.plot(x, y)

# Set the minimum and maximum values for x-axis and y-axis
plt.xlim(0, 30)
plt.ylim(0, 8)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of Points')

# Display the plot
plt.show()