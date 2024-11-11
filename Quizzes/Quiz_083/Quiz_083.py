def N(x):
    if len(x) == 1:
        return x[0]
    if len(x) == 0:
        return 0
    M = len(x) // 2
    L = N(x[:M])
    R = N(x[M:])
    return L + R

print(N([17,12,15]))