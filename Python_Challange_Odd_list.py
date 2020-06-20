N = int(input("Input the last number of the list "))
input_list = []
for value in range(0, N):
    input_list.append(value)

 
def odd(input_list):
    output_list = [] 

    for index in range(0, len(input_list)):
        if input_list[index] % 2 != 0:
        
          output_list.append(input_list[index])
    
    return output_list

print(input_list)
print(odd(input_list))