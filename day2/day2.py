with open("file.txt") as file:
    lines = file.readlines()

# Part 1
config = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

result = 0
for line in lines:
    possible = True
    id_pos = line.find(":")
    line_id = int(line[5:id_pos])

    for color in config.keys():
        for index, _ in enumerate(line):
            if line[index:index + len(color)] == color:
                if config[color] < int(line[index - 3:index]):
                    possible = False

    if possible:
        result += line_id

print(f"Solution 1 result: {result}")

# Part 2
result = 0
for line in lines:
    max_colors = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }

    for color in max_colors.keys():
        for index, _ in enumerate(line):
            if line[index:index + len(color)] == color:
                color_value = int(line[index - 3:index])
                if color_value > max_colors[color]:
                    max_colors.update({
                        color: color_value
                    })

    power = 1
    for color in max_colors.values():
        power = power * color

    result += power

print(f"Solution 2 result: {result}")
