list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_number = 0
for i in range(len(list_numbers)):
    max_num = list_numbers[max_number]
    number_now_ = list_numbers[i]
    if number_now_ > max_num:
        max_number = i

list_numbers[max_number], list_numbers[-1] = list_numbers[-1], list_numbers[max_number]
print(list_numbers)
