votes = [
    "Пицца",
    " суши ",
    "ПИЦЦА",
    "бургер",
    "Суши",
    "",
    "  пицца  ",
    "   ",
    "БУРГЕР",
    "тако",
]

stock = dict()
for vote in votes:
    food = vote.strip().lower()

    if food == "":
        continue

    if food in stock:
        stock[food] += 1
    else:
        stock[food] = 1

print(f"Голосов: {sum(stock.values())}")

for product, quantity in stock.items():
    print(f"{product}: {quantity}")
