# Prosty if
suma = 0

for i in range(1,101):
    suma += i

print("Suma liczb od 1 do 100 to:",suma,"\n")

# If z indeksowaniem
lista = ["Mercedes", "BMW", "Skoda"]

for i, auto in enumerate(lista):
    print(i, auto)

print()

# If z łączeniem dwóch tablic
liczby = [1,2,3]
owoce = ["jabłko", "arbuz", "ananas"]

for liczba, owoc in zip(liczby,owoce):
    print(liczba, owoc)

print()

# If z operacjami
liczby = [1,2,3,4,5]

kwadraty = [x**2 for x in liczby]

print(kwadraty)

print()

# While
x = 1
while x <= 10:
    print(x)
    x += 1

print()

# Do-While
x = 1
while True:
    print(x)
    x += 1
    if x > 10:
        break