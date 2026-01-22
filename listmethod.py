l = [11,14,3,1,5,1]
print(l)
l.append(13) # Add new number in a list.
l.sort()#Acending order.
l.sort(reverse=True)#Decending order.
l.reverse() # change original list.
print(l.count(1)) # How many number repeated in a list.
print(l.index(1))
l.insert(1,189)#insert new number in a list.
m = [100,200,300,400]
l.extend(m)# new number extend in a list in last position.
k = m + l
print(k)#Concating method.
print(l)
