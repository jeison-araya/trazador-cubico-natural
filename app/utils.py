import matplotlib.pyplot as plt


def show_graphic(x, y):
    plt.plot(x, y)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')

    plt.show()
