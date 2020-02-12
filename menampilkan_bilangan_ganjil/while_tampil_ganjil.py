def main():
    bil = 10

    while bil < 30:
        if bil % 2 == 1:
            if bil != 21 and bil != 27:
                print(bil)
        bil += 1


if __name__ == "__main__":
    main()
