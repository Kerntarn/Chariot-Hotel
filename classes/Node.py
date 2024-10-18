from .Room import Room
class Node:
        def __init__(self, data: Room):
            self.data: Room = data      #Room
            self.left: Node | None = None       
            self.right: Node | None = None
            self.height: int = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):        #Set height base on child node
            a = Node.getHeight(self.left)   
            b = Node.getHeight(self.right) 
            self.height = 1 + max(a,b)
            return self.height

        def getHeight(node) -> int: 
            return -1 if not node else node.height

        def balanceValue(self) -> int:  #GetBalanceFactor
            return Node.getHeight(self.right) - Node.getHeight(self.left)
        
      