class treenode :
    def __init__(self , data):
        self.data = data 
        self.left = None
        self.right= None
class Bst :
    def __init__(self):
        self.root = None
#////////////////////////////////////////////////////////////////////////////////////
    def insert(self , value) :
        def _insert(node , value) :
            if node is None :
                return treenode (value) 
            if value == node.data :
                print('error == **')
                return node 
            if value < node.data :
                if node.left is None or (node.left is None and node.left.right is None):
                    node.left = _insert(node.left , value)
                else :
                    print("error darajeh 2 ")
            else :
                if node.right is None or (node.right.left is None and node.right.right is None):
                    node.right = _insert(node.right , value)
                else :
                    print ("error darajeh 2 ")
            return node
        self.root = _insert(self.root , value)

#//////////////////////////////////////////////////////////////////////////////////////
    def find_Bs(self , root , target):
        
        if root is None :
            return False
        if root.data == target :
            return True
        if root.data > target :
            return self.find_Bs(root.left)
        if root.data < target :
            return self.find_Bs(root.right)

#///////////////////////////////////////////////////////////////////////////////////////////

    def lista (self , values) :
        for i in values :
            self.insert(i)
#//////////////////////////////////////////////////////////////////////////////////
    def show (self) :
        def _inorder(node):
            if node :
                _inorder(node.left)
                print(node.data , end="  ")
                _inorder(node.right)
        _inorder(self.root)
        print()
#/////////////////////////////////////////////////////////////////////////////////////////

bst = Bst()
bst.lista([50 ,63,78 ,65,12,3,25])
bst.show()
bst.insert(100)
bst.show()
bst.find_Bs(63)