# Quiz 073


## Slide Picture

![Screen Shot 2024-09-10 at 23.12.31.png](Screen%20Shot%202024-09-10%20at%2023.12.31.png)


*Fig.1* Quiz 073 Slide Picture


## Python Code

```python
def check(msg):
    i0 = 0
    i1 = len(msg) / 3
    i2 = len(msg) / 3 * 2

    for i in range(len(msg)/3):
        if msg[i0] != msg[i1] or msg[i0] != msg[i2] or msg[i1] != msg[i2]:
            return True
        i0 += 1
        i1 += 1
        i2 += 1
    return False

def correction(msg):
    i0 = 0
    i1 = len(msg) / 3
    i2 = len(msg) / 3 * 2
    res = ""

    for i in range(len(msg)/3):
        if msg[i0] == msg[i1] or msg[i0] == msg[i2]:
            res += msg[i0]
        elif msg[i1] == msg[i2]:
            res += msg[i1]
        else:
            print("Error")
        i0 += 1
        i1 += 1
        i2 += 1
    return res
```    
    

## Work on paper

![WhatsApp Image 2024-09-11 at 23.44.19.jpeg](WhatsApp%20Image%202024-09-11%20at%2023.44.19.jpeg)
*Fig.2* Quiz 073 Work on paper


## Proof


![Screen Shot 2024-09-10 at 23.22.42.png](Screen%20Shot%202024-09-10%20at%2023.22.42.png)


*Fig.3* Quiz 073 Proof

