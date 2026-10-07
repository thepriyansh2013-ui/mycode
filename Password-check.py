def check_password():
    correct_password = "python123"
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Correct password. Access granted.")
    else:
        print("Incorrect password. Access denied.")


check_password()
