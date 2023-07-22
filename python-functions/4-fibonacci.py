def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fibonacci_numbers = fibonacci_sequence(n-1)
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

        return fibonacci_numbers
    

