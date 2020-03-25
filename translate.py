# Author    : Salim Suprayogi
# Ref       : freeCodeCamp.org ( youtube )


def translate(phrase):
    "mengganti huruf tertentu"
    translation = ""
    # loop
    for letter in phrase:
        # cek apakah ada huruf AEIOUaeiou
        # jika ada ganti dengan huruf "g"
        if letter.lower() in "aeiou":
            # ubah phrase menjadi huruf kecil
            if letter.isupper():
                # cek, apakah phrase huruf kapital
                # jika iya, ganti dengan "G" kapital
                translation = translation + "G"
            else:
                # jika bukan huruf kapital
                # ganti dengan "g" kecil
                translation = translation + "g"
        else:
            # jika tidak ada huruf AEIOUaeiou, tampilkan phrase
            translation = translation + letter
    return translation


if __name__ == "__main__":
    print(translate(input("Enter a phrase: ")))
