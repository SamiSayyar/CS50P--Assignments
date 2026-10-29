amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    
    # Use try/except or ensure the input is valid if needed, 
    # but standard int() works if a number is entered:
    coin = int(input("Insert Coin: "))
    
    # CS50 only accepts 25, 10, and 5 cent coins
    if coin in [25, 10, 5, 1]:
        amount_due -= coin

change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")