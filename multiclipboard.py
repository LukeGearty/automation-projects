"""

High Level View: 

A command line function that stores things copied and pasted to a data structure that is going on.

"""

import clipboard
import time
import sys


def has_clipboard_changed(last) -> bool:
    
    time.sleep(0.2)
    current = clipboard.paste()
    if current == last:
        return False
    else:
        return True


def multiclipboard(limit=10):
    multiclipboard = {}
    key = 0
    
    while key < limit:
        current = clipboard.paste()
        if current not in multiclipboard.values():
            multiclipboard[key] = current
            key += 1
            print(multiclipboard)
        if not has_clipboard_changed(current):
            time.sleep(1)
    return multiclipboard


def retrieve_value(mc):
    for key, value in mc.items():
        print(f"{key} : {value}")
    
    print("Enter the key you want to retrieve: ")
    try:
        key_choice = int(input())
    except ValueError:
        print("Please enter an integer, exiting")
        return
    
    if key_choice not in mc.keys():
        print(f"{key_choice} not in clipboard, exiting")
        return
    else:
        # copy to clipboard
        clipboard.copy(mc[int(key_choice)])
        print(f"{key_choice} copied to your clipboard")
    return mc[key_choice]


def replace_value(mc):
    for key, value in mc.items():
        print(f"{key} : {value}")

    print("Enter the key for the value you want to replace: ")
    try:
        key_input = int(input())
    except ValueError:
        print("Please enter an integer, exiting")

    if key_input not in mc.keys():
        print(f"{key_input} not a key, exiting")
        return
    else:
        mc[int(key_input)] = clipboard.paste()
        print(f"{key_input}'s value copied to your clipboard")
        return mc[key_input]

    
def resize_clipboard(mc, old_size):
    if not isinstance(old_size, int):
        print("Please enter an integer")
        return mc, old_size
    print("Please enter a new size for the clipboard: ")
    try:
        new_size = int(input())
    except ValueError:
        print("Please enter an integer, exiting")
    
    
    if new_size == old_size:
        print("Don't be silly")
        return mc, old_size
    elif new_size < old_size:
        # clear out the last old_size - new_size elements, for example if old size = 4, new_size = 2, clear out last two elements
        k = old_size - new_size
        print(f"Clearing out the last {k} elements from the old multiclipboard")
        for _ in range(k):
            mc.popitem()
        return mc, new_size
    else:
        print("Adding new elements to clipboard")
        new_clipboard = multiclipboard(new_size)
        combined = mc | new_clipboard
        return combined, new_size



def main():
    if len(sys.argv) != 2:
        print("Usage: ./multiclipboard.py <size of multiclipboard")
        return
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Please enter a number")
        sys.exit(1)

    mc = multiclipboard(size)

    choices = ["Retrieve a Value", 
               "Replace a Value", 
               "Clear Clipboard",
               "Resize Clipboard",
               "Exit",]

    print("What would you like to do now?")


    while True:
        for i, choice in enumerate(choices):
            print(f"{i + 1}: {choice}")   
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a number")
        
        if choice == 1:
            retrieve_value(mc)
        elif choice == 2:
            replace_value(mc)
        elif choice == 3:
            mc.clear()
            mc = multiclipboard(size)
        elif choice == 4:
            mc, size = resize_clipboard(mc, size)
        else:
            break
    
    sys.exit(0)


if __name__=="__main__":
    main()