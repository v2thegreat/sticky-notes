from threading import Thread
from base_functions import base_functions
from time import sleep
from os import stat

class threading_functions(base_functions):
	"""docstring for threading_functions."""
	def __init__(self):
		super(threading_functions, self).__init__()


	def _createNewThread(self):
		"""
		This function is used to create a new thread for the function to keep updating the lable text
		This is done so that the label can be updated each time the file is saved. No easy clear means are avalible that enables us to check the file only when the file is open
			1. Running this takes less space (approximately 0.09% of my cpu), and minute read times
			2. the function: self.updateLabelTextForNewNote checks every 0.5 seconds, so it lowers disk read time
			3. the thread itself is a Daemon thread (this means that it closes when the main program closes)
		"""
		fileIndex = self.notesCount
		t = Thread(target = self.updateLabelTextForNewNote, args = (fileIndex,))
		t.setDaemon(True)
		t.start()


	def updateLabelTextForNewNote(self, label_index):
		"""
		Args:
			lable_index (int):
				This it the index of the file that needs to be read again and again so that the label's text can be updated

		This function keeps checking if the text in the file for this label has been updated or not, and if so, it updates the text of the label
		"""
		lastModified = -1
		fileName = self._getFileName(label_index)

		while True:
			sleep(0.5)
			self.__updateLabelWithNewTitle(label_index)
			lastModified = self.__addTimeStampIfModified(label_index, fileName, lastModified)


	def __updateLabelWithNewTitle(self, label_index): #Runtime/threading --updates the labels title ---threading
		newLabelTitle = self._getLabelTitle(label_index)
		self._getLblNoteLabel(label_index).setText(newLabelTitle)


	def __addTimeStampIfModified(self, label_index, fileName, lastModified = -1): #Runtime --Adds timestamp ---threading
		timeOfLastModification = stat(fileName)[8]

		if lastModified == -1:
			return timeOfLastModification

		elif timeOfLastModification != lastModified:
			timeStamp = threading_functions._getDateTimeStamp()
			open(fileName, 'a').write(timeStamp)

		return stat(fileName)[8]
