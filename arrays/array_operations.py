#array operations
numbers = [10 , 20 , 30 , 40 , 50]

print("Original arrays: ")
print(numbers)

#append 
numbers.append(60)

print("\nAfter append: ")
print(numbers)

#ınsert
numbers.insert(2, 25)

print("\n After insert : ")
print(numbers)

#Remove
numbers.remove(40)

#pop
numbers.pop()

print("\nAfter Pop: ")
print(numbers)


#dizinin uzunlugunu yazdıralım
print(len(numbers))

#ilk elemanı yazdıralım
print(numbers[0])

#son elemanı yazdıralım
print(numbers[-1])

#dizide gezinelim
for number in numbers:
    print(numbers)

#en büyük elemanı bulalım 
max(numbers)

#en küçük elemanı bulalım
min(numbers)
