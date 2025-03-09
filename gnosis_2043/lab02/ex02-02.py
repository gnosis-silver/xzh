# logic (3 points)
# Username rules:
 # - Must be 5 - 10 characters long.
 # - Must only contain letters and numbers.
 # - Must contain at least 1 digit.
# 'R2D2',"CoderGirl","CoderGirl","This1IsTooLong","High5","pyth0n"
import string
username = 'pyth0n'
is_valid = False
has_digit = False
###### Your task: Add print statements as directed to help find ######
###### and fix the logic error. ######
if len(username) >= 5 and len(username) <= 10: # Check length.
    is_valid = True

for char in username: # Loop to check the characters in username.
    if char in string.digits: # Check for a digit (0-9).
        has_digit = True
    elif char not in string.ascii_letters: # Check for non-letters. In [ ]: In [ ]:
        is_valid = False

if is_valid and has_digit:
    print(f"'{username}' is a valid username.")
else:
    print((f"'{username}' is invalid."))
