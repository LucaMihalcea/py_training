from sort_algos import sort


def remove_extrems(series, setting):
    if series is None:                                      #processing of the particular case None
        return []
    if len(series) == 1: return series                      #processing of the particular case where the series contains a single data
    sort.naive(series)
    total = len(series)
    median_pos = total // 2
    data_tested = 0
    for i in range(total):                                  #loop on each of the data
        test = series[data_tested] - series[median_pos]
        data_tested += 1
        if test >= setting:                                 #test if the data is judged as extreme
            series.remove(series[data_tested - 1])
    return series                                           #return the new series without any extreme data





