##############
#
#Brady Neeb
#
#Daily Coding Problem #69
#Given a list of integers, return the largest 
#product that can be made by multiplying any three integers.
#
#7/21/2020
#
##############

#imports


def prodThree(x):
   total = 1
   for i in range (0,3):
      total = x[i] * total
   print(total)



def largestProd(x):

   total = 0
   newTotal = 0
   
   for i in range (0, len(x)):
      total = x[i]*x[i+1]*x[i+2]
      
      if newTotal >= total:
          newTotal = total
          print(newTotal)




list = [10, -10, 5, 2]
prodThree(list)
