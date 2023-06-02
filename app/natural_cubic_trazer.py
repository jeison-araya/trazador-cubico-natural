from typing import List
from app.schemas import Interval
from sympy import symbols, solve, Eq


class NaturalCubicTracer:
    intervals: List[Interval]
    n = None
    h = []
    a = []
    b = []
    c = []
    d = []

    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals
        self.n = len(intervals)
        self.h = [interval.get_height() for interval in intervals]
        self.a = self._calculate_a_values()
        self.c = self._calculate_c_values()
        self.b = self._calculate_b_values()
        self.d = self._calculate_d_values()

    def _calculate_a_values(self):
        a = []
        for i in range(self.n):
            a.append(self.intervals[i].f(x=self.intervals[i].x[0]))
        a.append(self.intervals[-1].f(x=self.intervals[-1].x[-1]))

        return a

    def _calculate_c_values(self):
        c = []
        c.append(0)  # c_0 = 0

        for i in range(1, self.n):
            c.append(symbols(f'c_{i}'))
        c.append(0)  # c_n = 0

        c_i = ''
        equations = []

        for i in range(1, self.n):
            equation = self._build_c_i_equation(
                h=self.h,
                a=self.a,
                c=c,
                i=i)
            c_i += f'c_{i} '
            print(equation)
            equations.append(Eq(equation['equation'], equation['solution']))

        c_i = c_i[:-1]  # Remove last space

        solutions: dict = solve((equations), (symbols(c_i)))

        for i in range(1, self.n):
            solution = solutions.popitem()
            c[i] = solution[1]

        return c

    def _build_c_i_equation(self, h: List[float], a: List[float], c: List[float], i: int) -> dict:
        return {
            'equation': (h[i-1] * c[i-1]) + ((2.0 * (h[i-1] + h[i])) * c[i]) + (h[i]*c[i+1]),
            'solution': ((3.0 / h[i]) * (a[i+1] - a[i])) - ((3.0 / h[i-1]) * (a[i] - a[i-1]))
        }

    def _calculate_b_values(self):
        b = []
        for i in range(self.n):
            b.append((1.0 / self.h[i]) * (self.a[i+1] - self.a[i]) -
                     (self.h[i] / 3.0) * (2.0 * self.c[i] + self.c[i+1]))

        return b

    def _calculate_d_values(self):
        d = []
        for i in range(self.n):
            d.append((self.c[i+1] - self.c[i]) / (3.0 * self.h[i]))

        return d

    def aproximate(self, x: float):
        for i in range(self.n):
            if self.intervals[i].x[0] <= x <= self.intervals[i].x[-1]:
                return self.a[i] + self.b[i] * (x - self.intervals[i].x[0]) + self.c[i] * (x - self.intervals[i].x[0]) ** 2 + self.d[i] * (x - self.intervals[i].x[0]) ** 3

    def show_info(self):
        print(f'n: {self.n}')
        print(f'h_i: {self.h}')
        print(f'a_i: {self.a}')
        print(f'b_i: {self.b}')
        print(f'c_i: {self.c}')
        print(f'd_i: {self.d}')
