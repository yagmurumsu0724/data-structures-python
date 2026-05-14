numbers = [40, 10 ,30 , 20, 50]

n = len(numbers)

print("Original array: ")
print(numbers)


for i in range(n):

    for j in range(0, n - i - 1):

        print(f"\nComparing {numbers[j]} and {numbers[j + 1]}")

        if numbers[j] > numbers[j + 1]:
        

            print("Swaoping...")


            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1 ] = temp 

            print(numbers)

print("\nSorted Array: ")
print(numbers)