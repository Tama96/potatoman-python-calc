def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2

print("Silahkan pilih untuk melakukan perhitungan" "\n1. Penambahan"
    "\n2. Pengurangan"
    "\n3. Perkalian"
    "\n4. Pembagian")

select = int(input("Pilih Menu 1,2,3,4: "))
inputnum1 = float(input("Masukkan Angka Pertama :"))
inputnum2 = float(input("Masukkan Angka Kedua :"))

if select == 1:
    print(inputnum1, "+", inputnum2, "=", inputnum1+inputnum2)
elif select == 2:
    print(inputnum1, "-", inputnum2, "=", inputnum1-inputnum2)
elif select == 3:
    print(inputnum1, "x", inputnum2, "=", inputnum1*inputnum2)
elif select == 4:
    print(inputnum1, "/", inputnum2, "=", inputnum1/inputnum2)
else:
    print("input salah")