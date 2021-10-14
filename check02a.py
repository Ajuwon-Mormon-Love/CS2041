def prompt_number():
    num1 = 0
    
    while num1 < 1:
        num1 = int(input("Enter a positive number: "))
        if num1 < 0:
            print ('Invalid entry. The number must be positive.')
            
    print('')
    return num1

number1 = prompt_number()
number2 = prompt_number()
number3 = prompt_number()

def compute_sum():
    total = number1 + number2 + number3
    print ('The sum is:', total)
    
compute_sum()