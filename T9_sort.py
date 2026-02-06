def sort_1(a ) :
    s = len(a)
    B = [None]*s
    for i in range( s) :
        min = a[0]
        k = 0
        for j in range(1 , s) :
            if a[j] > min :
                min = a[j] 
                k = j
        B[i] = min
        a[k] = float('-inf')
    return B

A = [2,3,54,60,22,55,32,55,43]
m = sort_1(A )
print ( 'sotr_1         : ',m)

#///////////////////////////////////////////////////////////////////////////////////////

def bubble(a):
    s  = len(a)
    for i in range (s - 1):
        for j in range(s - 1):
            if a[j] < a[j+1] :
                a[j] , a[j+1] = a[j+1] , a[j]
    return a
q = [9,56,4,32,35,70,34,21,35]
n = bubble( q)
print('bebble sort    : ',n)

#///////////////////////////////////////////////////////////////////////////////////

def selection( A):
    for i in range(len(A) - 1) :
        min = A[i]
        k = i
        for j in range(i , len(A)) :
            if A[j] > min :
                min = A[j]
                k = j
        A[i] , A[k] = A[k] , A [i]
    return A
s = [10,5,80,4,8,1,2,7,11,6,3,9]
B = selection(s)
print( 'selection sort : ',B)

#/////////////////////////////////////////////////////////////////////////////////

def merge(A) :
    if len(A) > 1 :
        mid = len(A) // 2
        L = A[ :mid]
        R = A[mid: ]
        merge (L)
        merge (R)
        i = j = k = 0
        while i < len(L) and j < len(R) :
            if L[i] > R[j] :
                A[k] = L[i]
                i += 1
            else :
                A[k] = R[j]
                j += 1
            k += 1
        while i < len (L) :
            A[k] = L[i]
            i += 1
            k += 1
        while j < len (R) :
            A [k] = R [j]
            j += 1
            k += 1

    return A
r = [40,60,30,50,90,20,70,10,80]
z = merge(r)
print('merge sort     : ',z)
    
#/////////////////////////////////////////////////////////////////////////////////////

def partiton(A , low ,high):
    pivot = A[high]
    i = low - 1
    for j in range (low  , high) :
        if A[j] >= pivot :
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i + 1] , A[high] = A[high] , A[i + 1]
    return i + 1
def quick (A , low , high) :
    if low < high :
        P = partiton (A , low , high)
        quick (A , low , P-1)
        quick (A , P+1 , high)
    return A
h = [3,45,76,34,100,42,21,12,47]
v = quick(h , 0 , 8)
print ( 'quick sort     : ' , v)
