from .Node import Node
from .Room import Room
class AVLTree:
    def __init__(self, root: Node = None):
        self.root = root
        

    def add(self, data: Room) -> None:
        self.root = AVLTree._add(self.root, data)
    def _add(root: Node, data: Room) -> Node: 
        if not root:
            return Node(data)

        if data.number < root.data.number:
            root.left = AVLTree._add(root.left, data)
        elif data.number > root.data.number:
            root.right = AVLTree._add(root.right, data)
        else:
            return root

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
    
    def remove(self, data: int) -> None:
        self.root = AVLTree._remove(self.root)
    def _remove(root: Node, data: int) -> Node:
        ######################
        return root

    def find(self, data: int) -> Room:
        node_found: Node = AVLTree._find(self.root, data)
        return node_found.data
    def _find(root: Node, data: int) -> Node:
        ##################
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

    def printTree(self) -> None:
        AVLTree._printTree(self.root)
        print()
    def _printTree(node: Node, level: int = 0) -> None:
        if node:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

    def inorder(self) -> list[Room]:
        return AVLTree._inorder(self.root)
    def _inorder(root: Node) -> list[Room]:
        if root:
            tmp = []
            tmp += AVLTree._inorder(root.left)
            tmp.append(root.data)
            tmp += AVLTree._inorder(root.right)
            return tmp
        return []