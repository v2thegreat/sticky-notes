from os import startfile, stat
from time import sleep, gmtime, strftime
from PyQt5 import QtWidgets
from Defaults import *
from UI import stickyNotesUI
from markdown_functionality import markdown_functionality
from threading_functions import threading_functions

class Backend(markdown_functionality, threading_functions, stickyNotesUI):
	"""docstring for Backend"""

	def __init__(self):
		super().__init__()
		self.MainWindow_Dialog = QtWidgets.QMainWindow()
		self.setupUi(self.MainWindow_Dialog)
		self._HideNoteLabels()
		self._setNotesCount()
		self._setFunctionality()
		self.NotesDict = {}


	def _setFunctionality(self):
		print('Setting up button functionality')
		self._setLabels()
		self.lblNote_1.mousePressEvent = (lambda x: self.updateNote(0))
		self.lblNote_2.mousePressEvent = (lambda x: self.updateNote(1))
		self.lblNote_3.mousePressEvent = (lambda x: self.updateNote(2))
		self.lblNote_4.mousePressEvent = (lambda x: self.updateNote(3))
		self.lblNote_5.mousePressEvent = (lambda x: self.updateNote(4))
		self.lblNote_6.mousePressEvent = (lambda x: self.updateNote(5))
		self.lblNote_7.mousePressEvent = (lambda x: self.updateNote(6))
		self.lblNote_8.mousePressEvent = (lambda x: self.updateNote(7))
		self.lblNote_9.mousePressEvent = (lambda x: self.updateNote(8))
		self.lblNote__10.mousePressEvent = (lambda x: self.updateNote(9))
		self.lblNote__11.mousePressEvent = (lambda x: self.updateNote(10))
		self.lblNote__12.mousePressEvent = (lambda x: self.updateNote(11))
		self.lblNote__13.mousePressEvent = (lambda x: self.updateNote(12))
		self.lblNote__14.mousePressEvent = (lambda x: self.updateNote(13))
		self.lblNote__15.mousePressEvent = (lambda x: self.updateNote(14))
		self.lblNote__16.mousePressEvent = (lambda x: self.updateNote(15))
		self.lblNote__17.mousePressEvent = (lambda x: self.updateNote(16))
		self.lblNote__18.mousePressEvent = (lambda x: self.updateNote(17))
		self.lblNote__19.mousePressEvent = (lambda x: self.updateNote(18))
		self.lblNote__20.mousePressEvent = (lambda x: self.updateNote(19))
		self.lblNote__21.mousePressEvent = (lambda x: self.updateNote(20))
		self.lblNote__22.mousePressEvent = (lambda x: self.updateNote(21))
		self.lblNote__23.mousePressEvent = (lambda x: self.updateNote(22))
		self.lblNote__24.mousePressEvent = (lambda x: self.updateNote(23))
		self.lblNote__25.mousePressEvent = (lambda x: self.updateNote(24))
		self.lblNote__26.mousePressEvent = (lambda x: self.updateNote(25))
		self.lblNote__27.mousePressEvent = (lambda x: self.updateNote(26))
		self.lblNote__28.mousePressEvent = (lambda x: self.updateNote(27))
		self.lblNote__29.mousePressEvent = (lambda x: self.updateNote(28))
		self.lblNote__30.mousePressEvent = (lambda x: self.updateNote(29))
		self.pshBtnAdd.clicked.connect(lambda: self.addNote())

		print('Button functionality set')


	def addNote(self):
		"""
		Function to add a new note to the roster of sticky notes

		1. it changes the transparency of the lastest note to make it opaque
		2. Creates a new file where the note must be stored
		3. Creates a new thread to keep checking if the title of the file has been updated or not
		4. Increments self.notesCount until it reaches the maximum label count
		"""
		if not self._isPossibleToAdd():
			return -1

		self._showLabel()
		self._startNewfile()
		self._createNewThread()
		self.notesCount = min(self.MAX_LABEL_COUNT, self.notesCount+1)
		self._saveNoteCount()
		print('Added Notes')


	def _showLabel(self, index_val = None):
		"""
		Args:
			index_val = None (int or None):
				This is the index position of the label that you want to make visible

				Incase no parameter is passed(index_val = None), the self.notesCount property is
				used to check which is the latest value that is going to be made opaque

		Function to change the visibility for the given label
		"""

		lblNote = self._getLblNoteLabel(index_val)
		lblNote.show()


	def _startNewfile(self):
		"""
		The job of this function is to create a new file and add the time stamp. This is where it the users notes are going to be saved for future use
			The name of the file is created with the assistance of the _getFileName function

		Then, it starts the file with the assistance of os.startfile function
			This ensures that the file is opened in the users
			 default text editor
		"""
		timeStamp = Backend._getDateTimeStamp(addNewLine = False)
		open(self._getFileName(self.notesCount), 'w').write("Created at: " + timeStamp + "\n")
		startfile(self._getFileName(self.notesCount))


	def _saveNoteCount(self): #Runtime --saves the total number of notes ---Notes
		"""
		This function is used to save the notesCount
		"""
		open('notesCount.txt', 'w').write(str(self.notesCount))


	def updateNote(self, label_index): #Runtime --Updating Notes ---Notes
		if self.pshBtnViewHTML.isChecked():
			self.compileAndDisplayMarkdown(label_index)

		else:
			if self._checkIfNoteInitialized(label_index):
				print('Invalid Selection')		#Add a condition to set this to false when it is not possible to set

			else:
				self._openMarkDownFile(label_index)


	def _HideNoteLabels(self): #Rungtime/initialization --functionality ---Labels
		"""
		A function used to hide all the note labels

		This function iterates through the sticky notes UI

		Usage:
			At bootup, this is set to hide all labels that are not meant to be seen
		"""
		for nteLbl in self.notesLabelsLst:
			nteLbl.hide()


	def _setNotesCount(self): #initialization --functionality
		try:
			self.notesCount = int(open('notesCount.txt').read())
			print('File successfully found, set notesCount to {0}'.format(self.notesCount))
		except FileNotFoundError:
			self.notesCount = 0
			print('File not found, set notesCount to 0')


	def _setLabels(self): #Runtime --functionality --Labels
		for note_Index in range(0, self.notesCount):
			self._showLabel(note_Index)
			self._getLblNoteLabel(note_Index).setText(self._getLabelTitle(note_Index))


	def _isPossibleToAdd(self): #Runtime --Adding Notes ---Notes
		return self.notesCount < 30


	def _getLblNoteLabel(self, index_val = None): #Runtime --returns a notes_label ---Wrapper
		"""
		Args:
			index_val = None (int or None):
				This is the index position of the label that you want
				Incase no parameter is passed(index_val = None), the self.notesCount property is used to get the label instead

		This function checks
			if the index_val is none
				returns the latest label
			else
				returns the label at that position
		"""
		if index_val == None:
			return self.notesLabelsLst[self.notesCount]
		else:
			return self.notesLabelsLst[index_val]


	def _checkIfNoteInitialized(self, label_index): #Rungtime --checks if a note has been created ---Notes
		return self._getLblNoteLabel(label_index).text() ==	 DFLT_LABEL_TEXT


def main():
	import sys
	from PyQt5 import QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	backend_obj = Backend()
	backend_obj.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
