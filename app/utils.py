import numpy as np
import matplotlib.pyplot as plt
from app.natural_cubic_trazer import NaturalCubicTracer


def show_graphic(S: NaturalCubicTracer):
    x = []
    y = []

    for i in np.arange(1.0, 30.0, 1):
        x.append(i)
        y.append(S.aproximate(x=i))

    plt.plot(x, y)

    plt.xlim(0, 30)
    plt.ylim(0, 8)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')

    plt.show()
