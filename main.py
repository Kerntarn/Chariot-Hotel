from classes.AVLTree import AVLTree
from classes.Node import Node
from classes.Room import Room


AMOUNT_OF_PATH = 4
#room_no,path
def get_data() -> AVLTree:
    avl = AVLTree()
    with open("./Database.txt") as file:
        data = file.read().split('\n')
        if data[-1] == '':
            data.pop()
        print(data)
        for i in data:
            tmp = i.split(',')
            avl.add(Room(int(tmp[0]), tmp[1]))
    return avl

def save_data(avl: AVLTree) -> None:
    #####
    tmp = avl.inorder()
    with open("./Database.txt", "w") as file:
        string = ''
        for room in tmp:
            string += f'{room.number},{room.passage_path}\n'
        file.write(string)

0
def insert_guests(avl: AVLTree, guests: list[int]):
    ##############
    pass

if __name__ == "__main__":
    avl = get_data()
    while 1:
        print("What option you want to choose?")
        print("1.Guest(s) Arrival  2.Manually Add Room(s)  3.Manually Remove Room(s)")
        print("4.Sort Room(s)      5.Find Room             6.Show Empty Room(s) Amount")
        print("                    7.Kill The Program")
        inp = input()
        if len(inp) != 1 or not inp.isnumeric():
            print("!!-- INVALID INPUT. PLEASE ENTER ONE OF NUMBERS ABOVE. --!")
            continue

        if inp == '1':
            guests = []
            print("Enter Number of Guest(s) in each path.")
            for i in range(AMOUNT_OF_PATH):
                number = input(f'Path {i+1}: ')
                if not number.isnumeric():
                    print("Invalid input, set to default 0.")
                    number = '0'
                guests.append(int(number))
            insert_guests(avl, guests)
            print(avl.inorder())
            
        elif inp == '2':
            room_no = input("Enter Room Number you wanna add: ")
            if not room_no.isnumeric():
                print("Invalid input, input isn\'t a number.")
                continue
            if 0: ########### room exist
                print(f"Room {room_no} already exists.")
                continue
            avl.add(Room(int(room_no), 'None'))

        elif inp == '3':
            room_no = input("Enter Room Number you wanna remove: ")
            if not room_no.isnumeric():
                print("Invalid input, input isn\'t a number.")
                continue
            avl.remove(int(room_no))
        elif inp == '4':
            pass
        elif inp == '5':
            room_no = input("Enter Room Number you wanna find: ")
            if not room_no.isnumeric():
                print("Invalid input, input isn\'t a number.")
                continue
            room = avl.find()
            if room:
                print(f'Passenger in room {room.number} arrive by path {room.passage_path}.')
            else:
                print(f'Room {room_no} doesn\'t exist.')
        elif inp == '6':
            print(f"There's {avl.count_empty()} empty room(s)")
        elif inp == '7':
            save_data(avl)
            break