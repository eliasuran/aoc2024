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

def remove_one_and_check_is_safe(line):
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        if is_safe(new_line):
            return True

print(sum(1 for line in input if remove_one_and_check_is_safe(line.split())))
