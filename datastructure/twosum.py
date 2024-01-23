def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}
    print(num_indices[11])

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (the value needed to reach the target)
        complement = target - num
    
        # Check if the complement is in the dictionary
        if complement in num_indices:
            
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]
        
        
        # If not found, add the current number and its index to the dictionary
        num_indices[num] = i

    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]


target = 9
result = two_sum(nums, target)
print(result)
