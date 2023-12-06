//uses an iterative approach to count the occurrences of the first digit (1 to 9) in all numbers from 0 up to the given number n.
//It uses a while loop that iterates through the digit places (1s, 10s, 100s, etc.) by multiplying i by 10 in each iteration. For each digit place, it calculates how many times the first digit appears within that place range.
// it calculates the occurrences of the first digit and accumulates these counts


def first_digit_count(n):
    count = 0
    i = 1

    while i <= n:
        divider = i * 10
        count += ((n // divider) * i + min(max(n % divider - i + 1, 0), i) if i > 1 else (n // divider + 1) * i)
        i *= 10

    return count

# Taking integer input from the user
digit = int(input("Enter an integer: "))
result = first_digit_count(digit)
print(f"The count of the first digit in numbers up to {digit}: {result}")
