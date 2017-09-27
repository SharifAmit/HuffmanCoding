f = open("input.txt","r")
s = f.readline() # Reading line from the file
#s = s.replace(" ","") # Removing spaces between letters)
s = s.lower()
t = list(set(s)) # Unique chars in the string
print "The String: ",s
q = len(t)
print "The char list: ", t

# Making a frequency table for the chars in the string
b = [0]*q
for x in s:
  count = s.count(x)
  y = t.index(x)
  if b[y] == 0:
    b[y] = count
print "Frequency Table before sorting: "
print b


new = []
newchar = []
while b:
    max = b[0]
    for x in b:
        if x > max:
            max= x
    c=b.index(max)
    new.append(max)
    newchar.append(t[c])
    t.remove(t[c])
    b.remove(max)
print "Frequency Table after sorting: "
print new
print newchar
k = 0
for x in new:
    if x != 0:
        k = k + 1
j = 2*k-1
print "Number of nodes in the tree: ",j

print "Number of leafs in the tree: ",k


encoder = ["null"]*k
print "encoder",encoder


bintree = list(new)
strtree = list(newchar)

print "binarytree",bintree
print "Stringtree",strtree

for q in range(len(bintree)-1,-1,-1):
    left = 999
    right = 999
    leftstr = ""
    rightstr = ""
    for i in range(len(bintree)-1,-1,-1):
        if bintree[i] < right:
                right = bintree[i]
                rightstr = strtree[i]
                j = i
    #print rightstr, "ami right"
    #print right
    for y in rightstr:
        ci = newchar.index(y)
        if encoder[ci]=="null":
            encoder[ci]="0"
        else:
            encoder[ci]="0"+encoder[ci]
    v = strtree.index(rightstr)
    strtree.pop(v)
    bintree.pop(v)
    for i in range(len(bintree)-1,-1,-1):

        if bintree[i] < left or bintree[i] == right:
                left = bintree[i]
                leftstr = strtree[i]
                z = i
                #print "ami z",z

    #print leftstr, "ami left"

    #print left

    for x in leftstr:
        ci = newchar.index(x)
        if encoder[ci]=="null":
            encoder[ci]="1"
        else:
            encoder[ci]="1"+encoder[ci]


    #print leftstr
    w = strtree.index(leftstr)
    strtree.pop(w)
    bintree.pop(w)

    summation = right + left
    strsum = leftstr + rightstr
    strtree.insert(0,strsum)
    bintree.insert(0,summation)


    print "valuetable",bintree
    print "strlist",strtree
    print "encoder",encoder
    if len(bintree)==1:
        break
print newchar
f.close()
t = ""
for i in s:
    for j in newchar:
        if j==i:
            p = newchar.index(j)
            t = t + encoder[p]

print t
g = open("output.txt","w")
g.write(t)
g.close()