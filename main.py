alpha='abcdefghijklmnopqrstuvwxyz'
s='sharique'
t=''
i=0
k=1
t=t+(alpha[(((alpha.index(s[i]))+k)%26)])
print(alpha.index(s[i]))
#t=t+(alpha[(((alpha.index(s[i+1]))+k)%26)])
#print(t)

#t=t+(alpha[(((alpha.index(s[i+2]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+3]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+4]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+5]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+6]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+7]))+k)%26)])
#t=t+(alpha[(((alpha.index(s[i+8]))+k)%26)])

print(t)