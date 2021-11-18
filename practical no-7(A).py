noofstudent=[]
n = int(input("Enter total number of students : ")) 
for i in range(n):
   rollno=int(input("Enter roll on of student : " ))
   noofstudent.append(rollno)

key = int (input ('enter a key = '))
def linear_search():
  for i in range(n):
    if (noofstudent[i] == key):
      return (i)

    else:
      return (-1)

def sentinel_search():
     size=key 
     for i in range (len(noofstudent)):
           
           if (i == size):
                return (i)
           else:
               return (-1)

result = linear_search()
result1 = sentinel_search()
if (result==-1):
  print(" roll number not found")
else:
  print(" roll number found ")

if (result1==-1):
  print(" roll number not found ")
else:
  print(" roll number found ")
