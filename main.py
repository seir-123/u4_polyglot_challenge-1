def add_list(*nums):
    sum=0
    if type(nums) != int:
        
        print ("NaN")
    else:
        for el in nums:
          sum += el
    print(sum)
    return(sum)

def remove_ends (string):
    if len(word) <= 3:
        print("")
        return("")
    else:
        newWord = word[1:-1]
        print(newWord)


def is_palindrome(word):
      if len(word) <= 1:
          return True
      else: 
          newWord = word.replace("", "")
          for i in range(len(newWord)):
              backwords += newWord[len(newWord)- 1 -i]
          if newWord == backwords:
              print("true")
              return True
          else:
              print("false")
              return False
              
def is_prime (num):
    for x in range (2, num):
        if num % x == 0:
          print("false")
          return("False")
    print("prime!")
    return(True)
        
is_prime(3)


def calcTotal(dictionary, homestate):
   sum = 0
   for product in dictionary:
        product ["price"] *= 1.085
        sum += product["price"]
    if homestate == "HI" or homestate == "AK" or homestate == "TX" or homestate == "FL":
       sum += 10
       print (sum)
       return (sum)
    elif homestate == "AL" or homestate == "MS" or homestate == "NV" or homestate == "IL":
        sum += 5
        print (sum)
        return (sum)
    else:
       print(sum)
       return(sum)


def fizzbuzz (num):
    if type(num) != int or type(num) == None:
        print(f'{num} is not a number')
        return(f'{num} is not a number')
    for x in range(0, num):
        if x % 3 == 0 and x % 5 == 0:
            print('Fizzbuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('buzz')
        elif type(x) !=int:
            print ('Buzz')
        else: print(x)


def makeBoard (row, column):
    myList = ()
    for x in range(0, row):
       newList = ()
       if x % 2 == 0:
          for y in range (0, y):
              if(y%2 == 0):
                newList.append('0')
              else:
                  newList.append("X")
          
       else: 
           for y in range(0,column):
               if (y%2 == 0):
                   newList.append("X")
               else:
                   newList.append("0")       
       myList.append(newList) 
    print(myList)

makeBoard(2,3)-
