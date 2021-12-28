"""
-------------
| CTF Ware |
------------
| B64  |
--------
"""

import base64
import main
import Error_Handler
from time import sleep




#-- To ENCODE what is typed into Standard Base64
def nkoder():
    awords = input("Enter your sentence: ")
    awords_bytes = awords.encode('ascii')
    theEncoded = base64.standard_b64encode(awords_bytes)
    print(theEncoded.decode("utf-8"))
    internal_loop()


#-- To DECODE what is typed into standard English
def dkoder():
    bwords = input("Paste your Base64: ")
    theDecoded = base64.standard_b64decode(bwords)
    print(theDecoded.decode("utf-8"))
    internal_loop()




#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the B64's Menu? [y/n] : ")
    if loop_answer.lower()== 'y':
        b64_menu()
    else:
        main.mini_menu()



# The Title B64
def title():
    print("""
 __   __       
|__) /__  |__| 
|__) \__)    | 
-----------------------------------------------
| To help you Encode / Decode standard Base64 |
-----------------------------------------------""")
    sleep(2)
    # Call the menu
    b64_menu()



# -- The B64 Menu
def b64_menu():
    print("""
Base64 Menu:
------------
[1] : Encode.
[2] : Decode.
[3] : Main Menu.
[4] : Exit CTF Ware.
    """)
    menu_answer = input("What is your option?: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    menu_answer = Error_Handler.the_checker(menu_answer)

    # Process based on the value assigned by The Checker.
    if int(menu_answer) == 1:
        nkoder()
    elif int(menu_answer) == 2:
        dkoder()
    elif int(menu_answer) == 3:
        main.main_menu()
    elif int(menu_answer) == -1:
        b64_menu()
    elif int(menu_answer) == -2:
        b64_menu()
    else:
        main.outro()



'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    title() # The Title B64

