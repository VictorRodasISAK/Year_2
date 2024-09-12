# Quiz 076


## Slide Picture

![Screen Shot 2024-09-11 at 0.07.20.png](Screen%20Shot%202024-09-11%20at%200.07.20.png)
*Fig.1* Quiz 076 Slide Picture


## Python Code
```python
def get_positions(k: int) -> list:
    data = []
    for n in range(k):
        data.append(2**n - 1)
    return data

def get_msg(n, k):
    pos = get_positions(n)
    res = [0 for l in range(n + k)]
    for i in range(len(res)):
        if i in pos:
            res[i] = 1
    return res
```

## Work on paper

![WhatsApp Image 2024-09-11 at 23.45.18.jpeg](WhatsApp%20Image%202024-09-11%20at%2023.45.18.jpeg)
*Fig.2* Quiz 076 Work on paper


## Proof

![Screen Shot 2024-09-11 at 0.07.47.png](Screen%20Shot%202024-09-11%20at%200.07.47.png)
*Fig.3* Quiz 076 Proof