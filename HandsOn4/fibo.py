# Nagmat Nazarov

def fibo_rec(n):
    print("fibo{}".format(n))
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

# Test the function
print(f"Fibonacci({5}): {fibo_rec(5)}")
