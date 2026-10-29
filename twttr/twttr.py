text = input("Input: ")
result = ""

for character in text:
    if character.lower() not in "aeiou":
        result += character

print("Output:", result)