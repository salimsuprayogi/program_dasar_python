# Script Budi Raharjo
# Author Salim Suprayogi

import math
# konstanta pi di dapat dari modul math (3.146)
import os


def luas_keliling_lingkaran():
    # menampilkan informasi program
    print("Luas dan Keliling Lingkaran\n")

    # input jari-jari
    r = float(input("Masukan nilai jari-jari : "))

    # menghitung luas lingkaran
    # luas = pi.r2
    l = math.pi * (r**2)

    # menghitung keliling lingkaran
    k = 2 * math.pi * r

    # menampilkan hasil perhitungan
    print("Luas lingkaran \t\t:", l, "/", round(l))
    print("Keliling lingkaran \t:", k, "/", round(k), "\n")
    os.system("pause\n")


# if __name__ == "__main__":
#     luas_keliling_lingkaran()
