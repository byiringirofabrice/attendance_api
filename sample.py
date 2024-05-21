def listFunction(a):

    numbers_input = input("Enter numbers separated by commas:\n")
    
    
    number_list = [int(x) for x in numbers_input.split(",")]

    total_sum = sum(number_list)
    odd_numbers =[]
    even_numbers =[]


    average = total_sum / len(number_list)
    
 
    print("Average of :",number_list,"=", average)
    
    for i in number_list:
        
        if i %2 == 0:
         even_numbers.append(i)
         total_even=sum(even_numbers)
        if i %2 !=0:
         odd_numbers.append(i)
         total_odd = sum(odd_numbers)
    if even_numbers:
       print("Even numbers from the list are:",even_numbers, "and there sum is:",total_even)
    if odd_numbers:
       print("Odd numbers from the list are:",odd_numbers, "and there sum is :",total_odd)
 


listFunction([])  
