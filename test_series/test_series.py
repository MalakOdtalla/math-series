from series.series import fibonacci,lucas ,sum_series
import pytest


# fibonacci tests
def test_fibonacci():
    actual=fibonacci(9)
    expected=34

    assert actual == expected

# lucas tests
def test_lucas():
    actual = lucas(9)
    expected=76

    assert actual == expected

# sum_series tests

def test_sum_series1():
    actual = sum_series (0)
    expected = 0
    assert actual == expected

def test_sum_series2():
    actual = sum_series(0, 0, 1)
    expected = 0
    assert actual == expected


def test_sum_series3():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected