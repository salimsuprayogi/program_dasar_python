from konver_jam_kedetik import *


def main_jam_detik():
    "main untuk menjalankan program konversi jam dan detik"
    print("\nProgram Konversi Jam dan Detik")

    metodes = [
        "\nPilihan :\n"
        "\t1. Konversi Jam Ke Detik",
        "\t2. Konversi Detik Ke Jam ",
        "\t3. Pilih Program Lain"
    ]

    while True:
        for metode in metodes:
            print(metode)

        input_cara = input("\nPilih Metode :")

        if (input_cara == "1"):
            konversi_jam()
        elif (input_cara == "2"):
            konversi_detik()
        else:
            print("Sampai jumpa kembali...-D")
            exit(code=1)
