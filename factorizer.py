#!/usr/bin/python3

test = input('Enter a number less than 121: ')
cast = int(test)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 84, 97, 101, 103, 107, 109, 113]

units = []

for prime in primes:
    if cast % prime == 0:
        for i in [1, 2, 3, 4, 5]:
            if cast % prime ** i > 0:
                cast /= prime ** (i - 1)
                #print(str(prime) + '**' + str(i - 1))
                units.append(str(prime) + '**' + str(i - 1))
                break

print(' * '.join(units))
