from typing import List
from app.schemas import Interval
from app.natural_cubic_trazer import NaturalCubicTracer


S_1 = Interval(x=[1, 2, 5, 6, 7, 8, 10, 13, 17],
               y=[3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])

S_2 = Interval(x=[17, 20, 23, 24, 25, 27, 27.7],
               y=[4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1])

S_3 = Interval(x=[27.7, 28, 29, 30],
               y=[4.1, 4.3, 4.1, 3.0])

natural_cubic_tracer = NaturalCubicTracer(intervals=[S_1, S_2, S_3])

natural_cubic_tracer.show_info()



def show_a_i(intervals: List[Interval]):
    for i, interval in enumerate(intervals):

        print(f'a_{i} = {interval.f(x=interval.x[0])}')

        if i == len(intervals) - 1:
            print(f'a_{i + 1} = {interval.f(x=interval.x[-1])}')



# show_a_i(S)
