with open("input.txt", "r") as txt_file:
    list_of_nums = txt_file.read().splitlines()

left_list = []
right_list = []
for i in range(len(list_of_nums)):
    line = list_of_nums[i].split(" ")
    left_list.append(line[0])
    right_list.append(line[3])

similarity_score = 0

for i in range(len(left_list)):
    left_num = int(left_list[i])
    occurences = 0
    for j in range(len(right_list)):
        right_num = int(right_list[j])
        if left_num == right_num:
            occurences += 1

    similarity_score += (left_num * occurences)

print(similarity_score)
