# Author    : Salim Suprayogi
# ref       : https://www.geeksforgeeks.org/

import keyword
import json


def batas():
    x = 70
    y = "*"
    print(x*y)


def key_word():
    batas()
    print("How to check if a string is a valid keywords in Python?")
    # fungsi iskeyword()
    # s = "for"
    nama_var = input("Nama Keywords : ")
    if keyword.iskeyword(nama_var):
        print("%s termasuk keywords python" % nama_var)
    else:
        print("%s tidak termasuk keywords python" % nama_var)
    batas()


def check_keyword():
    batas()

    print("How to check if a string is a valid keyword in Python ?\n")

    input_nama = input("Nama Keywords : ")

    if input_nama in keyword.kwlist:
        print("\"%s\" termasuk keywords python\n" % input_nama)
    else:
        print("\"%s\" tidak termasuk keywords python\n" % input_nama)

    batas()

    print("Daftar Keywords Python : ")
    key = keyword.kwlist
    tampilkan_fungsi = []
    for i in range(0, len(key)):
        nama_fungsi = key[i]
        add_fungsi = {
            "Keywords Python": nama_fungsi
        }
        tampilkan_fungsi.append(add_fungsi)
    print(json.dumps(obj=tampilkan_fungsi, sort_keys=4, indent=True))

    batas()


if __name__ == "__main__":
    check_keyword()
