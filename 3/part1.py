import re

input = open("input.txt", "r").read()

pattern = r"mul\(([0-9]+),([0-9]+)\)"

print(sum(int(num1)*int(num2) for num1, num2 in re.findall(pattern, input)))
