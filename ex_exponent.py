# Autho : Salim Suprayogi
# Ref   : freeCodeCamp.org ( youtube )


# print(2**3) # nilai pangkat / pow

def raise_to_power(base_number, pow_number):
    result = 1
    for index in range(pow_number):
        # kurang sempurna, belum nemu caranya biar tisak berwarna kuning
        result = result * base_number
    return result


if __name__ == "__main__":
    print(raise_to_power(2, 3))
