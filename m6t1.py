stud={}
n=int(input('Enter how many records you want to enter'))
for i in range(n):
    a=input('Enter student\'s name:')
    b=int(input('Enter studen\'s marks'))
    stud[a]=b
s=input('Enter student name you want to search : ')
if s in stud:
    print(s , 'marks :',stud[s])
else:
    print('student not found')  
      