class Node :
    def __init__(self , data):
        self.data = data 
        self.prev = None
        self.next = None

class Dlinklist :
    def __init__(self):
        self.head = None

    #/////////////////////////////////////////////////////////////////////////////////
    def pop_last (self):
        if self.head is None :
            print ("list is empty.")
            return 
        if self.head.next == None :
            a = self.head.data
            self.head = None
            return a
        c = self.head
        while c.next :
            c = c.next
        a = c.data
        if c.prev :
            c.prev.next = None
        else :
            self.head = None 
        del  c
        return a
    #/////////////////////////////////////////////////////////////////////////////////////
    def zarb (self):
        if self.head is None :
            print("list is emputy.")
            return 
        c = self.head
        a = 1
        while c :
            a *= c.data
            c = c.next
        print ("zarb list = " , a)

#//////////////////////////////////////////////////////////////////////////////////////
    def max_ (self):
        max = 0
        index = 0
        max_index = 0
        if self.head is None :
            print("list is emputy")
            return
        if self.head.next is None :
            max = self.head.data 
            print("max = " , max , "index = " ,max_index)
            return 
        c = self.head
        while c :
            if max < c.data :
                max = c.data 
                max_index = index
            c = c.next
            index += 1
        print ( "max = ", max , "max_index = " , max_index)

#????//////////////////////////////////////////////////////////////////////////////////
    def del_after (self , x ) :
        if self.head is None :
            print ("list is emputy")
            return
        c = self.head 
        while c :
            if c.data == x :
                if c.next :
                    a = c.next
                    c.next = a.next 
                    if a.next :
                        a.next.prev = c
                    del a
                    return True
                print (f"next is {x} data not found.")
                return True
            c = c.next 
        print (f"data {x} nut found")
        return False
    
#///////////////////////////////////////////////////////////////////////////////

    def insert_after (self , x ,y ):
        if self.head is None :
            print ("list is emuty")
            return
        c = self.head 
        a = Node(y)
        while c.next :
            if c.data == x :
                if c.next :
                    c.next.prev = a
                    a.next = c.next 
                    c.next = a
                    a.prev = c
                else :
                    c.next = a
                    a.prev = c
                return True
            c = c.next
        print (f"data {x} not found")
        return False

#//////////////////////////////////////////////////////////////////////////////////
    def insert_befor(self , x ,y) :
        if self.head is None :
            print("list is emputy")
            return
        if self.head.data == x :
            print("error")
            return
        a = Node(y)
        c = self.head
        while c :
            if c.data == x :
                a.next = c
                a.prev = c.prev
                if c.prev :
                    c.prev.next = a
                else :
                    self.head = a
                c.prev = a
                return True
            c = c.next
        print(f"مقدار {x} در لیست یافت نشد.")    
        return False    
#/////////////////////////////////////////////////////////////////////////////////////
    def display (self) :
        c = self.head
        elements = []
        while c :
            elements.append(str(c.data))
            c = c.next
        elements.reverse()
        print ("<-->" .join(elements) )

#////////////////////////////////////////////////////////////////////////////////////
    def prime (self) :
        A = []
        c = self.head
        curent = 0
        while c :
            if c.data >= 2 :
                for i in range ( 2 , int(c.data/2+1)) :
                    if c.data % i == 0 :
                        curent += 1
                if curent < 1 :
                    A.append(c.data)
            curent = 0
            c = c.next
        print ("is prime = ")
        print (A)

#/////////////////////////////////////////////////////////////////////////////////////////////////
    def sum_(self) :
        s = 0
        c = self.head
        while c :
            s += c.data
            c = c.next
        print ("sum = " , s)

#//////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////

class stack :
    def __init__(self , limit = 10):
        self.dll = Dlinklist()
        self.limit = limit 
        self.size = 0
#////////////////////////////////////////////////////////////////////////////////////////////////////
    def push (self , data) :
        if self.size >= self.limit :
            print ("stak is full")
            return
        a = Node (data)
        if self.dll.head is None :
            self.dll.head = a
        else :  
            c = self.dll.head
            while c.next :
                c = c.next
            c.next = a
            a.prev = c
        self.size += 1
        print(f"data {data} is add.")
        self._print_useng()

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def pop (self) :
        if self.is_empty() :
            print ("stack is empty")
            return None
        value = self.dll.pop_last()
        if value is not None :
            self.size -= 1
            print (f"data {value} is pop ")
            self._print_useng()
        return value

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def peek(self) :
        if self.dll is None :
            print ("stack is empty")
            return
        c = self.dll.head
        while c.next :
            c = c.next
        return c.data

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def is_empty(self) :
        return self.size == 0 
#//////////////////////////////////////////////////////////////////////////////////////////////////////
    def is_full (self) :
        return self.size == self.limit
#/////////////////////////////////////////////////////////////////////////////////////////////////////
    def curent_size (self ):
        return self.size
    
#////////////////////////////////////////////////////////////////////////////////////////////////
    def del_after(self , x ) :
        if self.is_empty () :
            print ("stack is empty .")
            return None
        A = self.dll.del_after(x)
        if A :
            self.size -= 1
            print (f"data after {x} is del")
            self._print_useng ()

#////////////////////////////////////////////////////////////////////////////////////////////
    def insert_befor (self , x ,y):
        if self.size >= self.limit :
            print("error full stack")
            return
        B = self.dll.insert_befor(x , y)
        if B :
            self.size += 1
            print (f"data {y} befor is data {x} add")
            self._print_useng()

#/////////////////////////////////////////////////////////////////////////////////////////////////
    def insert_after(self , x ,y) :
        if self.size == self.limit :
            print (f"error full stack")
            return 
        C = self.dll.insert_after(x ,y)
        if C :
            self.size += 1
            print(f"data {y} after is data {x} add")
            self._print_useng()

#/////////////////////////////////////////////////////////////////////////////////////////////////
    def print_stack(self):
        c = self.dll.head
        while c.next :
            c = c.next
        print ("stack = ")
        while c :
            print(c.data)
            c = c.prev

#////////////////////////////////////////////////////////////////////////////////////////////////
    def sum_ (self ) :
        self.dll.sum_()
#////////////////////////////////////////////////////////////////////////////////////////////////
    def zarb (self):
        self.dll.zarb()
#///////////////////////////////////////////////////////////////////////////////////////////////
    def max_(self) :
        self.dll.max_()
#///////////////////////////////////////////////////////////////////////////////////////////////
    def prime(self) :
        self.dll.prime()
#////////////////////////////////////////////////////////////////////////////////////////////////
    def display (self) :
        self.dll.display()
#//////////////////////////////////////////////////////////////////////////////////////////////////
    def _print_useng(self) :
        print (f"فضای استفاده شده : {self.size} از {self.limit} | فضای خالی : {self.limit - self.size}")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////



s = stack (limit=10)
for i in [32 ,5, 65, 21 , 57 , 90 , 86 , 51 , 93 ,1 , 13]:
    if s.is_full():
        break
    s.push(i)
#s.print_stack()
s.display()