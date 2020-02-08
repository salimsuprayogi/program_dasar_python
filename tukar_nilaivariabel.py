import os


def main():
    # menampilkan informasi program
    print("#Cara Pertama\nMenukar nilai dari dua variabel\n")

    # input variabel ke-1 dan ke-2
    a = int(input("Masukan Variabel ke-1: "))
    b = int(input("Masukan Variabel ke-2: "))

    # menampilkan nilai sebelum di tukar
    print("\nSebelum Pertukaran Nilai")
    print("Variabel ke-1 \t:", a)
    print("Variabel ke-2 \t:", b)

    # melakukan pertukatan nilai setelah di tukar
    c = a
    # c adalah variabel bantu
    a = b
    b = c

    # menampilkan nilai setelah ditukar
    print("\nSetelah Pertukaran Nilai")
    print("Variabel ke-1 \t:", a)
    print("Variabel ke-2 \t:", b, "\n")
    os.system("pause")


def main_sub():
    # menampilkan informasi program
    print("\n#Cara Kedua\nMenukar nilai dari dua variabel\n")

    # input variabel ke-1 dan ke-2
    a = int(input("Masukan Variabel ke-1: "))
    b = int(input("Masukan Variabel ke-2: "))

    # menampilkan nilai sebelum ditukar
    print(a, "\t", b)

    # melakukan pertukaran nilai
    a, b = b, a

    # menampilkan nilai setelah di tukar
    print(a, "\t", b, "\n")
    os.system("pause")


def main_sub1():
    # menampilkan informasi program
    print("\nMenukar Nama Depan dan Nama Belakang\n")

    # input variabel ke-1 dan ke-2
    a = str(input("Nama Pertama Kamu \t: "))
    b = str(input("Nama Kedua Kamu \t: "))

    # menampilkan nilai sebelum di tukar
    print("\nSebelum Pertukaran Nama")
    print("Nama Pertama \t:", a)
    print("Nama Kedua \t:", b)

    # melakukan pertukatan nilai setelah di tukar
    c = a
    # c adalah variabel bantu
    a = b
    b = c

    # menampilkan nilai setelah ditukar
    print("\nSetelah Pertukaran Nama")
    print("Nama Pertama \t:", a)
    print("Nama Kedua \t:", b, "\n")
    os.system("pause")


if __name__ == "__main__":
    main()
    main_sub()
    main_sub1()
