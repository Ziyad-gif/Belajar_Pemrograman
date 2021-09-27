print("Kalkulator sederhana ")

angka1 = int(input("masukan angka 1 :"))
angka2 = int(input("masukan angka 2 :"))
operator = input("masukan operand : ")

if operator == "+":
    print(angka1 + angka2)
elif operator == "*":
    print(angka1 * angka2)
elif operator == "/":
    print(angka1 / angka2)
elif operator == "-":
    print(angka1 - angka2)
else :
    print("isi yang benar")