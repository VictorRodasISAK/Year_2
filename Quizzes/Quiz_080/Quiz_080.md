# Quiz 080


## Slide Picture

![Screen Shot 2024-09-12 at 11.40.11.png](Screen%20Shot%202024-09-12%20at%2011.40.11.png)
*Fig.1* Quiz 080 Slide Picture


## Python Code
```python
def F(N):
    if len(N) == 1:
        return N[0]
    else:
        M = F(N[1:])
        if N[0] > M:
            return N[0]
        else:
            return M
```



## Work on paper

![WhatsApp Image 2024-09-12 at 11.37.32.jpeg](WhatsApp%20Image%202024-09-12%20at%2011.37.32.jpeg)
*Fig.2* Quiz 080 Work on paper


## Proof

![Screen Shot 2024-09-12 at 11.41.14.png](Screen%20Shot%202024-09-12%20at%2011.41.14.png)
*Fig.3* Quiz 080 Proof