import random

# tal = random.randint(1, 100)
# while True:
#     gissning = int(input("gissa talet 1-100: "))
#     if gissning > tal:
#         print("för högt")
#     elif gissning < tal:
#         print("för lågt")
#     else:
#         print("rätt")
#         break


# namn = ["alex", "jake", "albert", "clark"]
# vald_namn = ""
# while True:
#     val = input("Välja mellan tärning, tärning2 och namn. 0 för att avsluta: ")
#     if val == "tärning":
#         print(random.randint(1, 6))
#     elif val == "tärning2":
#         print(random.randint(1, 6))
#         print(random.randint(1, 6))
#     elif val == "namn":
#         if len(namn) == 0:
#             print("namn lista är tomt")
#             continue
#         vald_namn = random.choice(namn)
#         print(vald_namn)
#         namn.remove(vald_namn)
#     elif val == "0":
#         break


# antal_försök = 7
# tal = random.randint(1, 100)
# while True:
#     gissning = int(input("gissa talet 1-100: "))
#     if gissning > tal:
#         print("för högt")
#     elif gissning < tal:
#         print("för lågt")
#     else:
#         print("rätt")
#         spela_igen = input("Vill du köra igen? y/n")
#         if spela_igen == "y":
#             antal_försök = 7
#             tal = random.randint(1, 100)
#             continue
#         else:
#             break
    
#     antal_försök -= 1
#     print(f"antal försök kvar: {antal_försök}")
#     if antal_försök == 0:
#         spela_igen = input("Vill du köra igen? y/n")
#         if spela_igen == "y":
#             antal_försök = 7
#             tal = random.randint(1, 100)
#             continue
#         else:
#             break

# spelare_pöang = 0
# dator_pöang = 0

# val_lista = ["Sten", "Sax", "Påse"]

# while True:
#     spelare_val = input("Välj mellan Sten-Sax-Påse: ")
#     dator_val = random.choice(val_lista)
    
#     if spelare_val == dator_val:
#         print(f"Båda valde: {spelare_val}")
#         continue

#     elif spelare_val == "Sten" and dator_val == "Sax":
#         spelare_pöang += 1

#     elif spelare_val == "Sten" and dator_val == "Påse":
#         dator_pöang += 1

#     elif spelare_val == "Sax" and dator_val == "Påse":
#         spelare_pöang += 1

#     elif spelare_val == "Sax" and dator_val == "Sten":
#         dator_pöang += 1

#     elif spelare_val == "Påse" and dator_val == "Sten":
#         spelare_pöang += 1

#     elif spelare_val == "Påse" and dator_val == "Sax":
#         dator_pöang += 1
#     else:
#         print("Fel input försök igen")
#         continue

#     print(f"Spelare valde: {spelare_val}, Dator valde: {dator_val}")
#     print(f"Spelare pöang: {spelare_pöang}")
#     print(f"Datorns pöang: {dator_pöang}")

#     if spelare_pöang == 3 or dator_pöang == 3:
#         if spelare_pöang == 3:
#             print("Du fick 3 pöang och vann!")
#         else:
#             print("Dator fick 3 pöang och vann")

#         spela_igen = input("Vill du spela igen? y/n: ")
#         if spela_igen == "y":
#             dator_pöang = 0
#             spelare_pöang = 0
#             continue
#         else:
#             break


# antal_kast = int(input("Skriv in hur många kast du vill simulera: "))
# totala_kast = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

# for i in range(antal_kast):
#     kast = random.randint(1, 6)
#     totala_kast[kast] += 1
# print(totala_kast)

# for k, v in totala_kast.items():
#     procent = ((totala_kast[k] * 100) // antal_kast)
#     print(f"{k}:or | {"x" * procent} {procent}%")











    

