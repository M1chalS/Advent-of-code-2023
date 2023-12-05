with open("file.txt") as file:
    lines = file.readlines()

# Part 1
result = 0
for line in lines:
    id_pos = line.find(":")
    line_id = int(line[4:id_pos])
    separator_pos = line.find("|")
    left_values = line[id_pos + 1:separator_pos].split(" ")
    right_values = line[separator_pos + 1:-1].split(" ")

    winning_values, values = list(), list()

    for value in left_values:
        if value.isdigit():
            winning_values.append(int(value))

    for value in right_values:
        if value.isdigit():
            values.append(int(value))

    power = 0
    for winning_value in winning_values:
        if winning_value in values:
            if power == 0:
                power = 1
            else:
                power *= 2

    result += power

print(f"Solution 1 result: {result}")

# Part 2
result = 0
cards = {}
for line in lines:
    id_pos = line.find(":")
    line_id = int(line[4:id_pos])
    separator_pos = line.find("|")
    left_values = line[id_pos + 1:separator_pos].split(" ")
    right_values = line[separator_pos + 1:-1].split(" ")

    winning_values, values = list(), list()

    for value in left_values:
        if value.isdigit():
            winning_values.append(int(value))

    for value in right_values:
        if value.isdigit():
            values.append(int(value))

    count = 0
    for winning_value in winning_values:
        if winning_value in values:
            count += 1

    num = cards.get(line_id)
    if num is None:
        cards.update({line_id: 1})
        num = 1
    elif num == 2:
        pass
    else:
        cards.update({line_id: num+1})
        num = cards.get(line_id)

    for j in range(num):
        for i in range(count):
            number = cards.get(line_id+i+1)
            if cards.get(line_id+i+1) is None:
                number = 0
            cards.update({line_id+i+1: number+1})

for card in cards.values():
    result += card

print(f"Solution 2 result: {result}")