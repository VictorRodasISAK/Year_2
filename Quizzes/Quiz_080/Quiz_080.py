def F(N):
    if len(N) == 1:
        return N[0]
    else:
        M = F(N[1:])
        if N[0] > M:
            return N[0]
        else:
            return M

N = [3,5,7,8]
print(N)
print(F(N))


