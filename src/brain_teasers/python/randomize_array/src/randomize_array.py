import random

def improved_fisher_yates_shuffle(arr):
    n = len(arr)

    # Iterate through the array in reverse order
    for i in range(n-1, 0, -1):
        # Generate a random index from the remaining subarray
        j = random.randint(0, i)
        
        # Ensure that the selected index is different from the current index
        while j == i:
            j = random.randint(0, i)

        # Swap the current element with the randomly selected element
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
my_array = [1, 2, 3, 4, 5]
improved_fisher_yates_shuffle(my_array)
print("Shuffled array:", my_array)
