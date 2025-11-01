'''Characterstis of set
1.Unordered  - no indexing. 
2.unique value and item . 
3.Mutable - add/remove elemenst 
4.Immutable elemenst  

#Type of sets 
#Using curls bracket
my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))

#Using the set constructor
my_set = set([1,2,3,4,5])
print(my_set)
print(type(my_set))

 #SET OPERATION
Fruits = {"Apple","Banana","Cherry"}
Fruits.add("Mango")#Add elements
Fruits.remove("Banana")#Remove elements
Fruits.discard("Orange")#Discard elemets but orange is not in the list. 
print(Fruits)


#SET Method 
#1.) Union set is combine elements from two sets . 
set_a = {1,2,3}
set_b = {4,5,6}
#union_set = set_a.union(set_b)
union_set2 = set_a | set_b # alternative union .  Another trick .  for  these symbol  just Press Shift + \ → You’ll get 
print(union_set2)
#Output {1,2,3,4,5,6}

#2.) Intersection means only elements present both side . 
set_c ={0,7,8,9,11}
set_d = {10,8,0,11}
#intersection_set = set_c.intersection(set_d)
intersection_set2 = set_c & set_d # Alternative 
print(intersection_set2)
#Output {8,0,11}
#3.) Difference means elements present in the first set but not in the second . 
set_e = {1,3,4,6}
set_f = {0,3,6,7}
#difference_set = set_e.difference(set_f)
difference_set2 = set_e -set_f # Alternative Difference or another trick 
print(difference_set2)
#Output {1,4}

#4.) Symmetric Difference means elements in either set, but not in the both . 
set_g = {1,2,3}
set_h = {3,4,5}
#Symmetric_diff = set_g.symmetric_difference(set_h)
Symmetric_diff2 = set_g ^ set_h #Alternative 
print(Symmetric_diff2)
# Output {1,2,4,5}
'''


#Set Iteration 
#For Loop 
Number = {1,2,3,4,5}
for i in Number:
     print(i)
     #Output 
     
2
3
4
5
 #While does 't support 
 
 #Set Compreshesion 
Squares = {x**3 for x in range(1,6)}
print(Squares)    
# Output : {64, 1, 8, 27, 125}
