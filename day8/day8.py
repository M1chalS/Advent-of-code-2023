with open("file.txt") as file:
    lines = file.readlines()

instructions = list(lines[0])
instructions.pop(-1)

values = {}
for index, line in enumerate(lines[2:]):
    value = line[:3]
    left_value = line[7:10]
    right_value = line[12:15]

    values.update({value: [left_value, right_value]})

# Part 1
result = 0
found = False
current_value = "AAA"
while not found:
    for index, instruction in enumerate(instructions):
        current = values.get(current_value)

        if instruction == "L":
            current_value = current[0]
        else:
            current_value = current[1]

        if current_value == "ZZZ":
            found = True

        result += 1

print(f"Solution 1 result: {result}")
