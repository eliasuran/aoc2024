with open("input.txt", "r") as txt_file:
    list_of_nums = txt_file.read().splitlines()

total = 0

left_list = []
right_list = []
for i in range(len(list_of_nums)):
    line = list_of_nums[i].split(" ")
    left_list.append(line[0])
    right_list.append(line[3])

left_list.sort()
right_list.sort()

for i in range (len(left_list)):
    diff = int(left_list[i]) - int(right_list[i])
    if diff < 0:
        diff = diff * -1
    total += diff

print(total)
