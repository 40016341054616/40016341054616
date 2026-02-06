class queue:
    def __init__(self, max=10):
        self.list = [None]*max
        self.front =-1
        self.rear = -1
    def insert (self , x):
        if self.rear >= len(self.list)-1:
            print('qeue is full')
            return -1
        self.rear +=1
        self.list[self.rear] = x
        if self.rear == 0 and self.front==-1:
            self.front+=1
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ll\\\\\\\\\
    def del_queue(self) :
        if self.rear == -1:
            print ('qeue is empty')
            return -1
        if self.front > self.rear :
             print ('qeue is empty')
             return -1
        k = self.list[self.front]
        self.front += 1
        return k

      
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def display (self) :
        print ('queue : ')
        for i in range(self.front , self.rear+1):
            print (self.list[i])
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def show(self):
        print (self.list[self.front : self.rear+1]) 
                   
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
s = queue ()
s.insert(9)
s.insert(8)
s.insert(7)
s.insert(6)
s.insert(5)
s.insert(4)
s.display()
print (s.del_queue())
s.display()
s.show()
print (s.del_queue())
s.show()

        