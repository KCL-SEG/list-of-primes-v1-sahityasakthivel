"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    print("h")
    list = []

    if (number_of_primes >= 1):
        list.append(2)
    counter = 3
    while(len(list) !=  number_of_primes):
        prime = True
        for i in range(2,counter):
            if(counter % i == 0):
                prime = False
        if prime:
            list.append(counter)

        counter+= 1
    return list
