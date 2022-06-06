def num_to_bin(x):
    if x is None: return []
    if x == 0: return [0]
    series = []
    pos = 0
    while x > 0:
        series.insert(pos, x % 2 )
        x = x // 2
    return series