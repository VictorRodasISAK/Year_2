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

print(get_msg(4, 3))
print(get_positions(5))