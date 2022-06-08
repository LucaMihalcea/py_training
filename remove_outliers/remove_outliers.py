from sort_algos import sort
from typing import List


def remove_outliers(series: List[int], distance_to_the_median: int) -> List[int]:
    if series is None:  # processing of the particular case None
        return []

    if len(series) == 1: return series  # processing of the particular case where the series contains a single data

    median_index, median_value = median(series)

    for candidate_index, candidate_value in enumerate(series):  # loop on each of the data
        if is_extreme(median_value, candidate_value, distance_to_the_median):  # test if the data is judged as extreme
            series.pop(candidate_index)

    return series  # return the new series without any extreme data


def is_extreme(median_value: int, candidate: int, distance: int):
    return candidate - median_value >= distance


def median(series: List[int]) -> (int, int):
    """
    Compute the median
    :param series: a list of integers when the series is None or empty then it will raise an error
    :return: the index of the median value and the median value of the series
    """
    if series is None or len(series) == 0:
        raise ValueError("series is none or empty")

    sort.naive(series)
    total = len(series)
    median_index = total // 2
    return median_index, series[median_index]
