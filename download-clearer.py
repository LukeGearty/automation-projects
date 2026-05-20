import os
import sys
from pathlib import Path
import shutil


"""
Clear out the downloads folder - Unix
"""


def main():
    if os.name != "posix":
        print("Only works on Linux")
        sys.exit()
    
    # change directory to Downloads folder
    path = os.path.expanduser('~/Downloads')
    os.chdir(path)
    print("Changed directory to: ", os.getcwd())

    # get all items in the current directory

    items = os.listdir('.')
    
    # if there are items
    if items:
        try:
            for item in items:
                path = Path(f'./{item}')
                print(f"Current path: {path}")
                if path.is_file():
                    os.remove(path)
                elif path.is_dir():
                    shutil.rmtree(path)
        except FileNotFoundError:
            pass
            
    else:
        print("Nothing in downloads to delete")
    
    sys.exit()


if __name__=="__main__":
    main()