from classes.AVLTree import AVLTree
from classes.Node import Node
from classes.Room import Room
import time

AMOUNT_OF_PATH = 4
PATH = ["Car", "Bus", "Boat", "Plane"]

def get_data() -> AVLTree:      #Get Data from .txt file
    avl = AVLTree()             #Create AVL Instance
    with open("./Database.txt") as file:
        data = file.read().split('\n')
        if data[-1] == '':      #Delete Last Empty Item
            data.pop()
        for i in data:
            tmp = i.split(',')
            avl.add(Room(int(tmp[0]), tmp[1]))      #Add Room in AVL
    return avl  #Return Instance

def save_data(avl: AVLTree) -> None:    #Save Data into .txt file
    tmp = avl.inorder()     
    with open("./Database.txt", "w") as file:
        string = ''
        for room in tmp:
            string += f'{room.number},{room.passage_path}\n'    #Save as room number,passage path
        file.write(string)

if __name__ == "__main__":
    avl = get_data()
    while 1:
        print("What option you want to choose?")
        print("1.Guest(s) Arrival  2.Manually Add Room(s)  3.Manually Remove Room(s)")
        print("4.Sort Room(s)      5.Find Room             6.Show Empty Room(s) Amount")
        print("                    7.Kill The Program")
        inp = input()               #Input  option
        if len(inp) != 1 or not inp.isnumeric() or int(inp) > 7 or int(inp) < 1:    #Input 
            print("!!-- INVALID INPUT. PLEASE ENTER ONE OF NUMBERS ABOVE. --!")
            continue
        
        if inp == '1':      #INSERT
            guests = []
            print("Enter Number of Guest(s) in each path.")
            all_room = avl.inorder() 

            for i in range(AMOUNT_OF_PATH):     #Get Amount of input on each path 
                number = input(f'Path {PATH[i]}: ')
                if not number.isnumeric():
                    print("Invalid input, set to default 0.")
                    number = '0'

                number = int(number)            
                guests.append(int(number))      #Append amount of a path to guests list

            start_time = time.time()        #Start time
            new_avl = AVLTree()             #Create new instance
            in_hotel_guest = len(all_room)  #Amount of guest that's already in hotel
            loop_limit = max(guests + [in_hotel_guest])    #Loop limit depends on most amount guest in a path
            for i in range(loop_limit):
                #Divide Room in Hotel into 5 rooms set and insert room each path a time
                if i < in_hotel_guest : new_avl.add(Room(i*5+1, all_room.pop(0).passage_path))
                if i < guests[0]: new_avl.add(Room(i*5+2, PATH[0]))
                if i < guests[1]: new_avl.add(Room(i*5+3, PATH[1]))
                if i < guests[2]: new_avl.add(Room(i*5+4, PATH[2]))
                if i < guests[3]: new_avl.add(Room(i*5+5, PATH[3]))
            avl = new_avl
            end_time = time.time()      #End time
            print(f'Elapsed time used: {end_time - start_time:.6f} Seconds')   

        elif inp == '2':    #Manually Add Room
            room_no = input("Enter Room Number you wanna add: ")
            if not room_no.isnumeric() or int(room_no) < 0:
                print("Invalid input, input isn\'t a number.")
                continue
            try: 
                avl.add(Room(int(room_no), 'None'))     #Add Room in Node with None Passage Path
            except Exception as err:    
                print(err)      

        elif inp == '3':    #Manually Remove Room
            room_no = input("Enter Room Number you wanna remove: ")
            if not room_no.isnumeric():
                print("Invalid input, input isn\'t a number.")
                continue
            avl.root, deleted = avl.remove(avl.root, int(room_no))
            if not deleted:
                print(f'Room {room_no} doesn\'t exist to be deleted.')
            else:
                print(f'Deleted room {room_no}.')

        elif inp == '4':    #Sort
            print(f'Our hotel rooms are already sorted.')

        elif inp == '5':    #Find a room
            room_no = input("Enter Room Number you wanna find: ")
            if not room_no.isnumeric():
                print("Invalid input, input isn\'t a number.")
                continue
            room = avl.find(int(room_no))
            if room:
                print(f'Passenger in room {room.number} arrive by path {room.passage_path}.')
            else:
                print(f'Room {room_no} doesn\'t exist.')
        
        elif inp == '6':    #SHOW EMPTY
            print(f"There's {avl.count()} empty room(s)")

        elif inp == '7':    #END Program
            save_data(avl)
            break
        
        print("-----------------------------------\n")