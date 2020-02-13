def main():
    # menampilkan program
    print("Program deret bilangan genap")

    n = 20
    for i in range(n):
        if i % 2 == 0:
            if i % 4 != 0:
                bil = i
                print(bil)


if __name__ == "__main__":
    main()
