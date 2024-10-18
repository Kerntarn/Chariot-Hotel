from .Node import Node
from .Room import Room
class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root
        

    def add(self, data: Room) -> None:          #Add Node
        self.root = AVLTree._add(self.root, data)
    def _add(root: Node, data: Room) -> Node:   #Recursive Add Node
        if not root:        #If visit Empty, Append new Node with Room in data
            return Node(data)

        if data.number < root.data.number:      
            root.left = AVLTree._add(root.left, data)
        elif data.number > root.data.number:
            root.right = AVLTree._add(root.right, data)
        else:
            raise Exception(f"Room {data} already exists.")

        root = AVLTree.balance(root)
        return root

    def find(self, data: int) -> Room:          #Find Node by room number
        node_found: Node = AVLTree._find(self.root, data)
        return node_found.data if node_found else None
    def _find(root: Node, data: int) -> Node:   #Recursive Find Node 
        if root:
            if data > root.data.number:
                return AVLTree._find(root.right, data)
            elif data < root.data.number:
                return AVLTree._find(root.left, data)
            else:
                return root     #Return Found Node
        return None         #Not Found, Return None

    def rotateLeftChild(root: Node) -> Node:    #Rotate Left child up
        left = root.left 
        root.left = left.right
        left.right = root
        root.setHeight()
        left.setHeight()
        return left
    def rotateRightChild(root: Node) -> Node:   #Rotate Right child up
        right = root.right  
        root.right = right.left
        right.left = root
        root.setHeight()
        right.setHeight()
        return right 

    def printTree(self) -> None:        #Print Tree Horizontally
        AVLTree._printTree(self.root)
        print()
    def _printTree(node: Node, level: int = 0) -> None:
        if node:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

    def inorder(self) -> list[Room]:        #Return List of Room
        return AVLTree._inorder(self.root)
    def _inorder(root: Node) -> list[Room]: 
        if root:
            tmp = []
            tmp += AVLTree._inorder(root.left)
            tmp.append(root.data)
            tmp += AVLTree._inorder(root.right)
            return tmp
        return []
    
    def count(self):        #Return Empty Room Amount
        max_num, sum_of_room = AVLTree._count(self.root, 0)
        return max_num - sum_of_room
    def _count(root: Node, max: int) -> tuple:  #Return max room number and amount of occupied room
        if root:
            if root.data.number > max:      #Compare max value with room number
                max = root.data.number
            s = 0           #Amount of room
            left = AVLTree._count(root.left, max)       
            s += left[1]
            right = AVLTree._count(root.right, max)
            s += right[1]

            max = left[0] if left[0] > max else max
            max = right[0] if right[0] > max else max

            if root.data.passage_path == 'None':    #None mean it's empty room
                return max, s
            return max, s + 1
        return max, 0
    
    def remove(self, root: Node, data: int) -> tuple[Node, bool]:   #remove node by inorder successor
        if not root:
            return None, False
        
        if data < root.data.number:
            root.left, deleted = self.remove(root.left, data)
        elif data > root.data.number:
            root.right, deleted = self.remove(root.right, data)

        else:
            deleted = True
            
            #none or 1 child case
            if not root.left:
                return root.right, deleted
            elif not root.right:
                return root.left, deleted
            
            #2 childs case
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            
            root.data = tmp.data        #Swap data in Node
            root.right, _ = self.remove(root.right, tmp.data.number)    #dive down to remove inorder successor

        root = AVLTree.balance(root)

        return root, deleted
    
    def balance(root: Node) -> Node:    #Balance AVL Node
        root.setHeight()
        diff = root.balanceValue()
        if diff > 1:
            if root.right.balanceValue() < 0:
                root.right = AVLTree.rotateLeftChild(root.right)
            root = AVLTree.rotateRightChild(root)
        elif diff < -1:
            if root.left.balanceValue() > 0:
                root.left = AVLTree.rotateRightChild(root.left)
            root = AVLTree.rotateLeftChild(root)

        root.setHeight()
        return root