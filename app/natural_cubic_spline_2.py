"""
Using the algorithm from the book "Numerical Analysis" by Burden and Faires
"""
from sympy import symbols
from typing import List


class Interval:
    def __init__(self, x, y):
        self.x = x
        self.a = y
        self.n = len(x)
        self.h: List[float] = [0.0] * (self.n - 1)
        self.alpha: List[float] = [0.0] * (self.n - 1)
        self.l: List[float] = [0.0] * self.n
        self.u: List[float] = [0.0] * (self.n - 1)
        self.z: List[float] = [0.0] * self.n
        self.b: List[float] = [0.0] * (self.n - 1)
        self.c: List[float] = [0.0] * (self.n)
        self.d: List[float] = [0.0] * (self.n - 1)
        self.s = self.build_s()

    def run_algorithm(self):
        self.step_1()
        self.step_2()
        self.step_3()
        self.step_4()
        self.step_5()
        self.step_6()

    def step_1(self):
        for i in range(0, self.n - 1):
            self.h[i] = self.x[i+1] - self.x[i]

    def step_2(self):
        for i in range(1, self.n - 1):
            self.alpha[i] = (3/self.h[i])*(self.a[i+1] - self.a[i]) - \
                (3/self.h[i-1])*(self.a[i] - self.a[i-1])

    def step_3(self):
        self.l[0] = 1
        self.u[0] = 0
        self.z[0] = 0

    def step_4(self):
        for i in range(1, self.n - 1):
            self.l[i] = 2*(self.x[i+1] - self.x[i-1]) - self.h[i-1]*self.u[i-1]
            self.u[i] = self.h[i]/self.l[i]
            self.z[i] = (self.alpha[i] - self.h[i-1]*self.z[i-1])/self.l[i]

    def step_5(self):
        self.l[self.n - 1] = 1
        self.z[self.n - 1] = 0
        self.c[self.n - 1] = 0

    def step_6(self):
        for j in range(self.n - 2, -1, -1):
            self.c[j] = self.z[j] - self.u[j]*self.c[j+1]
            self.b[j] = (self.a[j+1] - self.a[j])/self.h[j] - \
                self.h[j]*(self.c[j+1] + 2*self.c[j])/3
            self.d[j] = (self.c[j+1] - self.c[j])/(3*self.h[j])

    def build_s(self):
        self.run_algorithm()
        x = symbols('x')
        return [self.a[j] + self.b[j]*(x - self.x[j]) + self.c[j]*(x - self.x[j])**2 + self.d[j]*(x - self.x[j])**3 for j in range(0, self.n - 1)]

    def aproximate(self, x: float):
        """
        Returns aproximation of f(x) using the interval
        """
        for j in range(self.n - 1):
            if self.x[j] <= x <= self.x[j+1]:
                return self.s[j].subs('x', x)

    def __str__(self) -> str:
        return f"""

        Interval: {self.x}
        h: {self.h}
        --------------------
        alpha: {self.alpha}
        l: {self.l}
        u: {self.u}
        z: {self.z}
        --------------------
        a: {self.a}
        b: {self.b}
        c: {self.c}
        d: {self.d}
        --------------------
        s:
        {[f'S_{j}: {s}' for j, s in enumerate(self.s)]}
        """


class NaturalCubicSpline:
    intervals: List[Interval] = []

    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals

    def aproximate(self, x: float):
        """
        Returns aproximation of f(x) using the interval
        """
        for j, interval in enumerate(self.intervals):
            if interval.x[0] <= x <= interval.x[-1]:
                return interval.aproximate(x)

    def __str__(self) -> str:
        return '\n'.join([str(interval) for interval in self.intervals])
