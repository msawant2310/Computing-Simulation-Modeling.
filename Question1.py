#Q.1
def addition_numbers(list, num): 
    a=0
    b=0
    for i,number in enumerate(list):
        a=number
        b=num-a
        if b in list[i+1:]:
            return a,b

numbers = [2, 7, 11, 4]
print(addition_numbers(numbers, 13))