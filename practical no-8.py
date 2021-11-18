#bubble sort 
l = int(input("enter nos in list: "))
a=[]
for i in range(l):
  a.append(int(input("")))
print ("unsorted list =  ", a)

def bubble_sort(a) :
    for i in range(len(a)-1,0,-1):
        for j in range (i):
         if a[j]>a[j+1]:
            temp = a[j]
            a[j] =a[j+1]
            a[j+1] = temp
bubble_sort(a)
print("sorted list =",a)
