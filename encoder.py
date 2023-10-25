password = input()
result = ''
for digit in password:
    character = int(digit) + 3
    if character > 9:
        character = str(character)[1:]
    result += str(character)

print(result)