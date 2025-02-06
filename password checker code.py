import re

def check_password_strength(password):
    # Define the criteria for password strength
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    # Evaluate password strength
    if length_error or lowercase_error or uppercase_error or digit_error or special_char_error:
        print("Weak Password. Please ensure your password:")
        if length_error:
            print("- Is at least 8 characters long")
        if lowercase_error:
            print("- Has at least one lowercase letter")
        if uppercase_error:
            print("- Has at least one uppercase letter")
        if digit_error:
            print("- Contains at least one number")
        if special_char_error:
            print("- Contains at least one special character (!@#$%^&*)")
    else:
        print("Strong Password!")

# Get user input
password = input("Enter your password: ")
check_password_strength(password)
