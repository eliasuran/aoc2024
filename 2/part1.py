input = open("input.txt", "r").readlines()

def is_safe(line):
    type = None

    if len(set(line)) != len(line):
        return False

    for i in range(len(line)):
        num = int(line[i])
        if i != len(line) - 1:
            if num > int(line[i+1]):
                if type == "increasing":
                    return False
                type = "decreasing"
            else:
                if type == "decreasing":
                    return False
                type = "increasing"

            if abs(num - int(line[i+1])) > 3:
                return False
    return True


print(sum(is_safe(line.split()) for line in input))
