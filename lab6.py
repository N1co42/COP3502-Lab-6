#Nicolas Broderick

def encode():
    return_string = ''
    info = input('Please enter your password to encode: ')
    for i in info:
        j = int(i) + 3
        return_string += str(j)
    return return_string

#Aisha Yacoob
def decode(encoded_password):
    return_string = ''
    for i in encoded_password:
        j = int(i) - 3
        return_string += str(j)
    return return_string

def main(): 
    choice = 3.14159
    encoded_pword = ""

    while choice != 3:
        print('\nMenu')
        print('-------------')
        print('''1. Encode
2. Decode
3. Quit''')
        choice = int(input('\nPlease enter an option: '))

        if choice == 1:
            encoded_pword = encode()
            print('Your password has been encoded and stored!')
        elif choice == 2:
            if encoded_pword:
                original_pword = decode(encoded_pword)
                print(f'The encoded password is {encoded_pword}, and the original password is {original_pword}.')
            else:
                print("No password has been encoded yet.")
        elif choice == 3:
            break

if __name__ == '__main__':
    main()
