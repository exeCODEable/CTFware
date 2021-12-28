"""
-------------
| CTF Ware |
------------
| De-L33t-er |
--------------
"""


import sys
import main
import Error_Handler
from time import sleep

# -- To convert text to l33t sp34k.
def e_l33t ():
    ui_word = input("What to l33t: ")
    lw = ui_word.lower()
    el33ted = lw.replace("e", "3").replace("a", "4").replace("t", "7").replace("s", "5").replace("g", "6").replace("o", "0").replace("i", "1")
    print(el33ted.title())
    internal_loop()


# -- to convert l33t back to standard text.
def d_leet ():
    ui_word = input("What to d-leet: ")
    lw = ui_word.lower()
    dleeted = lw.replace("3", "e").replace("4", "a").replace("7", "t").replace("5", "s").replace("6", "g").replace("0", "o").replace("1", "i")
    print(dleeted)
    internal_loop()


def title():
    print("""
 __  __        __  __  ___     __ __  
|  \|_  __  /|  _)  _)   / __ |_ |__) 
|__/|__      | __) __)  /     |__| \  
-------------------------------------------------------
| To convert text TO and FROM Leet Speak / 1337 sp34k |
-------------------------------------------------------""")
    sleep(2)
    # call the de-leet-er menu
    leeter_menu()



def leeter_menu():
    print("""
De-l33t-er Menu
---------------
[1]: E-1337.
[2]: D-Leet.
[3]: Main Menu.
[4]: Exit CTF Ware.
    """)
    menu_answer = input("What is your option?: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    menu_answer = Error_Handler.the_checker(menu_answer)

    # Process based on the value assigned by The Checker.
    if int(menu_answer) == 1:
        e_l33t()
    elif int(menu_answer) == 2:
        d_leet()
    elif int(menu_answer) == 3:
        main.main_menu()
    elif int(menu_answer) == -1:
        leeter_menu()
    elif int(menu_answer) == -2:
        leeter_menu()
    else:
        main.outro()



#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the De-L33t-er Menu? [y/n] : ")
    if loop_answer.lower()== 'y':
        leeter_menu()
    else:
        main.mini_menu()









#-- The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    title() # The Title De-l33t-er


