import pytest
from src.flatten_xyz import flatten
from src.flatten_xyz.exception import InvalidArgumentException

def test_simple_flatten():
   f =  flatten.Flatten()
   assert f.flatten([1, [2, [3, [4, 5]]]]) == [1, 2, 3, 4, 5]

def test_simple_failed_flatten():
   f =  flatten.Flatten()
   assert f.flatten([1, [2, [3, [4, 5]]]]) != [1, 4, 3, 4, 5]

def test_complex_flatten():
   f =  flatten.Flatten()
   assert f.flatten([[0,1],[[2,[3,[4,[5,[6]]]]]],[7,8]]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_raise_exeption():
   with  pytest.raises(InvalidArgumentException):
       f =  flatten.Flatten()
       f.flatten([1, ['a', [3, [4, 5]]]])
   
