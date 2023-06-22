from app.natural_cubic_spline_2 import Interval
from app.natural_cubic_spline_2 import NaturalCubicSpline


def run_example_1():
    x = [0.1, 0.2, 0.3, 0.4]
    y = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
    S_1 = Interval(x=x, y=y)

    S = NaturalCubicSpline(intervals=[S_1])

    x = 0.25
    print(f'S({x}) = { S.aproximate(x=x)}')

    x = 0.35
    print(f'S({x}) = { S.aproximate(x=x)}')

    S.draw_graphic(start=0.1, end=0.4, step=0.01, filename='images/test_1.png')


def run_example_2():
    S_1 = Interval(x=[1, 2, 5, 6, 7, 8, 9, 10, 13, 17],
                   y=[3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 6.9, 7.1, 6.7, 4.5])

    S_2 = Interval(x=[17, 20, 23, 24, 25, 27, 27.7],
                   y=[4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1])

    S_3 = Interval(x=[27.7, 28, 29, 30],
                   y=[4.1, 4.3, 4.1, 3.0])

    S = NaturalCubicSpline(intervals=[S_1, S_2, S_3])

    x = 26
    print(f'S({x}) = { S.aproximate(x=x)}')

    S.draw_graphic(start=1.0, end=30.0, step=0.1, filename='images/test_2.png')


def run_example_3():
    x = [-0.5, -0.25, 0]
    y = [-0.025, 0.335, 1.1]

    S_1 = Interval(x=x, y=y)

    S = NaturalCubicSpline(intervals=[S_1])

    S.draw_graphic(start=-0.5, end=0, step=0.01, filename='images/test_3.png')


run_example_1()
run_example_2()
run_example_3()
