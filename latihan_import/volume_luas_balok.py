# Script Budi Raharjo
# Author Salim Suprayogi

import os


def volume_luas_balok():
    """
    rumus
    volume = p.l.t
    luas permukaan = 2.(p.l + p.t + l.t)
    """
    # menampilkan informasi program
    print("\nVolume dan Luas Permukaan Balok\n")

    # input panjang, lebar dan tinggi
    p = float(input("Panjang \t: "))
    l = float(input("Lebar \t\t: "))
    t = float(input("Tinggi \t\t: "))

    # melakukan perhitungan
    v = p * l * t
    lp = 2 * (p*l + p * t + l*t)

    # menampilkan hasil perhitungan
    print("\nVolume \t\t:", v)
    print("Luas Permukaan \t:", lp, "\n")
    os.system("pause\n")


# if __name__ == "__main__":
#     volume_luas_balok()
