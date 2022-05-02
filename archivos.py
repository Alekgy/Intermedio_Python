from ast import Num


def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["alejandro", "facundo", "miguel", "pepe", "cristian", "rocio"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    pass


def run():
    write()


if __name__ == "__main__":
    run()