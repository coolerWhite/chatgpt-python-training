from pathlib import Path

path = Path(__file__).with_name("expenses.txt")

categoryes = dict()
error_types = 0

def parse_expense(line):
    parts = line.split(";")

    if len(parts) != 2:
        return None
    categoty, amount = parts

    categoty = categoty.strip().lower()

    try:
        amount = int(amount)
    except ValueError:
        return None

    if categoty == "" or amount < 0:
        return None
    
    return categoty, amount

with path.open(encoding="utf-8") as file:
    for line in file:
        result = parse_expense(line)

        if not line.strip():
            continue

        if result is None:
            error_types += 1
            continue

        categoty, amount = result

        if categoty in categoryes:
            categoryes[categoty] += amount
        else:
            categoryes[categoty] = amount

print(f"Всего потрачено: {sum(categoryes.values())}")
for item, cost in categoryes.items():
    print(f"{item} : {cost} руб.")
print(f"Ошибочных записей: {error_types}")