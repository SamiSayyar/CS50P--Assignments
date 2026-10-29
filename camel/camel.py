camel_case = input("camelCase: ")
snake_case = ""

for character in camel_case:
    if character.isupper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character

print("snake_case:", snake_case)