#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

x = input("Enter username\n")
if x == "admin":
    y = input("Enter password\n")
    if y == "12345password":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("invalid user")