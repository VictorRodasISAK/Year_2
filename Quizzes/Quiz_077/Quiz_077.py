def parities(k,n,p):
    p_list = []
    for i in range(0, k+n):
        if i & p == p:
            p_list.append(i)
    return p_list

print(parities(7, 2, 1))