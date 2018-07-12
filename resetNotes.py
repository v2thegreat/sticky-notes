from os import remove, listdir
import re

if __name__ == '__main__':
    if 'notesCount.txt' in listdir():
        print('notesCount.txt')

    for x in listdir():
    	if 'Note-' in x:
    		print(x)
