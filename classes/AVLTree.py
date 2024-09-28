from Node import Node
from Room import Room
class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root

    def add(self, data: Room):
        self.root = AVLTree._add(self.root, data)

    def _add(root: Node, data: Room) -> Node: 
        if not root:
            return Node(data)

        if data.number < root.data.number:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()
        #rebalance
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

    def rotateLeftChild(root: Node) -> Node:
        left = root.left 
        root.left = left.right
        left.right = root
        root.setHeight()
        left.setHeight()
        return left

    def rotateRightChild(root: Node) -> Node:
        right = root.right
        root.right = right.left
        right.left = root
        root.setHeight()
        right.setHeight()
        return right 

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node: Node, level: int = 0):
        if node:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl = AVLTree()
inp = input('input: ').split(' ')
for i in inp:
    room = Room(int(i), 'tuk tuk')
    avl.add(room)
    avl.printTree()