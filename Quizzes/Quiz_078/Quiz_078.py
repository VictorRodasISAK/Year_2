def parity(message: str, positions, k):
    res = [-1 for l in range(len(message) + k)]
    msg_index = 0
    for i in range(len(res)):
        if i not in positions:
            res[i] = message[msg_index]
            msg_index += 1
    return res

print(parity("1011", [0, 1, 3], 3))