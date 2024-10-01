from classes.AVLTree import AVLTree
from classes.Node import Node
from classes.Room import Room


AMOUNT_OF_PATH = 4

def get_data() -> AVLTree:
    return AVLTree()

def insert_guests(avl: AVLTree, guests: list[int]):
    pass


if __name__ == "__main__":
    avl = get_data()
    while 1:
        print("What option you want to choose?")
        print("1.Guest(s) Arrival  2.Manually Add Room(s)  3.Manually Remove Room(s)")
        print("4.Sort Room(s)      5.Find Room             6.Show Empty Room(s)")
        print("                    7.Kill The Program")
        inp = input()
        if len(inp) != 1 or not inp.isnumeric():
            print("!!-- INVALID INPUT. PLEASE ENTER ONE OF NUMBERS ABOVE. --!")
            continue
        #read data from .json
        #make instance

        if inp == '1':
            guests = []
            print("Enter Number of Guest(s) in each path")
            for i in range(AMOUNT_OF_PATH):
                number = input(f'path {i+1}: ')
                if not number.isnumeric():
                    print("Invalid input, set to default 0.")
                    number = '0'
                guests.append(int(number))
            insert_guests(avl, guests)
            avl.printTree()
            
        elif inp == '2':
            pass
        elif inp == '3':
            pass
        elif inp == '4':
            pass
        elif inp == '5':
            pass
        elif inp == '6':
            pass
        elif inp == '7':
            #save
            break