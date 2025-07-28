import secrets
import string

def generate_password(length=10):
    if length < 10:
        raise ValueError("Password length must be at least 10.")

    # Ensure at least one character from each category
    lower = secrets.choice(string.ascii_lowercase)
    upper = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    # Fill the rest of the password length
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [secrets.choice(all_chars) for _ in range(length - 4)]

    # Combine and shuffle
    password_list = [lower, upper, digit, special] + remaining
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)

if __name__ == "__main__":
    print(generate_password(12))  # Example usage

