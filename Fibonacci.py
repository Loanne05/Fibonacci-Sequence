# Fibonacci Sequence
def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

while True:
    print("---------------------------")
    number = int(input("Enter a number: "))

    print("\n")
    print("Fibonacci Sequence: ")
    total = 0
    for i in range(number+1):
        print(fib(i))
        total = total + fib(i)
    print("Overall total of fibonacci sequence:", total)
    print("\n")
    print(f"{number}th term:")
    print(fib(number))