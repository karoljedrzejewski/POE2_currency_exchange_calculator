import pytest
import pjo

def test_calculate_possible_pairs_in_ratio():
    assert pjo.calculate_possible_pairs_in_ratio(2, 100) == [{'ratio': 2.0, 'x1': 1, 'x2': 2}, {'ratio': 2.0, 'x1': 50, 'x2': 100}]
    assert pjo.calculate_possible_pairs_in_ratio(1.66, 100) == [{'ratio': 1.6552, 'x1': 29, 'x2': 48}, {'ratio': 1.6562, 'x1': 32, 'x2': 53}, {'ratio': 1.6571, 'x1': 35, 'x2': 58}, {'ratio': 1.6579, 'x1': 38, 'x2': 63}, {'ratio': 1.6585, 'x1': 41, 'x2': 68}, {'ratio': 1.6591, 'x1': 44, 'x2': 73}, {'ratio': 1.6596, 'x1': 47, 'x2': 78}, {'ratio': 1.66, 'x1': 50, 'x2': 83}]
    assert pjo.calculate_possible_pairs_in_ratio(0.23, 300) == [{'ratio': 0.2308, 'x1': 13, 'x2': 3}, {'ratio': 0.2295, 'x1': 61, 'x2': 14}, {'ratio': 0.2297, 'x1': 74, 'x2': 17}, {'ratio': 0.2299, 'x1': 87, 'x2': 20}, {'ratio': 0.23, 'x1': 100, 'x2': 23}, {'ratio': 0.23, 'x1': 1300, 'x2': 299}]
    assert pjo.calculate_possible_pairs_in_ratio(0.5, 10000) == [{'ratio': 0.5, 'x1': 2, 'x2': 1}, {'ratio': 0.5, 'x1': 20000, 'x2': 10000}]

if __name__ == "__main__":
    test_calculate_possible_pairs_in_ratio()
    