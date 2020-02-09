# program kalkulator sederhana metode kedua

while True:
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('Selamat datang di menu kalkulator sederhana')
    print("===================================================")

    print(
        'Silahkan pilih menu berikut :\n'
        '1. Mulai\n'
        '2. Selesai'
    )

    menu = input('Masukkan pilihan anda di sini : ')

    try:
        menuUser1 = ['1', 'Mulai', 'mulai', 'MULAI']
        if menu in menuUser1:
            # if menu == '1 :
            angka_pertama = int(input('Silahkan input angka pertama : '))
            print("'Anda memilih angka pertama :", str(angka_pertama) + "'")

            pilih = input('Operator yang anda pilih : ')

            angka_kedua = int(input('Silahkan input angka kedua : '))
            print("'Anda memilih angka kedua :", str(angka_kedua) + "'")
            print("===================================================")

            if pilih == '+':
                hasil = angka_pertama + angka_kedua
                print('Hasil dari', angka_pertama,
                      '+', angka_kedua, '=', hasil)
            elif pilih == '-':
                hasil = angka_pertama - angka_kedua
                print('Hasil dari', angka_pertama,
                      '-', angka_kedua, '=', hasil)
            elif pilih == '/':
                hasil = angka_pertama / angka_kedua
                print('Hasil dari', angka_pertama,
                      '/', angka_kedua, '=', hasil)
            elif pilih == '*':
                hasil = angka_pertama * angka_kedua
                print('Hasil dari', angka_pertama,
                      '*', angka_kedua, '=', hasil)
            elif pilih == '%':
                hasil = angka_pertama % angka_kedua
                print('Hasil dari', angka_pertama,
                      '%', angka_kedua, '=', hasil)
            else:
                print('"""""""""""""""""""""""""""""""""""""""""""""""""""')
                print(
                    'Operator yang di gunakan adalah :\n'
                    '+ = penjumlahan\n'
                    '- = pengurangan\n'
                    '* = perkalian\n'
                    '/ = pembagian\n'
                    '% = sisa bagi'
                )
                print('"""""""""""""""""""""""""""""""""""""""""""""""""""')
            print("===================================================")
    except:
        print("***************************************************")
        print('Ohh, yang anda inputkan tidak sesuai')
        print('Silahkan inputkan nomor saja')
        print("***************************************************")

    menuUser2 = ['2', 'Selesai', 'selesai', 'SELESAI']
    if menu.strip() in menuUser2:
        # menggunakan fungsi strip() agar ketika pilih '2', tidak masuk pada fungsi while
        print('#Semoga hari anda menyenangkan#')
        break
