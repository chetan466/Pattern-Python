def pattern_square(n):
    for i in range(n):
        print('* ' * n)

def pattern_right_triangle(n):
    for i in range(1, n + 1):
        print('* ' * i)

def pattern_left_triangle(n):
    for i in range(1, n + 1):
        print('  ' * (n - i) + '* ' * i)

def pattern_pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

def pattern_diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)

# Dictionary acting as switch-case
pattern_switch = {
    '1': pattern_square,
    '2': pattern_right_triangle,
    '3': pattern_left_triangle,
    '4': pattern_pyramid,
    '5': pattern_diamond
}

def main():
    while True:
        print("\nStar Pattern Menu")
        print("1. Square")
        print("2. Right Triangle")
        print("3. Left Triangle")
        print("4. Pyramid")
        print("5. Diamond")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            print("Exiting program.")
            break

        n = int(input("Enter the number of rows: "))

        pattern_function = pattern_switch.get(choice)
        if pattern_function:
            pattern_function(n)
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program
main()
