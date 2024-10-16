# Created by Collins Senaya and Ethan Edwards on 10/12/2024

'''
Function to count the number of valid strings of length n
Input: n (length of the string)
Output: Number of valid strings of length n, where for any given substring of length 6,
        {'a', 'b', 'c', 'd'} must be present at least once
'''
def count(n):
    # Edge case: For strings of length <= 5, all combinations are valid
    if n <= 5:
        return 4 ** n

    # Initialize a list to hold the number of valid strings of length n
    # dp[length][window] will store the count of valid strings of a given length ending with a specific window
    dp = [[0] * (4 ** 6) for _ in range(n + 1)]

    # Pre-calculate valid combinations of 6 characters over {a, b, c, d}
    valid_states = []
    for i in range(4 ** 6):
        window = []
        temp = i
        for j in range(6):
            window.append(temp % 4)
            temp //= 4
        window = ''.join(['abcd'[k] for k in window])
        if all(c in window for c in 'abcd'):
            valid_states.append(window)

    # Map from state representation to index
    state_to_index = {state: idx for idx, state in enumerate(valid_states)}

    # Initialize the dp for length 6 by populating all possible combinations of 6 characters
    for i in range(4 ** 6):
        window = []
        temp = i
        for j in range(6):
            window.append(temp % 4)
            temp //= 4
        window = ''.join(['abcd'[k] for k in window])
        if len(window) == 6 and all(c in window for c in 'abcd'):
            dp[6][state_to_index[window]] += 1

    # Populate the DP table for lengths from 7 to n
    for length in range(7, n + 1):
        for idx, state in enumerate(valid_states):
            for char in 'abcd':
                new_window = state[1:] + char  # Slide window
                if new_window in state_to_index:
                    dp[length][state_to_index[new_window]] += dp[length - 1][idx]

    # The result is the sum of all valid states for length n
    total_valid_strings = sum(dp[n][state_to_index[state]] for state in valid_states)

    return total_valid_strings


'''
Main function
Input(from user): n (length of the string)
Output(to stdout): Number of valid strings of length n
'''
def main():
    n = input("Enter the length of the string: ")
    print("n =", n, "     Answer:", count(int(n)))
    exit(0)


if __name__ == "__main__":
    main()
