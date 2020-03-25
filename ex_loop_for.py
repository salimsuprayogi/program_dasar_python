# Autho : Salim Suprayogi
# Ref   : freeCodeCamp.org ( youtube )


def for_string():
    "perulangan string"
    for letter in "Salim Suprayogi":
        print(letter)


def for_list():
    "perulangan list"
    friends = ["Jim", "Karen", "Kevin"]
    for friend in friends:
        print(friend)


def for_list_range():
    "perulangan list menggunakan fungsi range dan len"
    friends = ["Jim", "Karen", "Kevin"]
    # tipe list bisa di akses dengan menggunakan indeks, dimulai dari 0
    # belum menampilkan string di dalam list, hanya mengambil indeks nya saja
    for index in range(len(friends)):
        # fungsi range untuk mengambil semua data dari list
        # dimulai dari 0 sampai N data
        # jika print(index), maka hanya akan tampil indesknya saja
        print(friends[index])
        # gunakan variabel yang bertipe list untuk menampilkan data di dalamnya ( ex : nama)
        # kemudian di ikuti index untuk perulangan di dalam sebanyak data di dalam list


def for_itterarion():
    "iterasi dalam for"
    for index in range(5):
        if index == 0:
            print("first iteration")
        elif index == 1:
            print("second iteration")
        else:
            print("not first and second")


def for_list_dimension():
    # membaca baris dan kolom, representasi dari tipe data list
    number_grid = [
        [1, 2, 3],  # baris 1
        [4, 5, 6],  # baris 2
        [7, 8, 9],  # baris 3
        [0]         # baris 4
    ]

    # print(number_grid[0][0]) # ambil baris pertama kolom pertamas

    for row in number_grid:
        # ambil semua baris dan kolom / masih dalam bentuk per list / per baris
        print(row)

    for row in number_grid:
        for col in row:
            print(col)  # ambil semua baris untuk di tampilkan satu persatu


if __name__ == "__main__":
    # for_string()
    # for_list()
    # for_list_range()
    # for_itterarion()
    for_list_dimension()
