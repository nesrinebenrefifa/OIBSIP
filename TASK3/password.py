import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char= ''
    if use_letters:
        char += string.ascii_letters
    if use_numbers:
        char += string.digits
    if use_symbols:
        char += string.punctuation
    
    if not char:
        print("Error: No character set selected.")
        return None
    
    password = ''.join(random.choice(char) for _ in range(length))
    return password

def main():
    print(" the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (yes/no): ").lower() == 'y'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'y'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Your generated password:", password)

if __name__ == "__main__":
    main()
