#Adding parent directory to path so we can import base_functions
import sys
sys.path.append('..')

from unittest import TestCase, main
from base_functions import base_functions
from itertools import product


class base_functions_unit_test(TestCase, base_functions):
    """docstring for base_functions_unit_test.
    Unit Tests to test base_functions"""


    def test_getFileName(self):
        """
        Test to checks if _getFileName works

        Test is done by running _getFileName with all the parameters that are used or are expected to be used, and this is checked with all the expected values
        """
        from expected_values.getFileName import expected_outputs
        possible_Index_Values = [x for x in range(0, 100)]
        possible_file_formats = ['md', 'HTML']

        possible_inputs = product(possible_Index_Values, possible_file_formats)
        given_outputs = [self._getFileName(indx_val, fl_frmt) for indx_val, fl_frmt in possible_inputs]

        for gvn, expctd in zip(given_outputs, expected_outputs):
            assert gvn == expctd


    def test_getDateTimeStamp(self):
        """
        Test to check if _getDateTimeStamp works

        Test is done by
            * checking if _getDateTimeStamp returns anything at all
            * checking if the retured value is a string
        """
        assert self._getDateTimeStamp(addNewLine = True) != None
        assert self._getDateTimeStamp(addNewLine = False) != None
        assert isinstance(self._getDateTimeStamp(addNewLine = True), str)
        assert isinstance(self._getDateTimeStamp(addNewLine = False), str)


if __name__ == '__main__':
    main()
