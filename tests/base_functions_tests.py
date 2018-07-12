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
        Test for _getFileName

        Test is done by running _getFileName with all the parameters that are used or are expected to be used, and this is checked with all the expected values
        """
        from test_outputs.getFileName import expected_outputs
        possible_Index_Values = [x for x in range(0, 100)]
        possible_file_formats = ['md', 'HTML']

        possible_inputs = product(possible_Index_Values, possible_file_formats)
        given_outputs = [self._getFileName(indx_val, fl_frmt) for indx_val, fl_frmt in possible_inputs]

        for gvn, expctd in zip(given_outputs, expected_outputs):
            assert gvn == expctd


    def test_getDateTimeStamp(self):
        """
        Test for _getDateTimeStamp

        Test is done by
            * checking if _getDateTimeStamp returns anything at all
            * checking if the retured value is a string
        """
        assert self._getDateTimeStamp(addNewLine = True) != None
        assert self._getDateTimeStamp(addNewLine = False) != None
        assert isinstance(self._getDateTimeStamp(addNewLine = True), str)
        assert isinstance(self._getDateTimeStamp(addNewLine = False), str)


    def test_checksForPossibleTitle(self):
        """
        Test for _checksForPossibleTitle

        Test is done by
            * Generating possible Titles
            * Ensuring that all outputs are correct
                * Checking if the titles have been confused with actual timestamps
        """
        from test_inputs.checksForPossibleTitle import test_inputs
        from test_outputs.checksForPossibleTitle import expected_outputs

        for pos, input in enumerate(test_inputs):
            try:
                assert self._checksForPossibleTitle(input) == expected_outputs[pos]
            except AssertionError:
                print(input, self._checksForPossibleTitle(input), expected_outputs[pos])


if __name__ == '__main__':
    main()
