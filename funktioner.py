# def hälsning(namn):
#     print(f"Hej {namn}! Vad kul att du är här.")
# hälsning("stefan")

# def area(bredd, höjd):
#     return bredd * höjd
# print(area(10, 5))

# def jämnt(tal):
#     if tal % 2 == 0:
#         return True
#     else:
#         return False
# print(jämnt(3))

# def omvandlare(temperatur):
#     return temperatur * 1.8 + 32
# print(omvandlare(20))

# def högsta_talet(tal1, tal2, tal3):
#     if tal1 > tal2 and tal1 > tal3:
#         return tal1
#     elif tal2 > tal1 and tal2 > tal3:
#         return tal2
#     else:
#         return tal3
# print(högsta_talet(7,9,2))

# def betygsättare(betyg):
#     if betyg > 90:
#         return "A"
#     elif betyg > 80:
#         return "B"
#     elif betyg > 70:
#         return "C"
#     elif betyg > 60:
#         return "D"
#     elif betyg > 50:
#         return "E"
#     else:
#         return "F"
# print(betygsättare(83))

# vokaler = ['a', 'o', 'u', 'å', 'e', 'i', 'y', 'ä', 'ö']
# def vokalräknare(text):
#     antal_vokaler = 0
#     for i in text:
#         if i in vokaler:
#             antal_vokaler += 1
#     return antal_vokaler
# print(vokalräknare("Programmering"))

# def list_summering(lista):
#     summa = 0
#     for i in range(len(lista)):
#         summa += lista[i]
#     return summa
# print(list_summering([7, 5, 4]))

# def palindrom_koll(ord):
#     ord_baklänges = ""
#     x = 1
#     for i in ord:
#         ord_baklänges += ord[len(ord) - x]
#         x += 1
#     if ord == ord_baklänges:
#         return True
#     else:
#         return False
# print(palindrom_koll("kajak"))
# print(palindrom_koll("lösenord"))

# nummer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# def lösenordsvalidering(lösenord):
#     if len(lösenord) >= 8 and lösenord != "password":
#         for i in lösenord:
#             if i in nummer:
#                 return True
#             else:
#                 continue
#     return False
# print(lösenordsvalidering("Sommar2025"))

            



