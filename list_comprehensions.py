# def run():
#     # squares = []
#     # for i in range(1, 101):
#     #     if i % 3 != 0:
#     #         squares.append(i**2)

#     squares = [i**2 for i in range(1, 101) if i % 3 != 0]

#     print(squares)


# if __name__ == "__main__":
#     run()

    #reto:

# def run():

#     squares = [i for i in range (1, 100000) if i % 36 == 0]
    
    
#     print(squares)


    


# if __name__ == "__main__":
#     run()

#reto 2 
import numbers


def run():
    # numbers = []
    # for i in range(0,6):
    #         numbers.append(i**2)

    my_list = [1, 2, 3, 4, 5]

    numbers = [i**2 for i in my_list]

    print(numbers)

if __name__ == "__main__":
    run()