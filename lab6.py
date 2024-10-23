#Nicolas Broderick


def encode():
	return_string = ''
	info = input('Please enter your password to decode: ')
	for i in info:
		j = int(i) + 3
		return_string += str(j)
	return return_string

def main():
	choice = 3.14159

	while choice != 3:
		print('\nMenu')
		print('-------------')
		print('''1. Encode
2. Decode
3. Quit''')
		choice = int(input('\nPlease enter an option: '))

		if choice == 1:
			pword = encode()
			print('Your password has been encoded and stored!')
		elif choice == 2:
			pass
		elif choice == 3:
			break

if __name__ == '__main__':
	main()
