def sum_of_input(number1,number2):
    assert number1 < number2,"number1 should be bigger than number2"
    sum = 0
    for i in range(number1):
        sums=0
        for y in range(number2):
            sums = i+y
        sum+=sums
    return print(sum)

sum_of_input(4,5)

