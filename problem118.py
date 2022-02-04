##############
##
##Brady Neeb
##
##Daily Coding Problem #118:
##Given a sorted list of integers, square 
##the elements and give the output in sorted order
##
##7/21/2020
##
##############

#imports


def square(x):
   newList = []
   for i in range (0,len(x)):      
      newList.append((x[i])**2)
   newList.sort()
   print(newList)


list = [-9,-2,0,2,3]
square(list)