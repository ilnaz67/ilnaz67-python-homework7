text = input()

result = ""

for char in text:
    if char != 'w' and char != 'z':
        result += char

print(result)