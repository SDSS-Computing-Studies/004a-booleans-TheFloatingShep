#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"

x = input("Enter a sentence\n")
if "password" in x:
    print("the sentence contains password")
else:
    print("the sentence does not contain password")