def n_th_fibonnaci(original_list, n):
    """
    Extend the original list by appending the sum of the last two elements 'n' times.

    Parameters:
    original_list : list
        The original list of numbers.
    n : int
        The number of times to generate and append the sum of the last two elements.

    Returns:
    list
        The original list extended with the sum of the last two elements 'n' times.
    """
    for _ in range(n):
        # Calculate the sum of the last two elements
        sum_last_two = original_list[-1] + original_list[-2]
        
        # Append the sum to the original list
        original_list.append(sum_last_two)
        
    return original_list

# Example usage
original_list = [0, 1]  # Initial list
n = 10  # Number of times to generate and append the sum
extended_list = n_th_fibonnaci(original_list, n)
print("The nth fibonacci sequence is ::", extended_list)
