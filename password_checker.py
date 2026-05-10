import re

def check_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("❌ Too short — use at least 8 characters")
    elif len(password) >= 12:
        score += 2
        feedback.append("✅ Good length")
    else:
        score += 1
        feedback.append("⚠️ Acceptable length — try 12+ characters")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Has uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Has lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters")

    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✅ Has numbers")
    else:
        feedback.append("❌ Add numbers")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Add special characters (!@#$%)")

    # Check common passwords
    common = ["password", "123456", "qwerty", "abc123", "password123"]
    if password.lower() in common:
        feedback.append("❌ This is a very common password — change it!")
        score = 0

    # Rating
    if score == 0:
        rating = "💀 VERY WEAK"
    elif score <= 2:
        rating = "🔴 WEAK"
    elif score <= 4:
        rating = "🟡 MODERATE"
    elif score <= 6:
        rating = "🟢 STRONG"
    else:
        rating = "💪 VERY STRONG"

    print("\n--- Password Strength Checker ---")
    print(f"Password: {password}")
    print(f"Score: {score}/7")
    print(f"Rating: {rating}")
    print("\nFeedback:")
    for item in feedback:
        print(item)

# Run
password = input("\nEnter a password to check: ")
check_password(password)
