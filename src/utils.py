import subprocess

def check_git_exists():
    version = None
    try:
        version = subprocess.check_output(["git", "--version"]).decode()[4:-1]
    except subprocess.CalledProcessError:
        pass
    return version

def get_git_files():
    # Gets files that are changed/should be committed, in an easy to parse format
    return subprocess.check_output(["git", "status", "--porcelain"]).decode().splitlines()