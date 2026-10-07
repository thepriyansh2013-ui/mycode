# Pseudocode:
# START
# Ask the user for their age
# IF age is 18 or older
#     Display that the user can vote
# ELSE
#     Display that the user cannot vote yet
# END

def voting_check():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")


voting_check()
