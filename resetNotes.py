from os import remove, listdir

if __name__ == '__main__':
    if 'notesCount.txt' in listdir():
        remove('notesCount.txt')

    for x in listdir():
    	if 'Note-' in x:
    		remove(x)
