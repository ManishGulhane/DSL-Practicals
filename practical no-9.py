# DSL-Practicals
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

def pivot_ele(p,first,last):
  pivot = p[first]
  left = first+1
  right = last
  while True:
    while left<=right and p[left]<=pivot:
      left = left+1
    while left<=right and p[right]>=pivot:
      right = right-1
    if right<left:
      break
    else:
      p[left],p[right] = p[right],p[left]
  p[first],p[right] =p[right],p[first]
  return right

def quicksort(p,first,last):
  if first<last:
    q = pivot_ele(p,first,last)
    quicksort(p,first,q-1)
    quicksort(p,q+1,last)

n=len(p)
quicksort(p,0,n-1)
print(p)
