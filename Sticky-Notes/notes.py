from UI import stickyNotesUI
from base_functions import base_functions
from threading_functions import threading_functions

class notes(threading_functions, stickyNotesUI, base_functions):
    """docstring for notes."""
    def __init__(self):
        super(notes, self).__init__()
