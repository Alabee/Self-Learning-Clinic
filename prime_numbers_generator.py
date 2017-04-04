def prime_number_generator(n):
    if not isinstance(n, int):
        return "Only integers allowed"

    elif n < 0:
        return "Invalid input, only positive numbers allowed"

    elif n == 0:
        return "No prime numbers between 0 and 0"

    else:
        for x in range(2, n):
            for y in range(2, x):
                if (x % y == 0):
                    break

            
            else:
                print(x)


if __name__ = "__main__":
    main()
