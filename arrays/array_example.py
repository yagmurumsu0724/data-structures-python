# Array Example
numbers = [1, 2, 3, 4, 5]
print("Array:", numbers)

print(numbers[1])
print(numbers[2])
print(numbers[3]) 
print(numbers[4])
#indeks sıfırdan başlıyor çünkü 
# adres= başlangıç_adres + index * veri_boyutu

#DİZİYİ GEZME 
for number in numbers:
    print(number)

#Dizideki tüm elemanları tek tek ziyaret etmek.

for i in range(len(numbers)):
    print(f"Index: {i} Value: {numbers[i]}")

#Burada: 
#len(numbers) -> eleman sayısı 
#range() -> sayı üretir 
#numbers[i] -> index erişimi
