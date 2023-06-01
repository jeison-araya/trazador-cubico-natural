

class Interval:
    x = []
    _y = []

    def __init__(self, x, y):
        self.x = x
        self._y = y

    def f(self, x: float):
        return self._y[self.x.index(x)]
    
    def get_height(self):
        """
        Returns height of the interval h = (b - a)
        """
        return self.x[-1] - self.x[0]


    def __str__(self):
        return f'x: {self.x}\nf(x): {self._y}'