def print_spiral(height, width):
    # print(height, width)
    number = 1
    max_number_length = len(str(height * width)) + 1
    list_ans = []

    for i in range(height):
        list_ans.append(" " * max_number_length * width)

    for lap in range(min(height, width)//2+1):
        for i in range(lap, width-lap):
            list_ans[0+lap] = list_ans[0+lap][:i*max_number_length] + str(number) + list_ans[0+lap][(((i)*max_number_length)+len(str(number))):]
            number += 1
        if number > height*width:
            break
        for i in range(1+lap, height-lap):
            list_ans[i] = list_ans[i][:(width-1-lap)*max_number_length] + str(number) + list_ans[i][(width-1-lap)*max_number_length+len(str(number)):]
            number += 1
        if number > height*width:
            break
        for i in reversed(range(lap, width-1-lap)):
            list_ans[height-1-lap] = list_ans[height-1-lap][:i*max_number_length] + str(number) + list_ans[height-1-lap][(((i)*max_number_length)+len(str(number))):]
            number += 1
        if number > height*width:
            break
        for i in reversed(range(1+lap, height-1-lap)):
            list_ans[i] = list_ans[i][:(0+lap)*max_number_length] + str(number) + list_ans[i][(0+lap)*max_number_length+len(str(number)):]
            number += 1
        if number > height*width:
            break

    for i in list_ans:
        print(i)

#
# print('Enter height')
# height = input()
# print ('Enter width')
# width = input()
#
# print_spiral(height, width);


print_spiral(9, 15)
print()
print_spiral(9, 6)
print()
print_spiral(6, 8)
print()
print_spiral(2, 3)