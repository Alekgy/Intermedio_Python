def divisor(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
        try:
            num = int(input("ingresa un numero: "))
            print(divisor(num))
            print("Termino mi programa")

        except ValueError :
            print("Debes ingresar un numero")

# def run():
#     while True:
#         tr
#             num = int(input('Ingresa un número: '))
#             if num < 0:
#                 raise ValueError
#             print(divisor(num))
#             print("Terminó mi programa")
#             break
#         except ValueError:
#             print("Debes ingresar un entero positivo")

if __name__ == "__main__":
    run()