def swap(s, i, j):
    L = list(s)
    L[i], L[j] = L[j], L[i]
    return ''.join(L)


def P(s, k):
    if k == len(s):
        return [s]
    else:
        out = []
        for i in range(0, len(s)-1):
            T = swap(s, k, i)
            out.extend(P(T, k + 1))
        return out

print(P("AB", 1))