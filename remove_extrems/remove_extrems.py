from sort_algos import sort


def remove_ext(serie, p):
    if serie is None:
        return []
    if len(serie) == 1: return serie
    sort.naive(serie)
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





