
"""

Sort out the downloads folder based on file type and extension, and places them into directories
on the desktop



"""

import os
import sys
import mimetypes
import filetype
import shutil


def check_types(mime_type: str):
    try:
        if mime_type == "image/jpeg":
            return "images"
        elif mime_type == "text/plain":
            return "text"
        elif mime_type == "application/pdf":
            return "pdfs"
        else: # returning none
            return None
    except ValueError:
        return

def main():
    download_path = os.path.expanduser('~/Downloads')
    desktop_path = os.path.expanduser('~/Desktop')

    if not os.path.exists(download_path) or not os.path.exists(desktop_path):
        print("Desktop or Downloads path does not exist")
        sys.exit(1)
    os.chdir(download_path)
    print("Now in downloads, collecting all files")

    items = os.listdir('.')

    if items:
        for item in items:
            mime_type = mimetypes.guess_type(item)
            directory = check_types(mime_type[0])

            if not directory: # returned None, mimetypes.guess_type can't determine
                print(f"Could not determine filetype of {item}, making a guess. Check after")
                directory = filetype.guess(item)
            
            print(directory)
            # check types 
            path = f"{desktop_path}/{directory}"
            if not os.path.exists(path):
                os.mkdir(path)
            # move file from Downloads to Desktop directory
            shutil.move(item, path)

            

    else:
        print("Nothing in downloads directory to sort")
        sys.exit()
    

    


if __name__=="__main__":
    main()