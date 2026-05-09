def check_password(password):

    score = 0
    missing = []

    # Rule 1: Length check
    if len(password) >= 8:
        score += 1
    else:
        missing.append("Too short (min 8 characters)")

    # Rule 2: Uppercase
    if any(c.isupper() for c in password):
        score += 1
    else:
        missing.append("Missing uppercase letter")

    # Rule 3: Lowercase
    if any(c.islower() for c in password):
        score += 1
    else:
        missing.append("Missing lowercase letter")

    # Rule 4: Digit
    if any(c.isdigit() for c in password):
        score += 1
    else:
        missing.append("Missing digit")

    # Rule 5: Special character
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        missing.append("Missing special character (!@#$%^&*)")

    # Strength label
    if score <= 1:
        label = "Weak (your password is basically 'password123')"
    elif score <= 3:
        label = "Medium (getting there...)"
    else:
        label = "Strong (even hackers would cry)"

    return score, label, missing


# Testing with different passwords
passwords = ["abc", "password123", "MyPass1", "MyP@ss1", "Str0ng@Pass"]

for p in passwords:
    score, label, missing = check_password(p)
    print("\nPassword:", p)
    print("Score:", score)
    print("Strength:", label)
    print("Missing:", missing)