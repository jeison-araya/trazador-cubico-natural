import numpy as np
from app.natural_cubic_spline import Interval, NaturalCubicSpline
from app.utils import show_graphic

# x = [-0.5, -0.25, 0]
# y = [-0.025, 0.335, 1.1]
# interval = Interval(x=x, y=y)
# print(interval)
# y_prima = interval.aproximate(x=-0.3)
# print(y_prima)

# S_1 = Interval(x=[1, 2, 5, 6, 7, 8, 9, 10, 13, 17],
#                y=[3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 6.9, 7.1, 6.7, 4.5])

# S_2 = Interval(x=[17, 20, 23, 24, 25, 27, 27.7],
#                y=[4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1])

# S_3 = Interval(x=[27.7, 28, 29, 30],
#                y=[4.1, 4.3, 4.1, 3.0])

# S = NaturalCubicSpline(intervals=[S_1, S_2, S_3])

# print(S.aproximate(x=26))



x = [0.1, 0.2, 0.3, 0.4]
y = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
interval = Interval(x=x, y=y)


print(interval)

x = []
y = []

for i in np.arange(0.1, 0.4, 0.01):
    x.append(i)
    y.append(interval.aproximate(x=i))
    print(f"{i} -> {interval.aproximate(x=i)}")

show_graphic(x=x, y=y)
