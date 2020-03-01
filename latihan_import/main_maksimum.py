from nilai_maksimum_bilangan import *


def main_nilai_maksimum():
    "main untuk menjalankan program nilai maksimum"
    print("\nProgram Nilai maksimum dari bilangan")

    metodes = [
        "\nPilihan :\n"
        "\t1. Nilai Maksimum Dua Bilangan",
        "\t2. Metode Pertama Nilai Maksimal ",
        "\t3. Metode Kedua Nilai Maksimal ",
        "\t4. Metode Ketiga Nilai Maksimal ",
        "\t5. Nilai Maksimum Dengan Fungsi Python",
        "\t6. Pilih Program Lain"
    ]

    while True:
        for metode in metodes:
            print(metode)

        input_cara = input("\nPilih Metode :")

        if (input_cara == "1"):
            nilai_max_dua()
        elif (input_cara == "2"):
            cara_pertama()
        elif (input_cara == "3"):
            cara_kedua()
        elif (input_cara == "4"):
            cara_ketiga()
        elif (input_cara == "5"):
            nilai_max_python()
        else:
            print("Sampai jumpa kembali...-D")
            exit(code=1)
