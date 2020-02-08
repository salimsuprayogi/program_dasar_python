def main():
    x = 1
    y = 1
    jumlah = x + y
    print(x, y, jumlah)
    a = 0

    while a < 7:
        if jumlah < 20:
            x = y
            y = jumlah
            if x == y:
                y = x + y
                jumlah = x + y
                print(x, y, jumlah)
            else:
                jumlah = x + y
                print(x, y, jumlah)
        else:
            print("jumlah 20", x, y, jumlah)
        a += 1


if __name__ == "__main__":
    main()
