from curses import initscr
from src.utils import get_git_files
from src.debug import Debug

class GitSelectApp:
    def __init__(self):
        self.win = initscr()
        self.files = get_git_files()
        self.selected_keys = []
        self.debug = Debug()
    def focus_next(self):
        pass

    def focus_previous(self):
        pass    

    def toggle_selection(self):
        pass

    def handle_input(self):
        self.win.nodelay(True)
        key = self.win.getch()
        if key != -1:
            self.selected_keys.append(key)
        
    def run(self):
        while True:
            self.handle_input()
            self.win.addstr(0, 0, "hello!")
            self.debug.run(self.win.getmaxyx()[1], self.win.getmaxyx()[0], self.win)
            self.win.refresh()

            
