import fibo
import os
import multiprocessing
import requests
print("Hello, and welcome to " + os.name + " on this computer with " + str(multiprocessing.cpu_count()) + " processor cores/threads")
while True:
    print("Please enter an integer greater than one and the computer will attempt to give the sum of all numbers in the fibonacci sequence up to that number.")
    user_input = input()
    try:
        int_user_input = int(user_input)
        if int_user_input > 1:
            print(fibo.fibsum(int_user_input))
        else:
            print("Sorry, I can only work with integers greater than one")
    except ValueError:
        if (user_input == "exit"):
            quit()
        else:
            print("Sorry, I didn't understand that.")
