import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pjo

def test_calculate_possible_pairs_in_ratio():
    assert pjo.calculate_possible_pairs_in_ratio(2, 100) == [{'ratio': 2.0, 'x1': 1, 'x2': 2}, {'ratio': 2.0, 'x1': 50, 'x2': 100}]
    assert pjo.calculate_possible_pairs_in_ratio(1.66, 100) == [{'ratio': 1.6552, 'x1': 29, 'x2': 48}, {'ratio': 1.6562, 'x1': 32, 'x2': 53}, {'ratio': 1.6571, 'x1': 35, 'x2': 58}, {'ratio': 1.6579, 'x1': 38, 'x2': 63}, {'ratio': 1.6585, 'x1': 41, 'x2': 68}, {'ratio': 1.6591, 'x1': 44, 'x2': 73}, {'ratio': 1.6596, 'x1': 47, 'x2': 78}, {'ratio': 1.66, 'x1': 50, 'x2': 83}]
    assert pjo.calculate_possible_pairs_in_ratio(0.23, 300) == [{'ratio': 0.2308, 'x1': 13, 'x2': 3}, {'ratio': 0.2295, 'x1': 61, 'x2': 14}, {'ratio': 0.2297, 'x1': 74, 'x2': 17}, {'ratio': 0.2299, 'x1': 87, 'x2': 20}, {'ratio': 0.23, 'x1': 100, 'x2': 23}, {'ratio': 0.23, 'x1': 1300, 'x2': 299}]
    assert pjo.calculate_possible_pairs_in_ratio(0.5, 10000) == [{'ratio': 0.5, 'x1': 2, 'x2': 1}, {'ratio': 0.5, 'x1': 20000, 'x2': 10000}]

def test_get_item_ratio():
    assert pjo.get_item_ratio(1, 2) == 0.5
    assert pjo.get_item_ratio(2, 1) == 2
    assert pjo.get_item_ratio(1, 100) == 0.01
    assert pjo.get_item_ratio(100, 1) == 100

def test_calculate_full_exchange():
    assert pjo.calculate_full_exchange(1.71, 1, 1.75, 1, 100) == ([{'ratio': 1.7143, 'x1': 7, 'x2': 12}, {'ratio': 1.7059, 'x1': 17, 'x2': 29}, {'ratio': 1.7083, 'x1': 24, 'x2': 41}, {'ratio': 1.7097, 'x1': 31, 'x2': 53}], [{'ratio': 1.75, 'x1': 4, 'x2': 7}, {'ratio': 1.75, 'x1': 56, 'x2': 98}], 4.0)
    assert pjo.calculate_full_exchange(1, 1.71, 1, 1.75, 100) == ([{'ratio': 0.5833, 'x1': 12, 'x2': 7}, {'ratio': 0.5862, 'x1': 29, 'x2': 17}, {'ratio': 0.5854, 'x1': 41, 'x2': 24}, {'ratio': 0.5849, 'x1': 53, 'x2': 31}], [{'ratio': 0.5714, 'x1': 7, 'x2': 4}], 4.0)
    assert pjo.calculate_full_exchange(25, 1, 30, 1, 1000) == ([{'ratio': 25.0, 'x1': 1, 'x2': 25}, {'ratio': 25.0, 'x1': 40, 'x2': 1000}], [{'ratio': 30.0, 'x1': 1, 'x2': 30}, {'ratio': 30.0, 'x1': 33, 'x2': 990}], 5000)
    assert pjo.calculate_full_exchange(1, 25, 1, 30, 1000) == ([{'ratio': 0.0435, 'x1': 23, 'x2': 1}, {'ratio': 0.0417, 'x1': 24, 'x2': 1}, {'ratio': 0.04, 'x1': 25, 'x2': 1}], [{'ratio': 0.037, 'x1': 27, 'x2': 1}, {'ratio': 0.0357, 'x1': 28, 'x2': 1}, {'ratio': 0.0345, 'x1': 29, 'x2': 1}, {'ratio': 0.0333, 'x1': 30, 'x2': 1}, {'ratio': 0.0328, 'x1': 61, 'x2': 2}, {'ratio': 0.033, 'x1': 91, 'x2': 3}], 5000)

if __name__ == "__main__":
    test_calculate_possible_pairs_in_ratio()
    test_get_item_ratio()
    test_calculate_full_exchange()