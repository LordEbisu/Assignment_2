input_string = input("Enter a list element separated by space ")
lst  = input_string.split() #Add value in a list
print(f"Element of input list {lst}")
list_assort = sorted(lst, key = float)
print(f"Sorted values {list_assort}")
if list_assort == lst:
    print("The input is sorted asending order")
else :
    print("It is not assorted")    