#Python Program to find whether a number is prime or not
num = int(input('Enter the number: '))
for i in range(2, num):
    if num % i == 0:
        print('It is not a prime number')
        break
    else:
        print('It is a prime number')
        break
