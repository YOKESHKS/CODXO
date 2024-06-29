import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special else ''

    # Create the initial character set
    char_set = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_digits:
        password.append(random.choice(digit_chars))
    if use_special:
        password.append(random.choice(special_chars))
    password.append(random.choice(lowercase_chars))

    # Fill the rest of the password length
    for _ in range(length - len(password)):
        password.append(random.choice(char_set))

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_special=use_special
    )

    print(f"Generated password: {password}")
