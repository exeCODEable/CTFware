"""
-------------
| CTF Ware |
------------
| CHMODER |
-----------
"""


import main
import Error_Handler
from time import sleep


# ---- Defining Functions ----

# The Title : CHMODER
def title():
    print(""""
 __         __  __  __ __  
/  |__||\/|/  \|  \|_ |__) 
\__|  ||  |\__/|__/|__| \  
----------------------------------------------------
| Helps you figure out the CHMOD permissions code. |
----------------------------------------------------
""")

    sleep(2)
    # Calling the menu options.
    chmod_menu()


# The CHMOD Options Function
def chmod_menu():
    print("\n-----------------------"
    "\nChoose The Permissions"
    "\n-----------------------"
    "\n1: Execute [--x ]"
    "\n2: Write [ -w- ]"
    "\n3: Execute & Write [ -wx ]"
    "\n4: Read [ r-- ]"
    "\n5: Read & Execute [ r-x ]"
    "\n6: Read & Write [ rw- ]"
    "\n7: Read, Write, & Execute [ rwx ]" "\n")


    # Permission for USER.
    u = input("What is your choice for USER: ")
    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    u = Error_Handler.the_checker(u)

    # Process based on the value assigned by The Checker.
    if u == -1:
        chmod_menu()
    elif u == -2:
        chmod_menu()
    elif int(u) > 7:
        print("No such option. \nTry Again")
        sleep(2)
        chmod_menu()
    else:
        pass

    
    # Permission for GROUP.
    g = input("What is your choice for GROUP: ")
    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    g = Error_Handler.the_checker(g)

    # Process based on the value assigned by The Checker.
    if g == -1:
        chmod_menu()
    elif g == -2:
        chmod_menu()
    elif int(g) > 7:
        print("No such option. \nTry Again")
        sleep(2)
        chmod_menu()
    else:
        pass



    # Permission for EVERYONE.
    e = input("What is your choice for EVERYONE: ")
    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    e = Error_Handler.the_checker(e)

    # Process based on the value assigned by The Checker.
    if e == -1:
        chmod_menu()
    elif e == -2:
        chmod_menu()
    elif int(e) > 7:
        print("No such option. \nTry Again")
        sleep(2)
        chmod_menu()
    else:
        pass


    
    # Concacting the code
    uicode = str(u)+str(g)+str(e)
    code = uicode
    vcode = (u, g, e)


    # Dispalying the numeric results
    print("\nThis is your numeric CHMOD code: "+ code)
    
    # Call the visual function
    visual(vcode)



# Creating the Visuals of the permissions chosen 
def visual(vcode):  
    print("This will be your file's permissions: ", end="")
    for x in vcode:
        if (x == '1'):
            print("--x", end="")
        elif (x == '2'):
            print("-w-", end="")
        elif (x == '3'):
            print("-wx", end="")
        elif (x == '4'):
            print("r--", end="")
        elif (x == '5'):
            print("r-x", end="")
        elif (x == '6'):
            print("rw-", end="")
        elif (x == '7'):
            print("rwx", end="")
        else:
            print("Invalid Option")
    
    # Call the again function
    internal_loop()


    
#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\n\nBack to the CHMODER? [y/n] : ")
    if loop_answer.lower()== 'y':
        chmod_menu()
    else:
        main.mini_menu()




# ----- End of Defining Functions ----

# The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    title() # Calling the title.



