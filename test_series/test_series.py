from series.series import fibonacci
from series.series import lucas
import pytest


def fibonacci_test1():
    actual=fibonacci(9)
    expected=34

    assert_actual == expected


def lucas_test1():
    actual = lucas(9)
    expected=76

    assert_actual == expected