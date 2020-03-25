# Autho : Salim Suprayogi
# Ref   : freeCodeCamp.org ( youtube )


def say_hi(nama, age):
    print("Hello " + nama + ", you are " + str(age))


def cube(num):
    "return statement // give me some information"
    return num*num*num


def max_num(num1, num2, num3):
    "if statement and camparisons"
    # mencari nilai maksimum dari num1 num2 num3
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


if __name__ == "__main__":
    # def say_hi()
    """
    say_hi("Mike", 35)
    say_hi("Steve", 34)
    """

    # def cube
    """
    # print(cube(3))  # hasilnya none // jika tanpa return
    result = cube(4)
    print(result)
    """
    
    # def max_num
    """
    print(max_num(3, 4, 5)) # num3 max_num
    print(max_num(3, 40, 5)) # num2 max_num
    print(max_num(300, 4, 5)) # num1 max_num
    """
