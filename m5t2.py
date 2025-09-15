

file1=open("output.txt","w")
data1=input('Enter text to be written to the file :')
file1.write(data1)
print("Data sucessfully written to output.txt")
file1.close()
  
file1=open("output.txt","a")
data2 = input('Additional text to append:')
file1.write(data2)
print("Data sucessfully appended to output.txt")
file1.close()

file1 = open("output.txt","r")
read_file=file1.read()
print(read_file)
file1.close()