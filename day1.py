with open("file.txt") as file:
    lines = file.readlines()

sum = 0
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for i in lines:
    tab = {}

    for number in numbers.keys():
        for index, _ in enumerate(i):
            if i[index:index + len(number)] == number:
                tab.update({index: numbers[number]})

    for index, x in enumerate(list(i)):
        if x.isdigit():
            tab.update({index: x})

    first = tab[min(tab)]
    last = tab[max(tab)]
    temp = first + last
    sum += int(temp)

print(sum)
