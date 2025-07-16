def create_third_list(list1, list2):
    result = [list1[i] for i in range(1, len(list1), 2)]
    result += [list2[i] for i in range(0, len(list2), 2)]
    return result

list1_input = input("Enter the first list of numbers separated by spaces: ")
list1 = list(map(int, list1_input.split()))

list2_input = input("Enter the second list of numbers separated by spaces: ")
list2 = list(map(int, list2_input.split()))

third_list = create_third_list(list1, list2)
print("Third list:", third_list)
