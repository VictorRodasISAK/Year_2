def check(msg):
    i0 = 0
    i1 = len(msg) // 3
    i2 = (len(msg) // 3) * 2

    for i in range(len(msg) // 3):
        if msg[i0] != msg[i1] or msg[i0] != msg[i2] or msg[i1] != msg[i2]:
            return True
        i0 += 1
        i1 += 1
        i2 += 1
    return False

def correction(msg):
    i0 = 0
    i1 = len(msg) // 3
    i2 = (len(msg) // 3) * 2
    res = ""

    for i in range(len(msg) // 3):
        if msg[i0] == msg[i1] or msg[i0] == msg[i2]:
            res += msg[i0]
        elif msg[i1] == msg[i2]:
            res += msg[i1]
        else:
            raise ValueError("Error")

        i0 += 1
        i1 += 1
        i2 += 1
    return res

msg = "100111001011001110010110011100101"
print(check(msg))
print(correction(msg))