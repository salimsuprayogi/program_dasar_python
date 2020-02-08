import os


def main():
    # rumus yang digunakan C = 5 * (F-32)/9
    # menampilkan informasi program
    print("Konversi Suhu dari Fahrenheit ke Celcius)\n")

    # input suhu dalam fahrenheit
    f = float(input("Masukan suhu (Fahrenheit): "))

    # melakukan konversi suhu ke Celcius
    c = 5 * (f-32)/9

    # menampilkan hasil konversi
    print("Fahrenheit \t:", f)
    print("Celcius \t:", c, "\n")
    os.system("pause")


if __name__ == "__main__":
    main()
