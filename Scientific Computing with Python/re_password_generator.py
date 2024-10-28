import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """#+
    Generate a random password with specified constraints.#+

    This function creates a password string of a given length, ensuring it contains#+
    at least the specified number of numeric, special, uppercase, and lowercase characters.#+
#+
    Args:#+
        length (int, optional): The total length of the password. Defaults to 16.#+
        nums (int, optional): Minimum number of numeric characters required. Defaults to 1.#+
        special_chars (int, optional): Minimum number of special characters required. Defaults to 1.#+
        uppercase (int, optional): Minimum number of uppercase letters required. Defaults to 1.#+
        lowercase (int, optional): Minimum number of lowercase letters required. Defaults to 1.#+
#+
    Returns:#+
        str: A randomly generated password string meeting all specified constraints.#+
    """#+
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password
    
if __name__=="__main__":
    new_password = generate_password()
    print('Generated password:', new_password)
