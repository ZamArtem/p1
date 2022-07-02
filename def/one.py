
len = None
sum = None
min = None
max = None

# 1. Melyik a legkisebb szám a listában?
# Készíts függvényt legkisebb() néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.
# Figyelem! A feladat megoldása során nem használhatod a min függvényt! 

lista = [1,2,3,57,0,22,78]
def legkisebb(x):
  #min(lista)
  kicsi = x[0]
  for sor in x:
    if sor < kicsi:
      kicsi = sor
  return kicsi   
print(legkisebb(lista))


# 2. Mennyi a lista számainak összege?
# Készíts függvényt osszeg() néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.
# Figyelem! A feladat megoldása során nem használhatod a sum függvényt! 
lista = [1,2,3,57,0,20,73]
def osszeg(valami):
  #sum(lista)
  szumma = 0
  for sor in valami:
    szumma += sor
  return szumma

print(osszeg(lista))
# 3. Mennyi a listában levő számok szorzata?
# Készíts függvényt szorzat() néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával. 
lista = [1,2,3,4,5,6,7,8,9]
def szorzat(sajt):
  szor = 1 
  for sor in sajt:
    szor *= sor
  return szor

print(szorzat(lista))   
# 4. Mennyi a páros számok száma a listában?
# Készíts függvényt parosok_szama() néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával. 

def parosok_szama(lista):
  szamlalo = 0
  for sor in lista:
    if sor % 2 == 0:
      szamlalo += 1
  return szamlalo


print(parosok_szama(lista))   
