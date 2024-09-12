def check_message(message: str):
    num = 0
    for i in range(1, len(message)):
        if message[i] == '1':
            num += 1
    return num%2 == int(message[0])

print("100111001011001110010110011100101")
print(check_message("100111001011001110010110011100101"))