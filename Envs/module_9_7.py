
def is_prime(func):
    def wrapper(*args, **kwargs):
        count = 0
        result = func(*args, **kwargs)
        for i in range(1, result + 1):
            if result % i == 0:
                count += 1
        if count == 2:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(*args):
    sum_numb = 0
    for i in args:
        sum_numb += i
    return sum_numb


result = sum_three(2, 3, 6)
print(result)