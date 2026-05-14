numbers = [10 , 20, 30 , 40, 50 ,60 , 70]

target = int(input("Enter number to search: "))

left = 0
right = len(numbers) - 1 

found = False 

while left <= right:

    mid = (left + right) // 2

    print(f"\nleft: {left}")
    print(f"Right: {right}")
    print(f"Mid: {mid}")
    print(f"Checkiing: {numbers[mid]}")

    if numbers[mid] == target:
        print(f"\nElement found at index {mid}")
        found = True
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if not found: 
    print("\nElement not found")