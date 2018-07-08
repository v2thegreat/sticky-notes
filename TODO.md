# TODO:

* Add reference to author of the eye design: [here](https://www.flaticon.com/authors/freepik)

* Add a feature that stops adding dates if there's a date already in the last line

	* Fix 1: Check the last few lines of the document to see if the datetime stamp is present
		* Fix 1.1: This can be checked with using RE

		* Fix 1.2: Consider checking the date only when the file has been saved/checked with the updateLabelTextForNewNote, possibly refactoring it to include more details

* Make all thread based text checking to be done by a single thread instead of running 30 threads and hence reducing thread switching and overhead

* Review documentation for all

<hr>
#### All new features beyond this point are not to be completed until the file has been uploaded to GitHub

* Refactor checksForPossibleTitle

* Add an option to change default settings

* Possibly use everything as a .pyx file and run with Cython?
	* If speed is needed, and only for the final releases
		* Only for final releases because it can take a while for the UI.py to compile after each change

		Also, use a setup module for compiling for the releases as otherwise the compiled Cython code might reside in the memory
			*Lookup if it actually stays in the memory*

	* Also, compiling it is going to take a long time for the first time the program is run

<hr>
## Done:

* Add unit tests
	* Decided not to include unit tests


* Refactor to break down Backend into smaller classes
	* Broke down the Backend Classes into the following classes:
		* base_functions: This class contains the functions that're generally static methods
		* markdown_functions: This class contains the functions that are needed for the markdown functionality
		* threading_functions: This class contains the functions that control the threads

	The Backend class can be broken down further as well, but it'll take more effort and require more creativity as they are pretty intertwined 


* Add a mode where you can view the compiled markdown file instead of the markdown file itself

* Add a way to add a time stamp each time the file is modified --> Fix 1 was used

	* Fix 1: This can be done with using os.stats[8], which returns *time of most recent content modification*
		* This means that this can be used to check the time of the change

	* Fix 2: This can also be done by calculating a checksum (such as hashing the entire file) and constantly checking with that


* Fix issue where when all of the labels are hidden, newer labels are set in the middle
--> Fix 2 was used as it was the simpler solution, and all proper formatting was applied.
	* Cause:
		This might've been caused from using the horizontal and vertical layouts

	* Possible Fix 1: Enable the height of the labels to be dynamic, so that with each new label added the height increases
		This means that we'll have to add functionality to cover up this bug

		Look up how to check/be notified when the size of the main dialog is changed, and to what

		* If can't find the check for the change in size, setup another thread for changing the position of the button every 0.1 - 0.5 seconds, and ensure the button is still clickable

	* Possible Fix 2: Remove the all layout mechanisms manually from the UI
		* This means that we'll have to change everything from the designer application and refactor everything again
