numbers = [1,4,3,5,6,8,3,4,5,7,9,3,12,5,14,16,17,8]
def findMaxInList(numbers):
   maxValue = numbers[0]
   for eachNum in numbers:
      if eachNum > maxValue:
         maxValue = eachNum

   return maxValue
      
print(findMaxInList(numbers))