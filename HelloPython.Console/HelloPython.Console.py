import fibo
while True:
    print("Please enter an integer greater than one")
    user_input = input()
    try: 
        int_user_input = int(user_input)
        if int_user_input > 1:
            print(fibo.fib2(int_user_input))
        else:
            print("Sorry, I can only work with integers greater than one")
    except ValueError:
        print("Sorry, I didn't understand that.")