g = open("output.txt","r")
s = g.readline()
encoder = ['111', '101', '001', '1101', '0111', '1100', '0110', '1000', '0100', '0001', '10011', '01011', '0000', '01010', '10010']
newchar= [' ', 'a', 'm', 'i', 'e', 'h', 'l', 'n', 's', 'r', 'f', 'k', 'o', 't', 'y']
t = ""
j =""
for x in s:
    j = j + x
    for y in encoder:
        if j == y:
            q = encoder.index(y)
            t = t+ newchar[q]
            j = ""
print t
f = open("output2.txt","w")
f.write(t)
