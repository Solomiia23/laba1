text = input("Enter a string: ")
codeText = ""
i = 0
for number in text.split():
    if number.isdigit():
        number = str(int(number) + 1)
        input_number = text.split()
        input_number[1] = number
        text = ' '.join(input_number)
    i += 1

for letter in text:
    code = ord(letter)

    if 65 <= code <= 90:
        newpos = (code - 65 + 1) % 26 + 65
    elif 97 <= code <= 122:
        newpos = (code - 97 + 1) % 26 + 97
    elif 1072 <= code <= 1103:
        newpos = (code - 1072 + 1) % 32 + 1072
    elif 1040 <= code <= 1071:
        newpos = (code - 1071 + 1) % 32 + 1071

    else:
        newpos = code
    codeText += chr(newpos)
print(codeText)