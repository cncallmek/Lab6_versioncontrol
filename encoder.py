def encoder(password):
    result = ''
    for digit in password:
        character = int(digit) + 3
        if character > 9:
            character = str(character)[1:]
        result += str(character)
    return result


def decoder(password):
    result = ''
    for digit in password:
        character = int(digit) - 3
        if character > 0:
            character += 10
        result += character
    return result


if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        user_input = input('\nPlease enter an option: ')
        if user_input == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif user_input == '2':
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {decoded_password}, and the original password is {encoded_password}")
        elif user_input == '3':
            exit()
