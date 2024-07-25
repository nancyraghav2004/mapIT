#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip # sys is fpr reading potentioa; command line arguments
if len(sys.argv) > 1:   #sys.argv stores a list of program's filename and command line arguments
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else :
    # Get address from command line.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
