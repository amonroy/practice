### This is from r/dailyprogrammer and this is "[easy] challenge #1"
### create a program that will ask the users name, age, and reddit username
### have it tell them the information back, in the format:
### "your name is (blank), your are (blank) years old, and your username is (blank)"
### have the program log this information in a file to be accessed later.

#import sys

def user_info():
    """This function prompts users for their name, age, and username"""
    name = raw_input("Please eter your name:")
    age = raw_input("Please enter your age:")
    username = raw_input("Please enter you username:")
    print "You name  is %s, you are %s years old, and your username is %s" %(name, age, username)
    return name, age, username

def save_to_file(info1, info2, info3):
   with open("user_info_file.txt", 'w') as f:
       f. write("%s, %s, %s\n" %(info1, info2, info3))

user_name, user_age, user_username = user_info()

save_to_file(user_name, user_age, user_username)
