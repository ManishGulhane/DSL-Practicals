row=int(input("Enter no. of rows : "))
column=int(input("Enter no. of coloums : "))

print("Enter number of M1 : ")
mat_1=[[int(input())for i in range(column)]for i in range(row)]
print("M1 : ")
for a in mat_1:
    print(a)

row=int(input("Enter no. of rows : "))
column=int(input("Enter no. of coloums : "))

print("Enter number of M2 : ")
mat_2=[[int(input())for i in range(column)]for i in range(row)]
print("M2 : ")
for a in mat_2:
    print(a)

choice=int(input("enter your choice :"))

if choice==1:
    result_1=[[0 for i in range(column)]for i in range(row)]
    for i in range(row):
        for j in range(column):
            result_1[i][j]=mat_1[i][j]+mat_2[i][j]

    
    for r in result_1:
         print("the sum of matrices is : ",r)
       
elif choice==2:
    result_2=[[0 for i in range(column)]for i in range(row)]
    for i in range(row):
        for j in range(column):
            result_2[i][j]=mat_1[i][j]-mat_2[i][j]
            for r in result_2:
                print("the sub of matrices is : ",r)
      

elif choice == 3 :
    result_3=[[0 for i in range(column)]for i in range(row)]
    for i in range(len(mat_1)):
        for j in range(len(mat_2)):
            for k in range(len(mat_2)):
                result_3[i][j]=mat_1[i][k]*mat_2[k][j]

   
    for r in result_3:
         print("the multiplication of matrices is : ",r)
