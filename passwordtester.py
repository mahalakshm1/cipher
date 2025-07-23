import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Increase strength score based on criteria
    if not length_error:
        strength += 1
    if not digit_error:
        strength += 1
    if not uppercase_error:
        strength += 1
    if not lowercase_error:
        strength += 1
    if not symbol_error:
        strength += 1

    # Feedback
    if strength == 5:
        remarks = "Very Strong"
    elif strength >= 4:
        remarks = "Strong"
    elif strength >= 3:
        remarks = "Moderate"
    elif strength >= 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"

    return strength, remarks

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, remarks = check_password_strength(password)
    print(f"Password Strength: {strength}/5 -> {remarks}")
