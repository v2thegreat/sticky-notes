from time import sleep, gmtime, strftime
from Defaults.base_functions import *
from os import listdir, remove
import re

class base_functions(object):
	"""Base Functions
	This Class Contains functions that are inherited by the Backend class"""
	def __init__(self):
		super(base_functions, self).__init__()


	@staticmethod
	def _getFileName(index_val, file_format = 'md'):
		"""
		This function estimates what the name needs to be for the new file by the parameters and how many notes are there

		Args:
			index_val (int):
				This is the index position of the label that you want to get the file name of.

			file_format (str):
				This is the parameter that generates the
		"""
		if index_val != None:
			return DFLT_FILE_NAME_FORMAT.format(index_val, file_format)


	@staticmethod
	def _getDateTimeStamp(addNewLine = True):
		if addNewLine:
			return '\n###### {}'.format(strftime(DFLT_TIME_STAMP_FORMAT, gmtime()))

		else:
			return '{}'.format(strftime(DFLT_TIME_STAMP_FORMAT, gmtime()))


	@staticmethod
	def _getLabelTitle(label_index = None):
		"""
		Args:
			label_index = None (int or None):
				This property is used to check which label is to be used
				If no label index is passed, then it
				 defaults to the self.notesCount

		Function to get the title of the label from the label_index
		It does so by reading the first line of the file (which is assumed to be the title) and returns it
		"""
		text_lst = open(base_functions._getFileName(label_index)).readlines()

		for possibleTitle in text_lst:
			if base_functions._checksForPossibleTitle(possibleTitle):
				title = possibleTitle.replace('\n', '')
				break
		else:
			title = "<No Title Found>"

		title = title.replace('#', '').lstrip()
		return title


	@staticmethod
	def _checksForPossibleTitle(possibleTitle):
		"""
		Args:
			possibleTitle = str
				This parameter is what is to be checked against

		Checks to see if
		"""
		ch1 = '#' in possibleTitle
		ch2 = '~' not in possibleTitle
		return ch1 * ch2


	@staticmethod
	def _resetNotes():
		removalCounter = 0
		for x in listdir():
			if re.match(MTCH_STR_MARKDOWN, x) or re.match(MTCH_STR_HTML, x):
				remove(x)
				removalCounter += 1

		print('{} items removed'.format(removalCounter))

if __name__ == '__main__':
	base_functions._resetNotes()
