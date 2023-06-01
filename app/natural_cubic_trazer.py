from typing import List
from app.schemas import Interval

class NaturalCubicTracer:
    intervals: List[Interval]

    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals

    def get_a_i(self, i: int):
        if (0 <= i < len(self.intervals)):
            return self.intervals[i].f(x=self.intervals[i].x[0])
        elif (i == len(self.intervals)):
            return self.intervals[i - 1].f(x=self.intervals[i - 1].x[-1])
        

    def show_info(self):
        for i, interval in enumerate(self.intervals):
            print(f'Segment: S_{i}')
            print(f'x: {interval.x}\nf(x): {interval._y}')
            print(f'height: {interval.get_height()}')
            print()

        for i in range(len(self.intervals) + 1):
            print(f'a_{i} = {self.get_a_i(i)}')

    
    

