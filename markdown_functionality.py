from os import startfile
from base_functions import base_functions
from markdown import markdownFromFile

class markdown_functionality(base_functions):
	"""Seperate Class to hold markdown methods"""
	def __init__(self):
		super(markdown_functionality, self).__init__()


	def compileAndDisplayMarkdown(self, label_index):
		self._compileMarkDownFile(label_index)
		self._openCompiledMarkDownFile(label_index)


	def _compileMarkDownFile(self, label_index = None):
		"""
		Function to compile the markdown file. Uses markdown's markdownFromFile method and saves it to the file name generated from _getFile
		"""
		inputFileName = self._getFileName(label_index)
		outputFileName = self._getFileName(label_index, 'html')
		html_output = markdownFromFile(inputFileName, outputFileName)


	def _openCompiledMarkDownFile(self, label_index):
		"""
		Function to open the compiled HTML file with os.startfile
		"""
		startfile(self._getFileName(label_index, 'html'))


	def _openMarkDownFile(self, label_index):
		"""
		Function to start the markdown file
		"""
		startfile(self._getFileName(label_index))


if __name__ == '__main__':
    t = markdown_functionality()
    t.compileAndDisplayMarkdown(0)
