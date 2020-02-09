# program kalkulator sederhana metode pertama
a = True
while a == True:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Selamat datang di menu kalkulator dasar')
    print("===================================================")
    print(
        'Silahkan pilih operator yang anda inginkan :\n'
        '1. Penjumlahan\n'
        '2. Pengurangan\n'
        '3. Perkalian\n'
        '4. Pembagian\n'
        '5. Modulus / Sisa Bagi\n'
        '6. Keluar'
    )
    menu = input('Masukkan pilihan anda di sini : ')
    try:
        if menu == '1':
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            hasil = angka_pertama + angka_kedua
            print('Hasil dari', angka_pertama, '+', angka_kedua, '=', hasil)
            print("===================================================")
        if menu == '2':
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            hasil = angka_pertama - angka_kedua
            print('Hasil dari', angka_pertama, '-', angka_kedua, '=', hasil)
            print("===================================================")
        if menu == '3':
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            hasil = angka_pertama * angka_kedua
            print('Hasil dari', angka_pertama, 'x', angka_kedua, '=', hasil)
            print("===================================================")
        if menu == '4':
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            hasil = angka_pertama / angka_kedua
            print('Hasil dari', angka_pertama, '/', angka_kedua, '=', hasil)
            print('Hasil pembulatannya =', round(hasil))
            print("===================================================")
        if menu == '5':
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            hasil = angka_pertama % angka_kedua
            print('Hasil dari', angka_pertama, '%', angka_kedua, '=', hasil)
            print("===================================================")
    except:
        print("***************************************************")
        print('Input hanya diperbolehkan angka, dimulai dari 0 - 9')
        print("***************************************************")

    if menu.strip() == '6':
        # menggunakan fungsi strip() agar ketika pilih '2', tidak masuk pada fungsi while
        print('#Semoga hari anda menyenangkan#')
        break
