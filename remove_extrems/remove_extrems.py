def remove_ext(serie, p):
    if serie is None:
        return []
    if len(serie) == 1: return serie
    tri(serie)
    print(serie)
    tot = len(serie)
    m_p = tot // 2
    x = 0
    if tot == 1:
        return serie
    for i in range(tot):
        test = serie[x] - serie[m_p]
        x = x + 1
        if test >= p:
            serie.remove(serie[x - 1])
        else:
            pass
    return serie


def tri(x):
    pos = 0
    for i in range(len(x)):
        for idx, num in enumerate(x):
            if x[pos] > num:
                x.insert(0, num)
                x.pop(idx + 1)
        pos += 1
    return x



