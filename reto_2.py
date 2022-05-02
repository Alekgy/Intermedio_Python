def run():
    name_1 = input("cual es tu nombre?: ")
    age_1 = input("cual es tu edad?: ")
    subjet_1 = name_1 + age_1 
    name_2 = input("escoje otro nombre: ")
    age_2 = input("escoje su edad: ")
    subjet_2 = name_2 + age_2

    if age_1 > age_2:
        print(name_1 + " es mayor que " + name_2)
    elif age_1 < age_2:
        print(name_2 + " es mayor que " + name_1)
    else:
        print(name_1 + " y " +name_2 + " son de la misma edad")


if __name__ == "__main__":
    run()