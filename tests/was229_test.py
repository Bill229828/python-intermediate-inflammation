import numpy as np
import numpy.testing as npt
import pytest
from inflammation .models import daily_mean
data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')
data=[[1, 2],
 [3, 4],
 [5, 6]]


#Automating a test using npt.assert_array_equal
test_input = np.array([[1, 2], [3, 4], [5, 6]])
test_result = np.array([3, 4])
npt.assert_array_equal(daily_mean(test_input), test_result)

test_input = np.array([[2, 0], [4, 0]])
test_result = np.array([3, 0])
npt.assert_array_equal(daily_mean(test_input), test_result)

test_input = np.array([[0, 0], [0, 0], [0, 0]])
test_result = np.array([0, 0])
npt.assert_array_equal(daily_mean(test_input), test_result)

test_input = np.array([[1, 2], [3, 4], [5, 6]])
test_result = np.array([3, 4])
npt.assert_array_equal(daily_mean(test_input), test_result)



#Testing framework -Write a number of test inputs and results
#within different functions

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 1])

    # Need to use NumPy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

test_daily_mean_zeros()

def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 5])

    # Need to use NumPy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

    #test_daily_mean_zeros
    test_daily_mean_integers()

    print('I got to here')
