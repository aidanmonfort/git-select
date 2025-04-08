import sys
from src.gui import GitSelectApp
from src.utils import get_git_files

def main():
    app = GitSelectApp()
    while True:
        try:
            app.run()
        except KeyboardInterrupt:
            break
    print("Exiting...")
    return 0

if __name__ == "__main__":
    sys.exit(main())
        