from random import randint
import time
import sys
b = False
a = randint(1,50)
temp = True
while temp == True:
  c = input("Haluatko aloittaa pelin (kyllä // ei)")
  if c == "kyllä":
    b = True
    print("Tarkoituksena on arvata oikea numero, sovellus ilmoittaa onko numero suurempi vai pienempi.")
    temp == False
    break
  elif c == "ei":
      print("Sammutetaan.")
      time.sleep(1)
      sys.exit(0)
  else:
    print("kyllä /ei ")
while b == True:
    try:
      d = int(input("Arvaus:"))
      if d > a:
        print("Arvattava numero on pienempi")
      elif d < a:
        print("Arvattava numero on suurempi")
      else:
        print("Oikein arvattu, vastaus oli")
        print(a)
        b = False
        time.sleep(15)
        sys.exit(0)
    except ValueError:
        print ("Vastauksen täytyy olla numero :3")
        continue









