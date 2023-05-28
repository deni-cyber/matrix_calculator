#getting values

print('NOTE...these program solves simultinous equations using CRAMERS rule and the matrix inverse method.')
print('_'*60)
print('method 1; CLAMERS RULE')

print("enter first equation values")
a=eval(input())
b=eval(input())
c=eval(input())
print("enter second equation values")
d=eval(input())
e=eval(input())
f=eval(input())
print("enter third equation values")
g=eval(input())
h=eval(input())
i=eval(input())
#formatting the matrix
matrix1,matrix2,matrix3=[a,b,c],[d,e,f],[g,h,i]
print('the matrix of the "A"is')
print(matrix1)
print(matrix2)
print(matrix3)
#getting determinant
A=(a*(e*i-h*f)-b*(d*i-f*g)+c*(d*h-e*g)) 
print('the determinant is:',A)

#getting the opposite values on the right
print('enter the values on the right hand side of the three equations (first to third respectively)')

x=eval(input())
y=eval(input())
z=eval(input())
#formatting the three matrices.
#matrix one
matrix1,matrix2,matrix3=[x,b,c],[y,e,f],[z,h,i]
print('the matrix "A1"is')
print(matrix1)
print(matrix2)
print(matrix3)
#determinant one
A1=(x*(e*i-h*f)-b*(y*i-f*z)+c*(y*h-e*z)) 
print('the determinant is:',A1)
#matrix two
matrix1,matrix2,matrix3=[a,x,c],[d,y,f],[g,z,i]
print('the matrix of the "A2"is')
print(matrix1)
print(matrix2)
print(matrix3)

#determinant two
A2=(a*(y*i-z*f)-x*(d*i-f*g)+c*(d*z-y*g)) 
print('the determinant is:',A2)

#matrix three
matrix1,matrix2,matrix3=[a,b,x],[d,e,y],[g,h,z]
print('the matrix of the "A3"is')
print(matrix1)
print(matrix2)
print(matrix3)
#determinant three
A3=(a*(e*z-h*y)-b*(d*z-y*g)+x*(d*h-e*g))
print('the determinant is:',A3) 

print('multiplying:')
print(A1,"/",A)
print(A2,"/",A)
print(A3,"/",A)
#calculating values of x y & z
Ax=A1/A
Ay=A2/A
Az=A3/A
#displaying values of xy&z
print(' the value for ')
print('x=',Ax)
print('y=',Ay)
print('z=',Az)

#introducing method 2

print ('_'*60)
print('#method 2; MATRIX INVERSE METHOD')

a11,a12,a13,a21,a22,a23,a31,a32,a33=e*i-h*f,d*i-f*g,d*h-e*g,b*i-c*g,a*i-c*g,a*h-b*g,b*f-c*e,a*f-c*d,a*e-b*d
#matrix of minors
matrix1,matrix2,matrix3=[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]
print('the matrix of the minors is')
print(matrix1)
print(matrix2)
print(matrix3)
#matrix of co-factors
print('matrix of the co-factors is')
matrix1,matrix2,matrix3=[a11,-a12,a13],[-a21,a22,-a23],[a31,-a32,a33]

print(matrix1)
print(matrix2)
print(matrix3)

#matrix of adjonment
print('matrix of the adjoinment is')
matrix1,matrix2,matrix3=[a11,-a21,a31],[-a12,a22,-a32],[a13,-a23,a33]

print(matrix1)
print(matrix2)
print(matrix3)
#pre multiplying
print ('matrix of inverse is')

matrix1,matrix2,matrix3=[a11,-a21,a31],[-a12,a22,-a32],[a13,-a23,a33]
D_1=('1/',A)
matrix4,matrix5,matrix6=[x],[y],[z]
print('          ',matrix1,'         ')
print(D_1,matrix2,)
print('          ',matrix3,'          ')

print('crossing through')
print('          ',matrix1,'         ',matrix4)
print(D_1,matrix2,'    x    ',matrix5)
print('          ',matrix3,'          ',matrix6)
matrix_1=[(a11*x+-a21*y+a31*z)]
matrix_2=[(-a12*x+a22*y+-a32*z)]
matrix_3=[(a13*x+-a23*y+a33*z)]
print('    ')
print('          ',matrix_1 )
print(D_1,matrix_2 )
print('          ',matrix_3)
D_1=(1/A)
X=(D_1*matrix_1[0])
Y=(D_1*matrix_2[0])
Z=(D_1*matrix_3[0])

print('values of x,y & z are')

print ('X=',X)
print('Y=',Y)
print('Z=',Z)

print('_'*60)
print('a Denī Tech DEVELOPMENT')
print('_'*60)