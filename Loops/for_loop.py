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
string_list = ["Hello", "World", "Educative", "Learning", "Platform"]
print(len(string_list))
for str in string_list:
    print(str)
    
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