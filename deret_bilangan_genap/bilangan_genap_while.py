def main():
    # menampilkan program
    print("Program deret bilangan genap")

    n = 20
    i = 0
    while i < n:
        if i % 2 == 0:
            if i % 4 != 0:
                bil = i
                print(bil)
        i += 1


if __name__ == "__main__":
    main()
