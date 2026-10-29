import re

user_input = input("Expression: ")


x_str, y, z_str = re.findall(r"\d+|[+\-*/]", user_input)

x = float(x_str)
z = float(z_str)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z


print(f"{result:.1f}")