# Script Budi Raharjo
# Author Salim Suprayogi


def nilai_max_dua():
    "fungsi nilai maksimum dari dua buah bilangan"
    # menampilkan judul program
    print("Nilai Maksimum dari dua buah bilangan")

    # input bilangan
    a = int(input("\nMasukkan bilangan ke-1: "))
    b = int(input("Masukkan bilangan ke-2: "))

    #  menentukan nilai maksimum
    if a > b:
        maks = a
    else:
        maks = b

    # menampilkan nilai maksimumnya
    print("\nNilai maksimum adalah %d" % maks)


def cara_pertama():
    "fungsi nilai maksimum dari tiga buah bilangan"
    # menampilkan judul program
    print("1. Nilai Maksimum dari tiga buah bilangan")

    # input bilangan
    a = int(input("\nMasukkan bilangan ke-1: "))
    b = int(input("Masukkan bilangan ke-2: "))
    c = int(input("Masukkan bilangan ke-3: "))

    # menentukan nilai maksimum cara pertama
    if a > b:
        if a > c:
            maks = a
    else:
        if b > c:
            maks = b
        else:
            maks = c

    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d" % maks)


def cara_kedua():
    "fungsi nilai maksimum dari tiga buah bilangan"
    # menampilkan judul program
    print("2. Nilai Maksimum dari tiga buah bilangan")

    # input bilangan
    a = int(input("\nMasukkan bilangan ke-1: "))
    b = int(input("Masukkan bilangan ke-2: "))
    c = int(input("Masukkan bilangan ke-3: "))

    # menentukan nilai maksimum cara pertama
    if a > b and a > c:
        maks = a
    else:
        if b > a and b > c:
            maks = b
        else:
            maks = c

    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d" % maks)


def cara_ketiga():
    "fungsi nilai maksimum dari tiga buah bilangan"
    # menampilkan judul program
    print("3. Nilai Maksimum dari tiga buah bilangan")

    # input bilangan
    a = int(input("\nMasukkan bilangan ke-1: "))
    b = int(input("Masukkan bilangan ke-2: "))
    c = int(input("Masukkan bilangan ke-3: "))

    # menentukan nilai maksimum cara pertama
    maks = a
    if b > maks:
        maks = b
    if c > maks:
        maks = c

    # menampilkan nilai maksimum
    print("\nNilai maksimum adalah %d" % maks)


def nilai_max_python():
    "fungsi nilai max berdasarkan fungsi python"
    # menentukan nilai maksimum dari 5 bilangan
    print("Nilai maksimum menggunakan fungsi dari python")

    #  menentukan nilai maksimum dari 5 bilangan
    bilangan = []   # list kosong

    # pengambilan data
    for i in range(1, 6):    # 6-1 = 5
        nilai = int(input("Masukkan bilangan ke-%d: " % i))  # input nilai
        bilangan.append(nilai)  # menambahkan nilai ke dalam list bilangan

    # pengolahan data
    maks = max(bilangan)  # nilai maskimal menggunakan fungsi max()

    # menampilkan nilai maksimum
    print("\nData bilangan adalah %s " % bilangan)  # %s untuk list
    print("Nilai maksimum adalah %d " % maks)


# if __name__ == "__main__":
    # nilai_max_dua()
    # cara_pertama()
    # cara_kedua()
    # cara_tiga()
    # nilai_max_python()
