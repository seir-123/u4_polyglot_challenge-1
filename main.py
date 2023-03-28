# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

#-----------------------------------------------
def add_list(*nums):
    sum = 0
    
    for num in nums:
        if type(num) == int:
            sum += num
        else:
            print('NaN')

    print(sum)
    
# add_list(1,2,3,4,5)
# add_list(1,'two',3,4,5)
# add_list('two', 'four', 'six', 4.5)
# add_list()

    
   
    
    

    
#-----------------------------------------------




# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with
# the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
def remove_ends(string):
    if len(string) < 3:
        print('')
    else:
        print(string[1:-1])
        
# remove_ends('Led Zeppelin Rules')
# remove_ends('a')
#-----------------------------------------------



# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false 
# depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

#-----------------------------------------------
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) < 2:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

# is_palindrome('SEI Rocks')
# is_palindrome('rotor') 

#-----------------------------------------------



# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number 
# and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------
def is_prime(n):
    if n < 2:
        print(False)
    else:
        is_prime = True
        for i in range(2, int(n / 2)+1):
            if n % i == 0:
                is_prime = False
                
        print(is_prime)

is_prime(2)
is_prime(0.5)

#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there
# is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if 
# the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

# shopping_cart = [ 
#   {"item": "headphones", "price": 25},
#   {"item": "speakers", "price": 40 },
#   {"item": "microphone", "price": 70},
#   {"item": "lamp", "price": 15 },
#   {"item": "tower fan", "price": 35 },
# ]


#-----------------------------------------------
def calculate_total_cost(shopping_cart, homestate):
    total_cost = 0
    for item in shopping_cart:
        item_price = item["price"] * 1.085  
        total_cost += item_price

    shipping_fee = 0
    if homestate in ["HI", "AK", "TX", "FL"]:
        shipping_fee = 10
    elif homestate in ["AL", "MS", "NV", "IL"]:
        shipping_fee = 5

    total_cost += shipping_fee
    print(f"Total cost for {homestate}: ${total_cost:.2f}")


shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]

# calculate_total_cost(shopping_cart, 'TX')
# calculate_total_cost(shopping_cart, 'AL')
#-----------------------------------------------


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print 
# “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples
# of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not A number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
def fizz_buzz(num):
    for num in range(1, 51):
        if type(num) != int:
            print(f"{num} is not a Number")
        elif num % 3 == 0 and num % 5 == 0:
            print(f"{num} FizzBuzz")
        elif num % 3 == 0:
            print(f"{num} Fizz")
        elif num % 5 == 0:
            print(f"{num} Buzz")
        else:
            print(f"{num}")



# fizz_buzz('ham_sandwich')
# fizz_buzz(18)
# fizz_buzz(30)
# fizz_buzz(10)

#-----------------------------------------------




# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:

# [
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"],
#     ["O","X","O","X"],
#     ["X","O","X","O"]
# ]
# # And chess_board(3,7) should return this:


# [
#     ["O","X","O","X","O","X","O"],
#     ["X","O","X","O","X","O","X"],
#     ["O","X","O","X","O","X","O"]
# ]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


#-----------------------------------------------
def chess_board(rows, columns):
    chessboard = []
    for r in range(rows):
        row = []
        for c in range(columns):
            if (r+c) % 2 == 0:
                row.append("O")
            else:
                row.append("X")
        chessboard.append(row)
        print(row)
        
        
# chess_board(6,4)        
# chess_board(3,7)
#-----------------------------------------------

