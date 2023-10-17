import random

def Fizz_Buzz():
    expected_answer = ""
    for i in range(1,101):
        #find expected answer
        if i%35 == 0:
            expected_answer = "BuzzWoof"
        elif i%21 == 0:
            expected_answer = "FizzWoof"
        elif i%15 == 0:
            expected_answer = "FizzBuzz"
        elif i%7 == 0:
            expected_answer = "Woof"
        elif i%5 == 0:
            expected_answer = "Buzz"
        elif i%3 == 0:
            expected_answer = "Fizz"
        else:
            expected_answer = str(i)
        if i%2 == 0:
            User_input = input("The game is a group game where the players take turn to count incrementally, replacing any number that is divisible by three with the word Fizz and any number that is divisible by five with the word Buzz and any number that is divisible by both three and five with the word FizzBuzz. If the number is divisible by seven then the number should be replaced by the word Woof. If the number is divisible by three and seven then the number should be replaced with FizzWoof. If the number is divisible by five and seven then the number should be replaced with BuzzWoof.")
            #See if User has entered right Answer
            if User_input != expected_answer:
                print("You have saldy lost")
                break 
        else:
            #See if Computer makes an mistake
            Computer_Error = random.randint(1,5)
            if Computer_Error == 5:
                if expected_answer == str(i):
                    random_output = random.randint(1,6)
                    if random_output == 1:
                        print("FizzBuzz")
                    if random_output == 2:
                        print("Fizz")
                    if random_output == 3:
                        print("Buzz")
                    if random_output == 4:
                        print("Woof")
                    if random_output == 5:
                        print("FizzWoof")
                    if random_output == 6:
                        print("BuzzWoof")
                else:
                    print(i)
                print("you win")
                break
            else:
                print(expected_answer)
Fizz_Buzz()