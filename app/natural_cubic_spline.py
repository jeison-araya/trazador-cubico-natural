from typing import List
from sympy import symbols, solve, Eq


class Interval:
    x: List[float] = []
    y: List[float] = []
    h: List[float] = []
    n: int = None
    a = []
    b = []
    c = []
    d = []
    s = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x) - 1
        self.h = self._calculate_heights()
        self.a = self._calculate_a_values()
        self.c = self._calculate_c_values()
        self.b = self._calculate_b_values()
        self.d = self._calculate_d_values()
        self.s = self._build_s()

    def _calculate_a_values(self):
        return self.y

    def _calculate_c_values(self):
        c = [0]  # c_0 = 0

        for j in range(1, self.n):
            c.append(symbols(f'c_{j}'))

        c.append(0)  # c_n = 0
        c_j = ''
        equations = []

        for j in range(1, self.n):
            equation = self._build_c_j_equation(
                h=self.h,
                a=self.a,
                c=c,
                j=j)
            c_j += f'c_{j} '

            equations.append(Eq(equation['equation'], equation['solution']))

        c_j = c_j[:-1]  # Remove last space

        solutions: dict = solve((equations), (symbols(c_j)))

        # Replace c_j with the solution
        for j in range(1, self.n):
            solution = solutions.popitem()
            c[j] = solution[1]

        return c

    def _build_c_j_equation(self, h: List[float], a: List[float], c: List[float], j: int) -> dict:

        return {
            'equation': (h[j-1] * c[j-1]) + ((2.0 * (h[j-1] + h[j])) * c[j]) + (h[j]*c[j+1]),
            'solution': ((3.0 / h[j]) * (a[j+1] - a[j])) - ((3.0 / h[j-1]) * (a[j] - a[j-1]))
        }

    def _calculate_b_values(self):
        b = []

        for j in range(self.n):
            b.append((1.0 / self.h[j]) * (self.a[j+1] - self.a[j]) -
                     (self.h[j] / 3.0) * (2.0 * self.c[j] + self.c[j+1]))
        return b

    def _calculate_d_values(self):
        d = []

        for j in range(self.n):
            d.append((self.c[j+1] - self.c[j]) / (3.0 * self.h[j]))
        return d

    def _calculate_heights(self):
        heights = []

        for i in range(len(self.x) - 1):
            heights.append(self.x[i+1] - self.x[i])

        return heights

    def _build_s(self):
        s = []

        for j in range(self.n):
            s.append(self._build_s_j(j))

        return s

    def _build_s_j(self, j: int, x=symbols('x')):
        return self.a[j] + (self.b[j] * (x - self.x[j])) + (self.c[j] * (x - self.x[j])**2) + (self.d[j] * (x - self.x[j])**3)

    def aproximate(self, x: float):
        """
        Returns aproximation of f(x) using the interval
        """
        for j in range(self.n):
            if self.x[j] <= x <= self.x[j+1]:
                return self.s[j].subs('x', x)

    def __str__(self) -> str:
        return f"""
        x: {self.x}
        y: {self.y}
        h: {self.h}
        a: {self.a}
        b: {self.b}
        c: {self.c}
        d: {self.d}
        s: {[f'S_{j}: {s}' for j, s in enumerate(self.s)]}
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
