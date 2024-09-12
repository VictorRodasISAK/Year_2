# Quiz 075


## Slide Picture

![Screen Shot 2024-09-10 at 23.27.48.png](Screen%20Shot%202024-09-10%20at%2023.27.48.png)
*Fig.1* Quiz 075 Slide Picture


## Python Code
```python
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
```

## Work on paper

![WhatsApp Image 2024-09-11 at 23.44.59.jpeg](WhatsApp%20Image%202024-09-11%20at%2023.44.59.jpeg)
*Fig.2* Quiz 075 Work on paper


## Proof

![Screen Shot 2024-09-10 at 23.29.06.png](Screen%20Shot%202024-09-10%20at%2023.29.06.png)
*Fig.3* Quiz 075 Proof