g = open("output.txt","r")
s = g.readline()

encoder=[]
characters = []
with open('dictionary.txt') as p:
    for line in p:
        line = line.strip('\n')
        #print line
        w = line.split("=")
        #print w[0]
        #print w[1]
        characters.append(w[0])
        encoder.append(w[1])

t = ""
j =""
for x in s:
    j = j + x
    for y in encoder:
        if j == y:
            q = encoder.index(y)
            t = t+ characters[q]
            j = ""
print t
f = open("output2.txt","w")
f.write(t)

