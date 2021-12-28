"""
Error Handler : The Checker
This function is to validate the user's input.
The programs only accepts positive integers.
"The Checker" checks the input sent to it and returns one of three values:
1. Returns back the same value sent (if the input is a positive integer).
2. Returns '-1' (if the input is a negative number).
3. Returns '-2' (if the input is a non-number, i.e. a letter or special character)
Based on the returned value, the function that requested the checker then acts accordingly.
"""
# Imports
from time import sleep
# ///// Beginning of The Checker Function.

def the_checker(check_me_please):
    # Using Try & Except for ValueError Handling
    try:
        # If the input is correct.
        if int(check_me_please) > 0:
            # Return the positive value that was sent.
            return check_me_please
        # If the entry is a negative number.
        elif int(check_me_please) < 0:
            print("No negative numbers allowed. \nTry Again.")
            sleep(2)
            return -1
        # If the entry is a negative Zer0.
        elif int(check_me_please) == -0:
            print("No negative numbers allowed. \nTry Again.")
            sleep(2)
            return -1
        else:
            return check_me_please

    except ValueError:
        print("This is not an Integer. \nTry Again.")
        sleep(2)
        return -2

# ///// End of The Checker Function.


