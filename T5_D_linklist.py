class dnode :
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None
class dlink_list () :
    def __init__(self):
        self.dll = []
        self.head = None 
        self.prev = None

#//////////////////////////////////////////////////////////////////////////////////
    def append(self , x) :
        if self.head is None :
            self.head = dnode (x)
            return
        c = self.head
        a = dnode(x)
        while c.next :
            c = c.next
        c.next = a
        a.prev = c
#///////////////////////////////////////////////////////////////////////////////////
    def insert_first (self , x) :
        if self.head == None :
            self.head = dnode(x)
        a = dnode(x)
        a.next = self.head
        self.head.prev = a
        self.head = a

#//////////////////////////////////////////////////////////////////////////////////

    def insert_last (self , x) :
        if self.head == None :
            self.head = dnode(x)
        c = self.head
        a = dnode(x)
        while c.next :
            c = c.next
        c.next = a
        a.prev = c
#///////////////////////////////////////////////////////////////////////////

    def insert_befor (self , x , y) :
        if self.head is None :
            print ('list is emputy')
            return
        if self.head.data == x :
            self.insert_first (y)
            return
        c = self.head
        a = dnode (y)
        while c :
            if c.data == x :
                c.prev.next = a
                c.prev = a
                a.next = c
                a.prev = c.prev
                
                return
            c = c.next
        print ('not found')

#//////////////////////////////////////////////////////////////////////////

    def insert_after(self , x , y) :
        if self.head is None :
            print ('list is emputy')
            return
        c = self.head
        a = dnode (y)
        while c :
            if c.data == x :
                a.next = c.next
                if c.next :
                    c.next.prev =a
                c.next = a
                a.prev = c
                return
            c = c.next
        print ('not found')

#///////////////////////////////////////////////////////////////////////////
    def print(self):
        c = self.head
        while c :
            print(c.data  , end='<-->')
            c = c.next
        print('none')

#////////////////////////////////////////////////////////////////////////////

    def del_first (self) :
        if self.head is None :
            print('list is emputy.')
            return
        if self.head.next is None :
            self.head = None
            return
        c = self.head
        self.head = c.next
        del c

#////////////////////////////////////////////////////////////////////////////

    def del_last (self) :
        if self.head is None :
            print ('list is emputy')
        if self.head.next is None :
            self.head = None
            return
        c = self.head
        while c.next :
            c = c.next 
        c.prev.next = None
        del c

#////////////////////////////////////////////////////////////////////////////

    def del_after( self , x) :
        if self.head is None :
            print ('list is emputy')
            return
        c = self.head
        while c.next :
            if c.data == x :
                if c.next :
                    a = c.next
                    c.next = c.next.next
                    if c.next :
                        c.next.prev = c
                    del a
                    return
            c = c.next
        print (f"{x}  :not fond ")
#////////////////////////////////////////////////////////////////////////////

    def del_befor( self , x ) :
            if self.head is None :
                print ('list is emputy')
            if self.head.data == x :
                print ("error")
                return
            if self.head.next.data == x :
                self.del_first()
                return
            c = self.head
            while c.next :
                if c.data == x :
                    a = c.prev
                    c.prev = a.prev
                    a.prev.next = c
                    del a
                    return
                c = c.next
            print (f"{x}  : not found")

#////////////////////////////////////////////////////////////////////////////

    def del_x(self , x ) :
        if self.head is None :
            print('list is emuty')
        if self.head.data == x :
            self.del_first()
            return
        c = self.head
        while c.next :
            if c.data == x :
                c.prev.next = c.next
                if c.next :
                    c.next.prev = c.prev
                del c
                return
            c = c.next
        print(f"{x}   : not font ")

#////////////////////////////////////////////////////////////////////////////

    def del_all (self) :
        while self.head :
            self.del_first ()


#////////////////////////////////////////////////////////////////////////////

s = dlink_list()
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
s.print()
s.insert_after(30 , 80 )
s.print()
s.insert_befor(30 , 80 )
s.print()
s.insert_last(90)
s.print()
s.insert_first(100)
s.print()
s.del_first()
s.print()
s.del_last()
s.print()
s.insert_after(10,30)
s.print()
s.del_after(2)
s.print()
s.del_befor(20)
s.print()
s.del_x(40)
s.print()
s.del_all()
s.print()