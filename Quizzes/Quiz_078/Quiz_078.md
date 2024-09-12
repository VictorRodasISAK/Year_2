# Quiz 078


## Slide Picture

![Screen Shot 2024-09-11 at 0.16.24.png](Screen%20Shot%202024-09-11%20at%200.16.24.png)
*Fig.1* Quiz 078 Slide Picture


## Python Code
```python
def parity(message: str, positions, k):
    res = [-1 for l in range(len(message) + k)]
    msg_index = 0
    for i in range(len(res)):
        if i not in positions:
            res[i] = message[msg_index]
            msg_index += 1
    return res
```

## Work on paper

![WhatsApp Image 2024-09-11 at 23.46.28.jpeg](WhatsApp%20Image%202024-09-11%20at%2023.46.28.jpeg)
*Fig.2* Quiz 078 Work on paper


## Proof

![Screen Shot 2024-09-11 at 0.16.45.png](Screen%20Shot%202024-09-11%20at%200.16.45.png)
*Fig.3* Quiz 078 Proof