# Write a function in python which accept a number from user to return True, if the number
# is a prime number else return False. Use this function to print all prime numbers from 1
# to 100.


# Prime Number counter
prime_number = 0

# Function to check if a number is prime


def is_primenumber(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False

    else:
        return False
    return True


# Taking input of a number from the user to check if the number is prime

if_prime = int(
    input(
        "Enter a number to check: "
    )
)

print(is_primenumber(if_prime))

# Execution of the function for multiple numbers
for i in range(
        int(
            input("How many number to check:") + 1
        )):

    if is_primenumber(i):
        prime_number += 1
        print(i)

print("We found" + str(prime_number) + "prime numbers.")
