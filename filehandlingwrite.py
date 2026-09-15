f = open("demofile.txt","a")
f.write("\nWriting a file")  
f = open("demofile.txt","r")
fr = f.read()
print(fr)

f = open("demofile.txt","w")
f.write("\nonce we write something in existing file it will overwrite eveything ")