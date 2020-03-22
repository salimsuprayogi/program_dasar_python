# Author : Salim Suprayogi


def madlibs():
    "program mad libs game"

    print("/___|")
    print("   /|")
    print("  / |")
    print(" /  |")

    warna = input("Enter a color: ")
    kata_benda = input("Enter a plural noun: ")
    nama_artis = input("Enter a celebrity: ")

    print("\nRoses are %s" % warna)
    print("%s are blue" % kata_benda)
    print("I Love %s" % nama_artis)


def surat_cinta():
    "surat cinta untuk kekasih"

    nama_penerima = input("Untuk siapa surat ini :")
    nama_panggilan = input("Nama panggilan untuk surat ini: ")
    pasangan_cewek = input("Nama teman cewek kamu yang sudah menikah: ")
    pasangan_cowok = input("Nama teman cowok kamu yang sudah menikah: ")
    nama_teman = input("Nama teman dekat kamu: ")
    nama_pengirim = input("Nama kamu siapa: ")

    print(
        """
        Dear %s,
        """ % nama_penerima
    )
    print(
        """
        Hai dik % s bagaimana kabarmu dik ? Semoga selalu sehat dan dalam lindungan Tuhan yang maha esa.
        Aku tak pandai merangkai kata untuk surat yang kutulis ini sehingga mungkin surat ini akan kutulis singkat untukmu.
        """ % nama_penerima
    )
    print(
        """
        Semenjak bertemu kamu di acara pernikahan % s dan % s kemarin ada sesuatu yang mengganjal dihatiku yang ingin ku sampaikan kepadamu.
        Aku dengar dari si % s bahwa kamu belum memiliki calon pendamping hidup.
        """ % (pasangan_cewek, pasangan_cowok, nama_teman)
    )
    print(
        """
        Maka dari itu dengan ini aku bermaksud untuk mengajukan diri kepadamu untuk menjadi calon pendampingmu.
        Aku serius % s, jika kamu bersedia maka aku akan langsung datang kerumahmu untuk bertemu kedua orang tuamu.
        """ % nama_panggilan
    )
    print(
        """
        Semoga surat yang aku kirimkan ini tidak menyinggung atau membuatmu tidak berkenan.
        Demikian surat ini saya buat untukmu, besar harapan saya kamu bisa balas surat yang kubuat ini.
        """
    )
    print(
        """
        With Love,
        % s
        """ % nama_pengirim
    )


if __name__ == "__main__":
    # main()
    # surat_cinta()
    print("Halo, kita main Game Madlibs yuk !!!")
    daftar = [
        "Pilih dulu, mau yang mana:",
        "1. Madlibs Game",
        "2. Surat Cinta"
    ]
    while True:
        for daftars in daftar:
            print(daftars)

        selected = input("Masukan pilihan kamu disini: ")

        if (selected == "1"):
            madlibs()
        elif (selected == "2"):
            surat_cinta()
        else:
            print("Trimakasih !!!, Semoga Hari Anda Menyenangkan !!!")
            exit(code=0)
