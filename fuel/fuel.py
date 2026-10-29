while True:
    try:
        fraction = input("Enter a fraction : ")
        x, y = map(int, fraction.split("/"))
        if x > y:
            continue
        break
    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please enter a valid fraction.")
        continue
    percentage = round((x / y) * 100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

     