# function to perform linear search on list 
def linear_search(arr, target):

# write code here to perform linear search
# loop 

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# target which we need to find in a list 
target = 9

# a list in which we need to find the target
arr = [2,8,7,10,11,14,9,20]
# call a function to perform linear search
Result = linear_search(arr, target)

print(Result)

# week 1 - 7 input temperature 
# 7 days of temperature input

# average temperature for the week

# monday = input("Enter temperature for Monday: ")
# tuesday = input("Enter temperature for Tuesday: ")
# wednesday = input("Enter temperature for Wednesday: ")  
# thursday = input("Enter temperature for Thursday: ")
# friday = input("Enter temperature for Friday: ")
# saturday = input("Enter temperature for Saturday: ")
# sunday = input("Enter temperature for Sunday: ")

# # calculate average temperature for the week
# average_temperature = (int(monday) + int(tuesday) + int(wednesday) + 
#                        int(thursday) + int(friday) + int(saturday) + 
#                        int(sunday)) / 7

# print(f"Average temperature for the week is: {average_temperature:.2f}°C")

sum = 0   # 2/5
for i in range(1, 8):
    temperature = input(f"Enter temperature for day {i}: ")
    sum += int(temperature)
average_temperature = sum / 7
print(f"Average temperature for the week is: {average_temperature:.2f}°C")

