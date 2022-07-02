# 1. A karakterek_szama(fname) függvény visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')
def karakterek_szama(fname):
  with open(fname)as f:
    return len(f.read())
    
# 2. A szavak_szama(fname) függvény visszatér a fname) fájlban levő szavak számával.
def szavak_szama(fname):
  with open(fname)as f:
    return len(f.read().split())
    
# 3.  A sorok_szama(fname) függvény visszatér a  fájlban levő sorok számával.   
def sorok_szama(fname):
  with open(fname)as f:
    return len(f.readlines())
    
# 4. Az r_betuk_szama(fname) függvény visszatér a  fájlban levő 'r' betük számával.
def r_betuk_szama(fname):
  with open(fname)as f:
    return f.read().count("r")
    
# 5. A lorem_szavak_szama(fname) függvény visszatér a  fájlban levő "lorem" szavak számával.
def lorem_szavak_szama(fname):
  with open(fname)as f:
    return f.read().count("lorem")

# 6. A leggyakoribb_karakter(fname) függvény visszatér a  fájlban leggyakrabban előforduló karakterrel.
def leggyakoribb_karakter(fname):
  stat = dict()
  with open(fname)as f:
    for betu in f.read():
      stat[betu] = stat.get(betu,0) + 1
  return max(stat ,key = stat.get)
# 7. A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.
def leghosszabb_sor_hossza(fname):
  nagy = 0
  with open(fname)as f:
    for sor in f.readlines():
      if nagy < len(sor):
        nagy = len(sor)
  return nagy
