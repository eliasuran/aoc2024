with open("input.txt", "r") as txt_file:
    list_of_nums = txt_file.read().splitlines()

left_list = []
right_list = []
for i in range(len(list_of_nums)):
    line = list_of_nums[i].split(" ")
    left_list.append(line[0])
    right_list.append(line[3])

occurences = {}

for num in right_list:
    num = int(num)
    occurences[num] = occurences.get(num, 0) + 1

print(sum(int(num)*occurences.get(int(num), 0) for num in left_list))
