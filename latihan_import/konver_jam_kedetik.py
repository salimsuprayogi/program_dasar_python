# Script Budi Raharjo
# Author Salim Suprayogi


def konversi_jam():
    "konversi jam ke detik"
    #  menampilkan informasi program
    print("Konversi Jam Ke Detik\n")

    # rumus : total detik = (jam * 3600) + (menit * 60) + detik

    # input jam, menit, dan detik
    hh = int(input("Masukkan jumlah jam \t: "))
    mm = int(input("Masukkan jumlah menit \t: "))
    ss = int(input("Masukkan jumlah detik \t: "))

    # melakukan konversi hh:mm:ss ke detik
    totaldetik = (hh * 3600) + (mm * 60) + ss

    # menampilkan hasil konversi
    # print(str(hh), ":", str(mm), ":", str(ss),
    #       " sama dengan ", str(totaldetik), " detik")

    print("\n%d :%d :%d sama dengan %d detik" % (hh, mm, ss, totaldetik))


def konversi_detik():
    "konversi detik ke jam"
    # menampilkan informasi program
    print("Konversi Detik ke Jam\n")

    # input total detik
    totaldetik = int(input("Masukkan detik \t: "))

    #  melakukan konversi hh:mm:ss ke detik
    hh = totaldetik // 3600
    sisadetik = totaldetik % 3600
    mm = sisadetik // 60
    ss = sisadetik % 60

    # menampilkan hasil konversi
    print("\n%d detik sama dengan %d :%d :%d" % (totaldetik, hh, mm, ss))


# if __name__ == "__main__":
    # konversi_jam()
    # konversi_detik()