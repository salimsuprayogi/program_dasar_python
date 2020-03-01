# Script Budi Raharjo
# Author Salim Suprayogi

import os


def konversi_suhu():
    # rumus yang digunakan C = 5 * (F-32)/9
    # menampilkan informasi program
    print("\nKonversi Suhu dari Fahrenheit ke Celcius)")

    # input suhu dalam fahrenheit
    f = float(input("Masukan suhu (Fahrenheit): "))

    # melakukan konversi suhu ke Celcius
    c = 5 * (f-32)/9

    # menampilkan hasil konversi
    print("Fahrenheit \t:", f)
    print("Celcius \t:", c, "\n")
    os.system("pause\n")


# if __name__ == "__main__":
#     konversi_suhu()
