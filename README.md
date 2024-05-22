
Password Generator
Description
This Python script generates a secure random password with a mix of lowercase letters, uppercase letters, digits, and punctuation characters. The user specifies the desired length of the password, and the script ensures that the generated password contains at least one character from each character set to enhance security.

Features
Ensures password contains at least one lowercase letter, one uppercase letter, one digit, and one punctuation character.
Allows the user to specify the desired password length.
Provides error handling for invalid input (length less than 4).

Requirements
Python 3.x

Usage
Clone or download the script.
Run the script using a Python interpreter.
Follow the on-screen prompt to enter the desired password length.

Code Explanation
Imports:

random: Used for generating random characters.
string: Provides access to predefined character sets (lowercase, uppercase, digits, punctuation).
generate_password(length) Function:

Checks if the length is at least 4. Raises a ValueError if not.
Defines character sets for lowercase letters, uppercase letters, digits, and punctuation.
Ensures the password includes at least one character from each set.
Fills the rest of the password length with random characters from all sets combined.
Shuffles the characters to avoid predictable patterns.
Returns the generated password as a string.
main() Function:

Prompts the user to enter the desired password length.
Calls generate_password(length) to generate the password.
Prints the generated password.
Handles ValueError if the input length is invalid.

Error Handling
If the user inputs a length less than 4, the script will raise an error and display the following message:
Error: Password length should be at least 4 characters to ensure a mix of character types.

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

Author
Azad Saroha

Acknowledgments
Python documentation for providing comprehensive details on the random and string modules.
