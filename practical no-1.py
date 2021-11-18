marks=input("input a list of marks").split()
for n in range (len (marks)):
    marks[n] = int(marks[n])
print(marks)
total_marks=0
for i in marks:
    total_marks += i
print(total_marks)

total_students=0
for students in marks:
   total_students += 1
print (total_students)

average = str(total_marks / total_students)

print("the average marks are " + average)

max=marks[0]
for i in range(len(marks)):
  if marks[i]>max :
    max=marks[i]
print(f"maximum marks are {max}")

min =marks[0]
for n in range(len(marks)):
  if marks[i]<min :
      min=marks[i]
print(f"minimum marks are {min}") 

#max. frequency
p= 0
max= 0
for j in marks:
  if marks.index(j)==p:
    if marks.count(j)>max:
      max= marks.count(j)

  i=i+1
print(f"maximum frequency : {max} ")
        
#absent students
min=marks[0]
absent=0
for n in range (len(marks)):
  if marks[n]== -1:
    absent=absent+1
  if marks[n]<min :
    min=marks[n]
print(f"minimum marks are ={min}")
print(f"no. of absent stud : {absent}")
