# Greeting Function
def greet(name):
    return f"Hello, {name}!"
print(greet("Devesh Kumar"))


# Addition : Write a function add(a, b) that returns the sum of two numbers.
def addition(a, b):
    return a + b
result = addition(7, 4)
print(result)


# Even or Odd : Write a function check_even_odd(n) that returns "Even" or "Odd".
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
number = int(input("Enter number to check even/odd : "))
result = check_even_odd(number)
print(f"The number {number} is {result}")


# Maximum of Three Numbers : Write a function maximum(a, b, c) that returns the largest of three numbers.
def maximun(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
result = maximun(3, 1, 2)
print(f"largest number is {result}")


# Prime Number : Write a function is_prime(n) that returns True if a number is prime, otherwise False.
def check_prime(number):
    for i in range(2, int(number ** (1 / 2) + 1)):
        if number % i == 0:
            return False
    else:
        return True
number = int(input("Enter number to check prime : "))
if number == 0 or number == 1:
    print("Invalid Input, try number greater/equal to 2")
elif number < 0:
    print("Invalid Input, please enter positive number")
else:
    is_prime = check_prime(number)
    if is_prime:
        print("number is prime")
    else:
        print("number is not prime")


# Print Primes : Write a function print_primes(start, end) that prints all prime numbers between start and end.
def print_primes(start, end):
    for i in range(start, end):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
start = int(input("Enter start point to print prime : "))
end = int(input("Enter end point to print prime : "))
if end <= start:
    print("Invalid Input, try end point greater than start point")
elif start < 2:
    print("Invalid Input, try start point greater/equal to 2")
else:
    print_primes(start, end)


# Count Vowels : Write a function count_vowels(text) that returns the number of vowels in a string.
def count_vowels(text):
    count = 0
    for char in str.lower(text):
        if char in "aeiou":
            count += 1
    print(f"the number of vowels in the text is : {count}")
text = "PROGRAMMING"
count_vowels(text)


# Sum of List : Write a function list_sum(numbers) that returns the sum of all elements without using Python's sum().
def list_sum(lst):
    sum = 0
    for element in lst:
        sum += element
    return sum
size = int(input("set size of the list : "))
lst = []
for i in range(size):
    element = int(input(f"Enter element {i+1} : "))
    lst.append(element)
result = list_sum(lst)
print(result)


# Remove Duplicates : Write a function remove_duplicates(numbers) that removes duplicate elements without using set().
def remove_duplicates(lst):
    duplicate = []
    for element in lst:
        if element not in duplicate:
            duplicate.append(element)
       
    return duplicate
size = int(input("set size of the list : "))
lst = []
for i in range(size):
    element = int(input(f"Enter element {i+1} : "))
    lst.append(element)
result = remove_duplicates(lst)
print(result)


