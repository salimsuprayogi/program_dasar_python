# Author    : Salim Suprayogi
# Ref       : freeCodeCamp.org ( youtube )


def guessing_game():
    # nama fungsi guessing_game()
    "guessing game play / permainan tebak-tebakan."

    secret_word = "apel"
    # jawaban yang benar.

    guess = ""
    # penyimpanan sementara user.
    guess_count = 0
    # add nilai dimulai dari 0.
    guess_limit = 3
    # limit berapa kali user bisa input, ex [3 kali].
    out_of_guesses = False

    while guess != secret_word and not(out_of_guesses):
        # kondisi ini akan melakukan perulangan jika kondisinya benar/true, berhenti jika salah/false,
        # selama "guest" tidak sama dengan "secret_word",
        # maka akan melakukan perulangan berulangkali,
        # jika kondisinya benar (nilai "guess" sama dengan nilai "secret_word"), perulangan akan berhenti.

        if guess_count < guess_limit:
            # cek, apakah "guess_count" lebih kecil dari "guess_limit",
            # jika iya, lakukan perulangan dimulai dari 0 (guess_count),
            # jika "guess-count" lebih besar dari "guess_limit", maka kondisi "else" yang akan di jalankan.

            print("kata kunci-nya adalah nama buah cinta")

            user = input("Enter guess: ")
            # input user.
            guess = user.lower()
            # simpan input user dengan fungsi lower(), agar menjadi huruf kecil

            guess_count += 1
            # increment,
            # agar nilai "guess_count" bertambah menjadi 1,2,3,4,....,
            # ketika sampai pada 4, tidak akan menjalankan kondisi ini, karena pengecekan menggunakan (<) lebih kecil dari,
            # yang di jalankan adalah "else".
        else:
            # jika 3 kali input salah,
            # maka akan menjalankan kondisi ini.
            out_of_guesses = True
            # kemudian variabel "out_of_guesses" memiliki nilai True,
            # kemudian menggunakan fungsi "not" supaya nilainya False,
            # dalam artian "out_of_gusess" memiliki nilai sama sama false dan perulangan berhenti karena benar / True
            # dan cek "guess" tidak sama dengan "secret_word" -> iya, artinya True
            # jadi "while" ada dua kondisi yang menyatakan benar / True, maka perulangan akan berhenti(break)
            # lalu jalankan kondisi "if out_of_guesses".

    # melakukan pengecekan perulangan pada kondisi "while".
    if out_of_guesses:
        # jika 3 kali menjawab salah akan menjalankan pengecekan ini
        print("---Out of Guesses, YOU LOSE !!!---")
    else:
        print("---YOU WIN !!!---")
        # jika jawaban benar/ "!=" dan "out_of_guesses" benar/True


if __name__ == "__main__":
    guessing_game()
