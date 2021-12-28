# --------------
# CTF WARE
# Coder: ryn0f1sh (Ash Noor)
# Site: www.exeCODEable.com
# --------------

# Main Imports
from time import sleep

# Local .py files needed.
# HLPR
import hlpr
# B64
import b64
# CHMODER
import chmoder
# DE1337ER
import deleeter
# Error Handling : The Checker
import Error_Handler

# ------------------------------------------------------------
# The Title Function : CTF Ware - Lite
def title():
    print("""\n
╔═╗╔╦╗╔═╗  ╦ ╦┌─┐┬─┐┌─┐
║   ║ ╠╣   ║║║├─┤├┬┘├┤ 
╚═╝ ╩ ╚    ╚╩╝┴ ┴┴└─└─┘ 
    """)
    sleep(2)


# ------------------------------------------------------------
# The Main Menu Function : All the options.
def main_menu():
    print("""
 _ _       _ _    
//\/\\ain  //\/\enu
====================
[1]: HLPR.......[A file of ready to use CTF Commands]
[2]: B64...........[A Base64 Encoder / Decoder]
[3]: CHMODER........[File Permission Codes Helper]
[4]: DE-1337-ER.............[L33t & Text Converter]
[5]: Exit Program.

    """"")
    sleep(1)

    #User Input : Choice of the menu.
    user_menu_selection = input("Enter Your Selection: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    user_menu_selection = Error_Handler.the_checker(user_menu_selection)

    # Process based on the value assigned by The Checker.
    if int(user_menu_selection) == 1:
        # HLPR goes here
        hlpr.title()
    elif int(user_menu_selection) == 2:
        # B64 goes here
        b64.title()
    elif int(user_menu_selection) == 3:
        # CHMODER goes here
        chmoder.title()
    elif int(user_menu_selection) == 4:
        # De-leeter goes here
        deleeter.title()
        # If User Input is rejected by the Error Handler
    elif user_menu_selection == -1:
        main_menu()
        # If User Input is rejected by the Error Handler
    elif user_menu_selection == -2:
        main_menu()
    else:
        # Outro function goes here
        outro()
# End of Main Menu Function
# ------------------------------------------------------------



# ------------------------------------------------------------
# CTFW Mini Menu.
# This will be called on from the other files
def mini_menu():
    mm_answer = input("""
 _ _       _ _    
//\/\ini  //\/\enu
==================
(1): Main Menu.
(2): Exit CTF Ware.
Please select one:  """)

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    mm_answer = Error_Handler.the_checker(mm_answer)

    # Process based on the value assigned by The Checker.
    if int(mm_answer) == 1:
        main_menu()
    # If User Input is rejected by the Error Handler
    elif mm_answer == -1:
        mini_menu()
    # If User Input is rejected by the Error Handler
    elif mm_answer == -2:
        mini_menu()
    else:
        outro()

# End of CTFW Mini Menu Function.
# ------------------------------------------------------------





# ------------------------------------------------------------
# The Run Again Function.
# This is called from the other files.
# Takes the user back to main menu again, or exits after it is completed.
def run_again():
    # Getting the Y/N answer.
    yn_answer = input("\n\nAnother Selection? y/n : " )
    if (yn_answer.lower() == 'y'):
       # -- Call the Main Menu
       main_menu()

    else:
        #-- Call the Outro function.
        outro()

# End of The Run Again Function.
# ------------------------------------------------------------







# ------------------------------------------------------------
# The Outro Function
def outro():

    print("\nThank you for using CTF Ware, please wait.")
    sleep(2)

    xca_signature = """
    __          _____          __   
   / /         / ____|         \ \  
  / /  __  __ | |        __ _   \ \ 
 < <   \ \/ / | |       / _` |   > >
  \ \   >  <  | |____  | (_| |  / / 
   \_\ /_/\_\  \_____|  \__,_| /_/  
    
         www.exeCODEable.com 
           Code The Planet
                
"""

    print(xca_signature)
    sleep(1)

    # -- Any Key to Exit --
    input("\n>->-> [ Please press ENTER key to Exit ] <-<-<")
    exit()
# End of Outro Function
# ------------------------------------------------------------







# -----------------
# CALLING FUNCTIONS
# Using a Main Guard to prevent it from running when Imported.
#------------------
if __name__ == '__main__':
    title() #-- The CTF Ware - Lite
    main_menu() #-- The Main Menu function.