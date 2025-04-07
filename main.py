import sys
from src.gui import GitSelectApp

def main():
    app = GitSelectApp()
    app.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())
        