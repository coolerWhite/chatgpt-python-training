from pathlib import Path

path = Path(__file__).with_name("expenses.txt")

categories = dict()
category = ""

with path.open(encoding="utf-8") as file:
    for line in file:
        new_line = line.strip().lower()
        if new_line == "":
            continue
        else:
            type, price = new_line.split(";")
            price = int(price)
            type = type.strip()

        if type in categories:
            categories[type] += price
        else:
            categories[type] = price

print(f"Общая сумма: {sum(categories.values())}")

for item, cost in categories.items():
    print(f"{item} : {cost} руб.")