f1=open("HELLO001.txt",'w')
l1=["HELLO","\nWELCOME","\nTO","\nPYTHON"]
f1.writelines(l1)
f1.close()
f1=open("HELLO001.txt",'r')
print(f1.readlines())