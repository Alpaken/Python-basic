a = 5
b = 2
c = 6

najwieksza = a

# Klasyczny zapis
if b > najwieksza:
        najwieksza = b

if c > najwieksza:
        najwieksza = c

# Skrócony zapis

najwieksza = a if a > b and a > c else b if b > c else c

print("Największa liczba to:", najwieksza)