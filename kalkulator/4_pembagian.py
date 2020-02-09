#program kalkulator sederhana untuk pembagian

while True:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Selamat datang di menu pembagian aritmetika dasar')
    print("===================================================")
    try:
        angka_pertama = int(input('Silahkan input angka pertama : '))
        print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

        angka_kedua = int(input('Silahkan input angka kedua : '))
        print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
        print("===================================================")

        hasil = angka_pertama / angka_kedua
        print('Hasil dari', angka_pertama, '/', angka_kedua, '=', hasil)
        print('Hasil pembulatannya =', round(hasil))
        print("===================================================")
    except:
        print("***************************************************")
        print('Input hanya diperbolehkan angka, dimulai dari 0 - 9')
        print("***************************************************")
