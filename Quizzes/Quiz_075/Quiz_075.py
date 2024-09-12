import matplotlib.pyplot as plt


def quantity_k(msg):
    n = msg
    k = 0
    while k+n+1 > 2**k:
        k += 1
    return k

def efficiency_graph():
    x = range(1, 1000)
    y = [i/(quantity_k(i) + i) for i in x]
    plt.plot(x, y)
    plt.show()

efficiency_graph()