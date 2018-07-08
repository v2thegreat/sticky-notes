from time import sleep, gmtime, strftime


class base_functions(object):
	"""Seperate Class for base functions"""
	def __init__(self):
		super(base_functions, self).__init__()


	@staticmethod
	def _getFileName(index_val = None, file_format = 'md'):
		"""
		This function estimates what the name needs to be for the new file by the parameters and how many notes are there

		Args:
			index_val = None (int or None):
				This is the index position of the label that you want to get the file name of.
				Incase no parameter is passed(index_val = None), the self.notesCount property is used to calculate the file name
		"""
		if index_val != None:
			return "Note-{0}.{1}".format(index_val, file_format)


	@staticmethod
	def _getDateTimeStamp(addNewLine = True):
		if addNewLine:
			return '\n###### {}'.format(strftime("%Y-%m-%d ~ %H:%M:%S", gmtime()))

		else:
			return '{}'.format(strftime("%Y-%m-%d ~ %H:%M:%S", gmtime()))


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

if __name__ == '__main__':
	test = base_functions()
	print(test._getFileName(1, 'HTML'))
	print(test._getDateTimeStamp())
	print(test._getLabelTitle(0))
	print('All tests Ran successfully...')
