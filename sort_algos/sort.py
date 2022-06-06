def naive(x):
    if x is None: return []
    pos = 0
    for i in range(len(x)):
        for idx, num in enumerate(x):
            if x[pos] > num:
                x.insert(0, num)
                x.pop(idx + 1)
        pos += 1
    return x