class treenode :
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left  = None

class tree  :
    def __init__(self):
        self.root = None
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////////\\\\\\\\\\ 
    #اضافه کردن
    def insert ( self , root , data) :
        if root is None :
            return treenode(data)
        if data < root.data :
            root.left = self.insert (root.left ,data)
        else :
            root.right = self.insert (root.right , data)
        return root

#\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\\//\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
    #پیمایش درخت از چپ ->ریشه -> راست
    def inorder_traversal(  self ,root) :
        if not root :
            return []
        return self.inorder_traversal(root.left) + [root.data] + self.inorder_traversal(root.right)
    
#/\/\/\/\/\/\/\//\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\//\//\/\/\/\//\\/\/\/\/\/\/\/\/\/
    def inorder_traversel_print(self ,root ) :
        if root :
            self.inorder_traversel_print(root.left)
            print (root.data)
            self.inorder_traversel_print(root.right)

#/////////////////////////////////////////////////////////////////////////////////////////////////////
    #پیمایش درخت از چپ ->راست ->ریشه
    def postorder_traversal(self , root) :
        if not root :
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.data] 

#////////////////////////////////////////////////////////////////////////////////
    def postorder_traversal_print(self , root) :
        if root :
            self.postorder_traversal_print(root.left)
            self.postorder_traversal_print(root.right)
            print ( root.data)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
    #پیمایش درخت از ریشه-<چپ->راست
    def preorder_traversal(self , root) :
        if not root :
            return []
        return    [root.data] + self.inorder_traversal(root.left) + self.prerder_traversal(root.right)
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def preorder_traversal_print(self , root) :
        if root :
            print (root.data)
            self.prerder_traversel_print(root.left)
            self.prerder_traversel_print(root.right)
            

#///////////////////////////////////////////////////////////////////////////////////////////////////
    #متد حاصل جمع تمام مقادیر گره ها
    def sum_v_n(self , root):
        if root is None:
            return 0
        return  root.data + self.sum_v_n(root.left) + self.sum_v_n(root.right)
    
#/////////////////////////////////////////////////////////////////////////////////////////
    #متد محاسبه ارتفاع درخت باینری
    def  height_tree(self ,root ) :
        if root == None :
            return 0
        return 1 + max(self.height_tree(root.left) , self.height_tree(root.right))
    
#///////////////////////////////////////////////////////////////////////////////////////////
    #محاسبه تعداد برگهای درخت
    def  count_leaves(self , root) :
        if root is None :
            return 0
        if root.left  is  None  and  root.right is None :
            return 1
        return self.count_leaves(root.left) + self.count_leaves(root.right)
    
#//////////////////////////////////////////////////////////////////////////////////////////////////
    #محاسبه تعداد گره های درخت
    def count_Node (self , root ) :
        if root is None :
            return 0
        return 1 + self.count_Node(root.left) + self.count_Node(root.right)
    
#///////////////////////////////////////////////////////////////////////////////////////////////////
    #محاسبه گره های درجه 1
    def C_1D(self , root ):
        if root is None :
            return 0
        if root.left == None and root.right is not None :
            return 1 + self.C_1D(root.right)
        if root.right == None and root.left is not None :
            return 1 + self.C_1D(root.left)
        return self.C_1D(root.left) + self.C_1D(root.right)
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #محاسبه گره های درجه 2
    def C_2D(self , root ):
        if root is None :
            return 0
        if root.right is not None and root.left == None:
            return  self.C_2D(root.right)
        if root.left is not None and root.right == None:
            return  self.C_2D(root.left)
        if root.left is None and root.right is None :
            return 0
        return 1 + self.C_2D(root.left) + self.C_2D(root.right)
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def search(self , root , target) :
        if root is None :
            return False
        if root.data == target :
            return True
        return self.search(root.left , target) or self.search(root.right , target)
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def max_tree(self , root) :
        if root is None :
            return float ('-inf')
        return max (self.max_tree(root.left) , self.max_tree(root.right) , root.data)
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def min_tree(self , root) :
        if root is None :
            return float ('inf')
        return min (self.min_tree(root.left) , self.min_tree(root.right) , root.data)
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #ساخت درخت با preorder , inorder 
    def build_tree(self , preorder , inorder) :
        if not preorder or not inorder :
            return None
        val = preorder[0]
        index = inorder.index(val)
        n = treenode(val)
        n.left  = self.build_tree(preorder[1 : 1 + index] , inorder [ : index])
        n.right = self.build_tree(preorder[1 + index : ] , inorder[1 + index : ])

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #تشخیص درخت متقارن
    def is_symmetric(self, root, left=None, right=None):
        
        if root is None:
            return True
        if root is not None and root.left is None and root.right is None:
            return True
        if root is not None and root.left is None and root.right is not None :
            return False
        if root is not None and root.left is not None and root.right is None :
            return False
        if left.val != right.val:
            return False
        return (self.is_symmetric(root, left.left, right.right) and self.is_symmetric(root, left.right, right.left))
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #معکوس کردن
    def inv_tree( self , root) :
        if not root :
            return None
        root.left , root.right = root.right , root.left
        self.inv_tree(root.left)
        self.inv_tree(root.right)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

r = tree()
for i in [6 , 8 ,87,45,9,32 ,90 ,34 ,1 ,87] :
    r.root = r.insert (r.root, i )
print ("inorder_traversal = " , r.inorder_traversal(r.root)) 
r.inorder_traversel_print(r.root)
#print ( "sum_v_n = " , r.sum_v_n(r.root)) 
#print ( "count_leaves = " , r.count_leaves(r.root))
#print("height_tree = " , r.height_tree(r.root))
print ("postorder_traversal =  " , r.postorder_traversal(r.root))
r.postorder_traversal_print(r.root)