"""
Program which will test if the given number is a prime number or not.
Using the Miller-Rabin Algorithm as to ascertain primality.

Author: Nicola Mahon C15755031

"""

# import libs
from random import *


# check user input is positive odd number > 1
def input_number(message):
    # continue until a valid value is entered
    while True:
        try:
            # ask user for a value
            user_input = int(input(message))

            # if value is less than 2
            if user_input < 2:
                # raise an error
                raise ValueError
			# if the value is even and not 2
            elif user_input > 2 and user_input % 2 == 0:
				# raise an error
                raise ValueError
			# special case - 2 is even but also Prime
            elif user_input == 2:
				# return as a valid value
                return user_input
            else:
                # return the valid value
                return user_input
        except ValueError:
            # print error message to user
            print("\n** ERROR: Not a valid number! Try again.\n")
            continue


# is_prime()
def is_prime(n, k, q):

    # 2 is Prime but also even so return straight away
    if n == 2:
        return True

    # get random number < n-1
    a = randint(1, n-1)

    # for k iterations
    for i in range(0, k):
        temp_a = a % (n-1) + 1
        temp_q = int(q)

        # calculate a^q (mod n)
        mod = power_mod(temp_a, temp_q, n)

        while temp_q != n-1 and mod != 1 and mod != n-1:
            # calculate a^2^^j*q (mod n)
            mod = multiply_mod(mod, mod, n)
            temp_q *= 2

        # check if a^2^^j*q (mod n) = n-1
        if mod != n - 1 and temp_q % 2 == 0:
            # if mod != n - 1:
            return False

    return True


# calculate (a ^ b) % c
def power_mod(a, b, c):
    result = 1
    for i in range(0, b):
        result *= a
        result %= c
    return result % c


# calculate (a * b) % c
def multiply_mod(a, b, c):
    return (a * b) % c


# Main()
def main():

    # initialise value for number of divisions of n-1
    k = 0

    # get input from user, check input meets requirements
    # i.e. positive odd number > 1
    n = input_number("\nEnter a positive odd number greater than 1: ")

    # initialise value n-1 for dividing by 2
    q = n-1

    # while q is an even number
    while q % 2 == 0:
        # divide it by 2
        q = q/2
        # increment the number of divisions
        k += 1

    # print values for testing
    print("q: " + str(int(q)) + " k: " + str(k) + " n: " + str(n))

    # perform check for primality
    prime = is_prime(n, k, q)

    # check the result and print whether Prime or Composite
    if prime:
        print(str(n) + " is Prime")
    else:
        print(str(n) + " is Composite")


# call main()
if __name__ == "__main__":

    # keep program running until terminated
    while True:
        main()
