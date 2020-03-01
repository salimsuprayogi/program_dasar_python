from tukar_nilaivariabel import *


def main_tukar_variabel():
    "main untuk menjalankan program tukar nilai variabel"
    print("\nProgram Tukar Nilai Variabel (Integer)")

    metodes = [
        "\nPilih Metode :\n"
        "\t1. Metode Pertama",
        "\t2. Metode Kedua",
        "\t3. Metode Ketiga",
        "\t4. Pilih Program Lain"
    ]

    while True:
        for metode in metodes:
            print(metode)

        input_cara = input("\nPilih Metode :")

        if (input_cara == "1"):
            cara_pertama()
        elif (input_cara == "2"):
            cara_kedua()
        elif (input_cara == "3"):
            cara_ketiga()
        else:
            print("Sampai jumpa kembali...-D")
            exit(code=1)
