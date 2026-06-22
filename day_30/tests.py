# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key':'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"Wrong key {error_message} - does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('Height is greater than 3')

bmi = weight / height ** 2
print(bmi)
