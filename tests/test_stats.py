from shop.stats import average, median


def test_average_of_numbers():
    assert average([2, 4, 6]) == 4


def test_median_odd_and_even():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
