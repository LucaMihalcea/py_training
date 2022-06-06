def num_to_list(x):
    result = []
    if x == 0:
        return [0]
    if x == None:
        return []
    x = abs(x)
    while x > 0:
        y = x % 10
        x = x // 10
        result.append(y)
    result.reverse()
    return result
