# commit yoursel to github

#usun mnie albo nie
# łańcuch="słowo"
# długość = len(łańcuch)

# for i in range(długość):
#     print(łańcuch[i])
#
# for litera in łańcuch:
#     print(litera)

# print("Podaj imię")
# łań2 = input()
# łań3 = "Cześć "
# łań4 = " ! Miło mi cię widzieć"
#
# print(łań3 + łań2 + łań4)
# łań5 = (łań3 + łań2 + łań4)
# print(łań5)

# łańcuch = "Jeszcze więcej liter"

# ew = 0
# for litera in łańcuch:
#     if "e" == litera:
#         ew +=1
#     if ew == 0:
#         print("nie ma tu \"e\"")
#     else:
#         print("Znalazłem", ew, "liter e")


# if "e" in łańcuch:
#     print("Znalazłem \"e\"")

# nowy_łańcuch = ""
#
# for litera in łańcuch:
#     if "e" == litera:
#         nowy_łańcuch+="aaa"
#     else:
#         nowy_łańcuch+=litera
#
# print(nowy_łańcuch)
#
# łańcuch = "slowo"
# # print(łańcuch)
# #
# # lancuch_lista=list(łańcuch)
# # lancuch_lista[1]="m"
# # łańcuch="".join(lancuch_lista)
# # print(łańcuch)
#
# print(łańcuch.replace("s","sakakakakaka"))



#zadanka

#pierwsze 3 i 2 ostatnie chcą tutorialspointa
#odeń zacząć


# zadalanca = "Jedzmie pociąg z daleka na nikogo nie czeka konduktorze łaskawy byle nie do Wamrszawy"
#
# if zadalanca.isalpha():
#     print("To tylko litery")
# else:
#     print("To nie tylko litery")
#
# print(zadalanca.capitalize())
#
# print(zadalanca.replace(" ",""))
#
# print(zadalanca.rfind("m"))

# #odwórć słowo
#
# imie = "Andrzej"
# nowy_łańcuch=""
# k=0
#
# for i in range(len(imie)):
#     nowy_łańcuch += imie[-i-1]
#
# print(nowy_łańcuch)
# # print(imie[::2])


#zamienić pierwszymi literami

print("1. słowo:")
jednslowo = input()
print("Poda 2. słowo:")
drugslowo = input()

x = jednslowo[0:2]
jednslowo = jednslowo.replace(jednslowo[0],drugslowo[0:2])
drugslowo = drugslowo.replace(drugslowo[0],x)

print(jednslowo)
print(drugslowo)
