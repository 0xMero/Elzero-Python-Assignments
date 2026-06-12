import time
def calculate_time(func):
    def wrapper(*numbers):
        start = time.time()
        func(*numbers)
        end = time.time()
        print(f"Elapsed time is {end - start}")
    return wrapper
@calculate_time
def Loop_nums(*numbers):
    for i in numbers:
        for number in range(1, i + 1):
            print(number)
Loop_nums(100000, 10, 20, 30)