#Adding parent directory to path so we can import base_functions
import sys
sys.path.append('..')

from unittest import TestCase
from base_functions import base_functions

class base_functions_unit_test(TestCase, base_functions):
    """docstring for base_functions_unit_test.
    Unit Tests to test base_functions"""
    def __init__(self):
        super(base_functions_unit_test, self).__init__()

    def test_getFileName(self):
        possible_Index_Values = [x for x in range(0, 100)]
        possible_file_formats = ['md', 'HTML']
