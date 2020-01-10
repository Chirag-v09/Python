import sys
import os

# To find the path of strings.py
path = os.path.abspath("Add_two_num.py")

# Add the path of the strings.py file in order to import that file
sys.path.append (path)

# Import strings.py file
import Add_two_num

# Calling the functions of string.py file
Add_two_num.addition(3, 2)
Add_two_num.addition2()
