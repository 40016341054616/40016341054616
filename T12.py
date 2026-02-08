#کلاس استک الویت دار
class stack :
    def __init__(self , limit = 10):
        self.stak = [] 
        self.limit = limit
    def push (self , data ) :
        if len(self.stak) >= self.limit :
            print ("پشته پر است.")
            return
        self.stak.append(data)

#/////////////////////////////////////////////////////////////////////////////////////
    def pop (self) :
        if self.stak is None :
            print ("پشته خالی است")
            return
        for i in range (len(self.stak) -1 ,-1 ,-1) :
            if self.stak[i] % 2 == 0 :
                return self.stak.pop(i) , i
            
#//////////////////////////////////////////////////////////////////////////////////////
    def display (self)  :
        for i in range (len(self.stak) -1 ,-1 ,-1) :
            if self.stak[i]  % 2 == 0 :
                print(self.stak[i] ,"  index : ", i )
        for j in range (len(self.stak) -1 ,-1 ,-1) :
            if self.stak[j]  % 2 != 0 :
                print (self.stak[j] , "  index : ", j) 
#///////////////////////////////////////////////////////////////////////////////////////
    def count_data (self) :
        if not self.stak :
            print ("stack  is empty")
            return 
        count1 = 0
        max1 = 0
        for i in range(len(self.stak)) :
            for j in range(len(self.stak)) :
                if self.stak[i] == self.stak[j] :
                    count1 += 1
            if count1 > max1 :
                max1 = count1
                m = self.stak[i]
            count1 = 0
        print ("max1 = " , max1 , " ; " , m)



    def count_ (self) :
        if not self.stak :
            print ("stack is empyt")
            return None
        count_even = 0
        count_odd = 0
        for i in range (len (self.stak)) :
            if  self.stak[i] % 2 == 0 :
                count_even += 1
            elif  self.stak[i] % 2 != 0 :
                count_odd += 1
            
        print ("count_even = " , count_even)
        print ("count_odd = " , count_odd)

#/////////////////////////////////////////////////////////////////////////////////////////
    def peek (self) :
        if self.stak is None :
            print ("stack is empty")
            return None
        for i in range(len (self.stak) -1 , -1 , -1 ) :
            if self.stak[i] % 2 == 0 :
                return self.stak [i]


        
p = stack ()
for i in  [1 ,4 ,6 , 4,6 ,7 , 6 ,6 ,8 ,4 , 76 , 14] :
    p.push(i)
p.display()
print (p.pop())
p.count_()
print (p.peek())
p.count_data()