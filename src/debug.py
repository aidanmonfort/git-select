from curses import initscr

class Debug:
    def __init__(self):
        self.win = None
        self.min_width, self.min_height = 100, 25
        self.height, self.width = None, None

    def run(self, width, height, window):
        if self.win != None or width > self.min_width and height > self.min_height:
            self.height = 2*(height//3)
            self.width = 2*(width//3)
            self.win = window.subwin(height - self.height, width - self.width)
        else:
            self.win = None
            self.height, self.width = None, None
        if self.win != None:
            self.win.addstr(0, 0, "hello!")
            self.win.refresh()
        
