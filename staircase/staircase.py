def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

if __name__ == '__main__':
    n = int(input("Enter the height of the staircase: ").strip())
    staircase(n)
