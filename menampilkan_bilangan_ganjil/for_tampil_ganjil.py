def main():
    batas_bawah = 10
    batas_atas = 30

    for bil in range(batas_bawah, batas_atas):
        if bil % 2 == 1:
            if (bil == 21) or (bil == 27):
                continue
            print(bil)
        else:
            pass


if __name__ == "__main__":
    main()
