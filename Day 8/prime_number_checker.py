
def prime_checker(number):
    if number == 0 or number == 1:
        print("This number is neither prime nor composite")
        return

    prime = True
    for integer in range(2, number):
        if number % integer == 0:
            prime = False
            break

    if prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")



n = int(input("Check this number: "))
prime_checker(number=n)
