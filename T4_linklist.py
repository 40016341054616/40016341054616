class node :
    def __init__(self , Data):
        self.Data =Data
        self.next = None
class linklist () :
    def __init__(self):
        self.head = None
#/////////////////////////////////////////////////////////////////////////////
    def insert (self , data) :
        if self.head is None :
            self.head = node(data)
            return 
        c = self.head
        while c.next :
            c = c.next 
        a = node(data)
        c.next = a 
#////////////////////////////////////////////////////////////////////////////
    def insert_first (self , data) :
        if self.head is None :
            self.head = node (data)
             
        a = node (data)
        a.next = self.head
        self.head = a
#//////////////////////////////////////////////////////////////////////////////
    def insert_last (self , data) :
        if self.head is None :
            self.head = node (data)
        c = self.head
        a = node (data)
        while c.next :
            c = c.next 
        c.next = a
#/////////////////////////////////////////////////////////////////////////////
    def insert_after (self , x , y) :
        if self.head is None :
            print ('list is empty')
            return
        c = self.head
        a = node (y)
        while c :
            if c.Data == x :
                a.next = c.next
                c.next = a
                return
            c = c.next 
        print ('x  not found')
#//////////////////////////////////////////////////////////////////////////
    def insert_befor (self , x , y) :
        if self.head is None :
            print ('list is empty') 
        if self.head.Data == x :
            self.insert_first(y)
            return
        c = self.head 
        a = node (y)
        while c.next :
            if c.next.Data == x :
                a.next = c.next
                c.next = a
                return
            c = c.next
        print ('x not found')
#////////////////////////////////////////////////////////////////////////////////

    def print (self) :
        c = self.head 
        while c  :
            print (c.Data , end='-->')
            c = c.next
        print ('none')

#///////////////////////////////////////////////////////////////////////////////////
    def del_first(self) :
        if self.head is None :
            print ('list is empty')
        a = self.head 
        self.head = a.next
        del a
#///////////////////////////////////////////////////////////////////////////////////

    def del_after (self , x ) :
        if self.head is None :
            print('list is empty')
        c = self.head 
        while c :
            if c.Data == x :
                a = c.next 
                c.next = a.next 
                del a
                self.print()
                return 
            c = c.next
        print ('x not mm found' )

#//////////////////////////////////////////////////////////////////////////////////
    def del_befor(self  , x) :
        if self.head is None :
            print ('list is empty')
            return
        if self.head.Data == x :
            print('error')
            return
        if self.head.next.Data == x :
            self.del_first()
            return
        if self.head.next.next is None :
            print('error')
            return
        c = self.head
        while c.next.next :
            if c.next.next.Data == x :
                a = c.next
                c.next = a.next
                del a
                print('del_befor :')
                
                return
            c = c.next
        print ('x is not found')
#////////////////////////////////////////////////////////////////////////////////
    def del_last (self):
        if self.head is None :
            print ('list is emputy')
            return
        if self.head.next is None :
            self.del_first()
        else :
            c = self.head
            while c.next.next :
                c = c.next
            a = c.next 
            c.next = None
            del a
#//////////////////////////////////////////////////////////////////////////
    def del_x (self ,x ) :
        if self.head is None :
            print ('list is emputy')
            return
        if self.head.Data == x  :
            self.del_first()
            return
        c = self.head
        while c.next :
            if c.next.Data == x :
                a = c.next 
                c.next = a.next 
                del a
                return
            c =c.next
        print('x is not found')

#////////////////////////////////////////////////////////////////////////////
    def del_all(self) :
        while self.head :
            self.del_first()
#////////////////////////////////////////////////////////////////////////////
        

                  
s = linklist()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)   
s.print ()
s.insert_befor (30 , 80)
s.print ()
s.insert_after(30 , 90)
s.print ()
s.del_first()
s.print ()
s.del_after(30)
s.print ()
s.del_befor(80)
s.print ()
s.del_last()
s.print ()
s.del_x(30)
s.print ()
s.del_all()
#s.print()
