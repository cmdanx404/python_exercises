def isMonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing

#  Input from user
user_input = input("Enter numbers separated by spaces and/or commas: ")

#  Clean the input: replace commas with spaces, split, and convert to integers
nums = list(map(int, user_input.replace(',', ' ').split()))

#  Call the function
result = isMonotonic(nums)

#  Print the result
print("Is the array monotonic?", result)
