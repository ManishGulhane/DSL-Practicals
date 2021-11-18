A = int(input("Enter the number of rows:"))
B = int(input("Enter the number of columns:"))

matrix1 = []
for i in range(A):          
  a =[]
  for j in range(B):     
      a.append(int(input()))
  matrix1.append(a)

for i in range(A):
  for j in range(B):
      print(matrix1[i][j], end = " ")
  print()

sparse_mat =[]
sparse_mat1 = []


for i in range (len(matrix1)):
  for j in range (len(matrix1[0])):
    if (matrix1[i][j] !=0 ):
      b = []
      b.append(i)
      b.append(j)
      b.append(matrix1[i][j])

      sparse_mat.append(b)
print(sparse_mat)

matrix2 = []
for i in range(A):          
  a =[]
  for j in range(B):     
      a.append(int(input()))
  matrix2.append(a)

for i in range(A):
  for j in range(B):
      print(matrix2[i][j], end = " ")
  print()


for i in range (len(matrix2)):
  for j in range (len(matrix2[0])):
    if (matrix2[i][j] !=0 ):
      a = []
      a.append(i)
      a.append(j)
      a.append(matrix1[i][j])

      sparse_mat1.append(a)
print(sparse_mat1)

def add(sparse_mat,sparse_mat1):
  result = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
  print("addition")
  for i in range(len(sparse_mat)):  
    for j in range(len(sparse_mat[0])):  
       result[i][j] = sparse_mat[i][j] + sparse_mat1[i][j]
  print(result)

add(sparse_mat,sparse_mat1)

def transpose(sparse_mat):
  Res = []
  print("transpose0")
  for i in sparse_mat:
    Res.append([i[1], i[0], i[2]])
  print(Res)

transpose(sparse_mat)
transpose(sparse_mat1)
