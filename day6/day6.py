with open("file.txt") as file:
    lines = file.readlines()

# Part 1
times = map(int, lines[0].split(":")[1].split())
distance = map(int, lines[1].split(":")[1].split())

result = 1
for time, distance in list(zip(times, distance)):
    count = 0

    for time_holding in range(time + 1):
        time_left = time - time_holding
        distance_traveled = time_holding * time_left
        if distance_traveled > distance:
            count += 1

    result *= count

print(f"Solution 1 result: {result}")

# Part 2
times = lines[0].split(":")[1].split()
distance = lines[1].split(":")[1].split()

result = 0
tab = ["", ""]
for time in times:
    tab[0] = tab[0] + time

for dist in distance:
    tab[1] = tab[1] + dist

time, distance = [int(tab[0]), int(tab[1])]

for time_holding in range(time + 1):
    time_left = time - time_holding
    distance_traveled = time_holding * time_left
    if distance_traveled > distance:
        result += 1

print(f"Solution 2 result: {result}")
