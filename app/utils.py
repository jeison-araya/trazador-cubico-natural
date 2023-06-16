import matplotlib.pyplot as plt


def show_graphic(x, y):
    plt.plot(x, y)

    plt.xlim(0, 30)
    plt.ylim(0, 8)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of Points')

    plt.show()
