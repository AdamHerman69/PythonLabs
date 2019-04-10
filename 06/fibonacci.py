def fibonacci(n):
    numbers = [0,1]
    for i in range(2,n):
        numbers.append(numbers[i - 2] + numbers[i - 1])
    return numbers


def fib(n):
    return fibonacci(n)[n-1]
