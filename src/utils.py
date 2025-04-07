import subprocess

def check_git_exists():
    version = None
    try:
        version = subprocess.check_output(["git", "--version"]).decode()[4:-1]
    except subprocess.CalledProcessError:
        pass
    return version