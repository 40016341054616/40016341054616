class stack :
    def __init__ (self,limit=10):
        self.st=[]
        self.limit=limit
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def push (self,x ) :
            if len(self.st) >= self.limit :
                 print ("stack is full")
                 return -1
            self.st.append(x)

       # self.st.append(x)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def pop (self) :
        if len (self.st)==0 :
            print("stack is empty")
            return -1
        return self.st.pop()
        
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def peek(self):
        if len (self.st)==0 :
            print("stack is empty")
            return -1
        return self.st[-1]
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def show (self):
        print (self.st)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def display (self):
        print ("stack ; " )
        for i in reversed(self.st) :
            print (  i)
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def find (self , f ):
        found = False
        for i in range(len (self.st)) :
            if self.st[i] == f :
                print(f"مقدار {f} در ایندیکس {i} می باشد.")
                found=True
        if not found :
            print("not found")
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def find_1(self , f , x) :
        for i in range (len (self.st)):
            if self.st [i] == f :
                self.st[i] = x
                return
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def find_2(self , f , x) :
        for i in range(len(self.st)-1,0,-1):
            if self.st[i] == f :
                self.st[i] = x
                return

    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
s=stack()
s.push(7)
s.push(7)
s.push(7)
s.push(7)
s.push(7)  
s.display()
s.pop()
s.show()
s.display()  
s.find(7)  
#s.find_1(5 , 7)  
s.find_2(7 , 8)
s.show()
s.find_1(7 , 8)
s.show()
print (s.peek())