import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters to ensure a mix of character types.")


    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices from all sets
    all_chars = lower + upper + digits + punctuation
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting password list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
