
# 1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True 
    else:
        return False
# 2
def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    
    total = sum(arr)
    highest = max(arr)
    lowest = min(arr)
    
    return total - highest - lowest

# 3
#  result = ""
    for char in s:
        result += char + char
    return result
# 4 
def array_plus_array(arr1,arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    return sum1 + sum2

# 5 

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
