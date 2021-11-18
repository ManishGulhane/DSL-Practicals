
   
a=[]
n = int(input("Enter total number of students : ")) 
for i in range(n):
   rollno=int(input("Enter roll on of student : " ))
   a.append(rollno)
key = int (input ('enter a key = '))
def binarysearch (c,  k ) :
    first=0
    last = len(a)-1 
    mid = 0
    for i in a :
        for j in a :
  
         mid = first + last//2 
         if  c[mid]<k :
             low = mid +1 
         elif c[mid]>k :
             first = mid -1
         else :
             return mid

result = binarysearch (a , key )
print ("the elements are found in list" ,result )
#fibonacci_search :
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

key=int(input("enter no to search: "))

def fibonacci_search(p, key):
    size = len((p))
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        i = min(start + f0, size - 1)
        if p[i] < key:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = i
        elif p[i] > key:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return i
    if (f1) and (p[size - 1] == key):
        return size - 1
    return -1

output = (fibonacci_search(p, key))

if output == -1:
  print("not found")
else:
  print('found')
