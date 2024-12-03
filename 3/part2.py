import re

input = open("input.txt", "r").read()

pattern = r"mul\(([0-9]+),([0-9]+)\)"

total = 0

current_status = "do()"

for match in re.finditer(pattern, input):
    split_input = input.split(match.group(0))
    
    funcs = re.findall(r"do\(\)|don't\(\)", split_input[0])
    if funcs:
        current_status = funcs[-1]

    if current_status == "do()":
        total += int(match.group(1))*int(match.group(2))

    input = split_input[1]

print(total)
