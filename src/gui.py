from curses import initscr

class GitSelectApp:
    def __init__(self):
        self.initscr()
        self.kb = KeyBindings()
        self.kb.add("j")(focus_next)
        self.kb.add("k")(focus_previous)
        self.kb.add("space")(toggle_selection)

    