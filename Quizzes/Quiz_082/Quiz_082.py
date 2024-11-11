def FUNC(N):
    if N == 0 or N == 1:
        return 1
    return N * FUNC(N - 1)

print(FUNC(7))