first_string = input()
second_string = input()
while len(second_string) != len(first_string):
    second_string = input()
crypt_string = input()
decrypt_string = input()

decrypt_crypt_string = ""
for crypt_symbol in crypt_string:
    counter = 0
    for first_symbol in first_string:
        if crypt_symbol == first_symbol:
            decrypt_crypt_string += str(second_string[counter])
        counter += 1
print(decrypt_crypt_string)

crypt_decrypt_string = ""
for decrypt_symbol in decrypt_string:
    counter = 0
    for first_symbol in second_string:
        if decrypt_symbol == first_symbol:
           crypt_decrypt_string += str(first_string[counter])
        counter += 1
print(crypt_decrypt_string)