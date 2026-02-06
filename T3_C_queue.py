class C_queue():
    def __init__(self , max):
        self.list=[None]*max
        self.fornt = -1
        self.rear  = -1
    def insert (self , x):
        if self.fornt == -1 :
             self.list[0] = x
             self.fornt = 0
             self.rear  = 0
             return 
        if (self.rear+1)%(len(self.list))==self.fornt :
            print ('queue is full')
            return
        self.rear = (self.rear+1)%(len(self.list))
        self.list[self.rear] = x
#//////////////////////////////////////////////////////////////////
    def del_q(self) :
        if self.fornt == -1 : 
            print ('queue is full')
            return
        if self.fornt == self.rear :
            k = self.list[self.fornt]
            self.fornt = -1
            self.rear  = -1
            return k
        k = self.list[self.fornt]
        self.fornt = (self.fornt+1) % (len(self.list))
        return k
 #//////////////////////////////////////////////////////////////////
    def show(self) :
        print(self.list[self.fornt : self.rear+1])

#///////////////////////////////////////////////////////////////////

    def show_valid(self) :
        if self.rear >= self.fornt :
            for i in range (self.fornt , self.rear + 1) :
                print (self.list[i])
        else :
            for i in range (self.fornt , len(self.list , 1)) :
                print (self.list[i])
            for i in range (self.rear +1) :
                print (self.list[i])
#///////////////////////////////////////////////////////////////////

    def show_invalid(self) :
        if self.rear >= self.fornt :
            for i in range (self.rear+1 , len(self.list ) , 1):
                print (self.list[i])
            for i in range (self.fornt) :
                print (self.list[i])
#///////////////////////////////////////////////////////////////////
    def find (self , x) :
        for i in range (len(self.list)) :
            if self.list[i] == x :
                return i
        print ('not found')
#///////////////////////////////////////////////////////////////////

    def replace (self , x , y) :
        for i in range (len (self.list)) :
            if self.list[i] == x :
                self.list[i] = y

#///////////////////////////////////////////////////////////////////
s = C_queue(5)
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)
print(s.list)
s.del_q()
s.show ()
s.show_valid()