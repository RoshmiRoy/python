f=open("C:/Users/student.MCALAB/Documents/cycle5/p2.txt" ,"r")

f1=open("C:/Users/student.MCALAB/Documents/cycle5/hello.txt" ,"w")

line=f.readlines()
type(line)
for i in range(0,len(line)):
    if(i%2!=0):
        f1.write(line[i])
    else:
        pass
f1.close()
f1=open("C:/Users/student.MCALAB/Documents/cycle5/hello.txt","r")
lines=f1.read()
print(lines)
f1.close()
f.close()
