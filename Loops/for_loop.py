import statistics
for i in range(10,0,-3):
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
        
        
# Example 2
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(len(float_list))
for i in range(0, len(float_list),2):
    print(f"Element at index {i} is float: {float_list[i]}")
    
# Example 3
# string_list = ["Hello", "World", "Educative", "Learning", "Platform"]
# print(len(string_list))
# for str in string_list:
#     print(str)
    
# Example 4
test_string = "Educative"
for char in range(0, len(test_string),1):
    print(test_string[char])
    
# Example 5
test_string = "Hello World"
for char in test_string:
    print(char)
    
# Example 6 
def calculate_average(numbers):
    # Write your code here
    list_sum = 0
    for number in numbers:
      list_sum = list_sum + number
      average = list_sum/len(numbers)
    return average

# Test your function with different lists
numbers_list = [10, 20, 30, 40, 50]
print(f"The average of {numbers_list} is {calculate_average(numbers_list)}")

#Example 7 - Median of a list

def median_score(scores):
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    if n%2 == 1:
        median = sorted_scores[n//2]
    else:
        middle1 = sorted_scores[n//2]
        middle2 = sorted_scores[n//2 - 1]
        median = (middle1 + middle2)/2
    return median
    
# Test your function with different lists
score_list = [10, 20, 30, 40, 50, 60]
print(f"The median of {score_list} is {median_score(score_list)}")

#Example 7 - Median of a list using Statistics module

def median1_score(scores1):
    return statistics.median(scores1)

score_list1 = [1, 2, 3, 3, 5, 6]
print(f"The median of {score_list1} is {median_score(score_list1)}")

# Example 8 - Nested for loops
n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:
        if n1 + n2 == n:
            print(f"({n1}, {n2})")
            
# Example 9 - Continue
n = list(range(0,10))
for num in  n:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)
    
# Example 10 - Pass
n = list(range(0,20))
for num in n:
    pass
print(len(n))

# Example 11
def multiplication_table(n):
  # Write you code here
  for i in range(1,n):
    for j in range(1, n+1):
        print(f"{i} x {j} = {i*j}", end = "\n")

multiplication_table(5)

# Example 12 - While Loop
n = 1
while n <= 5:
    print(n)
    n += 1
    
# Example 13
n = 9015
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
    
# Example 14
for i in range(1, 6, 2):
    j = 0
    while j < i:
        print(i, end="")
        j = j + 1
    print()
    
# Example 15 - Write a program using a while loop that takes a number as input and calculates the sum of its digits.
def sum_of_digits(n):
 # Write your code here
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n // 10
    return sum
# Test the function
print(sum_of_digits(9015))

# Example 16 - Factorial 
def factor(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n -1
    return fact
print(factor(4))

# Example 17 - Factorial using recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(4)
print(result)

# Example 18 - Fibonacci Series
def generate_fibonacci(n):
    if n <= 0:
        return []
    
    #Handle the base case
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    #Initialize the sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    
    #Generate the Fibonacci sequence using a for loop
    for i in range(2, n):
        next_element = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_element)
    return fibonacci_sequence

# Test the function
n = 6
fibonacci_sequence = generate_fibonacci(n)
print(fibonacci_sequence)

# Convert to Binary
# def mystery(num):
#     binary_equivalent = []
#     if num <= 0: 
#         return 0
#     else:
#         remainder = (num % 2)
#         binary_equivalent.append(remainder)
#         mystery(num // 2)
#     # return binary_equivalent

# print(mystery(6))

def mystery(num):
    # Base case: if the number is 0 or less, return an empty list
    if num <= 0: 
        return []
    else:
        # Recursive call
        binary_equivalent = mystery(num // 2)
        # Append the remainder to the result of the recursive call
        binary_equivalent.append(num % 2)
        return binary_equivalent

# Convert the result to a string for proper binary representation
binary_result = ''.join(map(str, mystery(6)))
print(binary_result)

def collatz_sequence(n):
    n_list = []
    while n > 0:
        print(n)
        if n ==1:
            break
        elif n %2 == 0:
            n = n // 2
        else:
            n = n*3 + 1
        n_list.append(n)
    return n_list

#Test the function with different values of n
result = collatz_sequence(10)
print(result)

# Balance Square Brackets
def balance_brackets(s):
    balance = 0
    
    for char in s:
        if char == "[":
            balance += 1
            print(balance)
        elif char == "]":
            balance -= 1
            print(balance)
        if balance < 0:
            break
    return balance == 0

# Test the function
s = "[[[[][]]]]"
print(balance_brackets(s))

# Check sum for numbers in a list return True if the sum of any two numbers in the list is equal to 0 else False
def check_sum_zero(num_list):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == 0:
                return True
    return False

# Test the function
num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum_zero(num_list))

#Assesment -1 
a=5
b=10
a=a^b 
b=a^b 
a=a^b 
print(a,b)

print(bool())
print(bool('True'))

if (1 < 0) and (0 < -1):
  print("Pass")
elif (1 > 0) or False:
  print("Fail")
else:
  print("Educative")
  
def factorial(n): 
  return(n*factorial(n-1))  
  print(factorial(5))
  
y = 5
z = lambda x : x * y
print(z(9))

i = 1
while True:
  if i % 5 == 0:
    break
  print(i)
  i += 1
  
my_string = "Educative"
print (my_string[::-1])

# my_string = 'Educative'
# for i in range(my_string):
#   print(i)
  
my_string = 'Hello'
for i in range(len(my_string)):
  print (my_string)
  my_string = 'a'
  
my_string = "Hello World"
i = 0
while i < len(my_string):
    print(my_string[i], end=" ")
    i += 1
    
def detect_pattern(s1, s2): # this function takes two parameters as strings to compare.
  # Keep in mind that this method should return the same value 
  # no matter what order the two strings are passed
  
  # Insert your code here
  if s1 == s2:
    return True
  else:
    return False


s1 = "aba"
s2 = "xyz"
print(detect_pattern(s1, s2)) # Output: False