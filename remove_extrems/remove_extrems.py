from sort_algos import sort


def remove_extrems(series, setting):
    if series is None:  # processing of the particular case None
        return []
    if len(series) == 1: return series  # processing of the particular case where the series contains a single data
    data_tested = 0
    median_index, median_value = median(series)
    for i, _ in enumerate(series):  # loop on each of the data
        test = series[data_tested] - series[median_index]
        data_tested += 1
        if test >= setting:  # test if the data is judged as extreme
            series.remove(series[data_tested - 1])
    return series  # return the new series without any extreme data


def median(series):
    """
    Compute the median
    :param series: a list of integers
    :return: the index of the median value, the median value of the series
    """
    sort.naive(series)
    total = len(series)
    median_index = total // 2
    return median_index, series[median_index]


