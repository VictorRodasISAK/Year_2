# Quiz 079


## Slide Picture

![Screen Shot 2024-09-11 at 0.26.02.png](Screen%20Shot%202024-09-11%20at%200.26.02.png)
*Fig.1* Quiz 079 Slide Picture


## Python Code
```python
def find_k(n):
    k = 0
    while 2**k < n + k + 1:
        k += 1
    return k

def get_positions(k):
    return [2**i - 1 for i in range(k)]

def get_parity_list(k, n, P):
    parity_list = []
    for i in range(P + 1, k + n + 1):
        if i & P == P:
            parity_list.append(i - 1)
    return parity_list

def get_parity(message: str, parity_list):
    parity = 0
    for P in parity_list:
        parity += int(message[P])
    return parity % 2

def get_msg_with_parity(message: str, positions, k):
    res = [-1 for _ in range(len(message) + k)]
    msg_index = 0
    for i in range(len(res)):
        if i not in positions:
            res[i] = message[msg_index]
            msg_index += 1
    return res

def hamming_code(message: str):
    n = len(message)
    k = find_k(n)
    pos = get_positions(k)
    res = get_msg_with_parity(message, pos, k)
    for P in pos:
        parity_list = get_parity_list(k, n, P)
        parity = get_parity(res, parity_list)
        res[P] = parity
    res = [str(i) for i in res]
    return ''.join(res)
```


## Work on paper

![WhatsApp Image 2024-09-11 at 23.46.40.jpeg](WhatsApp%20Image%202024-09-11%20at%2023.46.40.jpeg)
*Fig.2* Quiz 079 Work on paper


## Proof

![Screen Shot 2024-09-12 at 12.56.37.png](Screen%20Shot%202024-09-12%20at%2012.56.37.png)
*Fig.3* Quiz 079 Proof