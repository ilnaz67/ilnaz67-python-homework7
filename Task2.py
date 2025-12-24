text = input()

result = ""

vowels = "aoyeuiAOEYUI"


for char in text:
    if char in vowels:
        continue
    
    result += "."
    
    result += char.lower()

print(result)