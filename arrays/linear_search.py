#linear search example 
numbers = [10 , 20 , 30, 40 , 50]
target = int(input("Enter number to search: ")) 
                   
found = False 


for i in range(len(numbers)):
    print(f"Cgecking index{i}...")


    if numbers[i] == target:
        print(f"Element fount at index{i}")
        found = True
        break

if not found:
    print("Element not found")

target = 30 #bulmak istediğimiz değer

found = False 

range(len(numbers))
if numbers[i] == target:
    print(f"Element found at index {i}")

