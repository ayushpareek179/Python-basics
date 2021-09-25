# Collatz sequence - the simplest math problem
def collatz(number):
    if number % 2 == 0:
        ans = number // 2
    else:
        ans = 3 * number + 1
    # Formatting
    if ans != 1:
        print(ans, end=", ")
    else:
        print(ans)
    return ans


if __name__ == "__main__":
    print("Enter a number")
    while True:
        # Input validation
        try:
            n = int(input())
            break
        except ValueError:
            print("Invalid input, enter an integer")
    length = 0
    while n != 1:
        n = collatz(n)
        length += 1
    print("Collatz sequence length: " + str(length))
