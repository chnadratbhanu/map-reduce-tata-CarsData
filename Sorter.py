n = open("out.txt","r")  # open file, read-only
s = open("l.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()