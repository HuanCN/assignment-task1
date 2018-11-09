
def add (a,b):
  return a+b
assert add(1,3) == 4

numbers = [1,2,3,5]
def sumOfList(someList):
    result = 0
    for index in someList:
        result = someList.index(index)+result
    return result
 sumOfList(numbers) == 11
