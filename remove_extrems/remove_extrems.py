from sort_algos import sort


def remove_extrems(series, setting):
    if series is None:  # processing of the particular case None
        return []

    if len(series) == 1: return series  # processing of the particular case where the series contains a single data
    median_index, median_value = median(series)

    for candidate_index, candidate_value in enumerate(series):  # loop on each of the data
        if candidate_value - median_value >= setting:  # test if the data is judged as extreme
            series.pop(candidate_index)

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


