# Mentor : Muhammad Nasrullah
# Author : Salim Suprayogi

# Import

from main_tukar import main_tukar_variabel as tukar_variabel
from main_maksimum import main_nilai_maksimum as nilai_maksimum
from volume_luas_balok import *
from luas_keliling_lingkaran import *
from konversi_suhu import *
from main_jam_detik import main_jam_detik as jam_detik
from trace_table import *

if __name__ == "__main__":
    # menampilkan informasi program
    print("Daftar Program Python")

    programs = [
        "\nDaftar Program :\n"
        "\t1. Cara menukar nilai variabel",
        "\t2. Nilai maksimum dari bilangan",
        "\t3. Volume dan Luas Permukaan Balok",
        "\t4. Luas dan Keliling Lingkaran",
        "\t5. Konversi suhu",
        "\t6. konversi jam dan atau detik",
        "\t7. Trace Table",
        "\t8. Keluar"
    ]

    while True:
        for program in programs:
            print(program)

        pilih = input("\n\tPilih Program : ")

        if (pilih == "1"):
            tukar_variabel()
        elif (pilih == "2"):
            nilai_maksimum()
        elif (pilih == "3"):
            volume_luas_balok()
        elif (pilih == "4"):
            luas_keliling_lingkaran()
        elif (pilih == "5"):
            konversi_suhu()
        elif (pilih == "6"):
            jam_detik()
        elif (pilih == "7"):
            trace_tabel()
        else:
            print("Sampai Jumpa Kembali...:-D")
            exit(code=1)
