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

def add_list(*args):
    sum = 0
    if len(args) == 0:
        return sum
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "NaN"
        sum += arg
    return sum

print(add_list(1))
print(add_list(1,50, 1.23))
print(add_list(7, -12))
print(add_list("peanut_butter", "marshmellow_fluff"))

#-----------------------------------------------




# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------

def remove_ends(str):
    if len(str) < 3: 
        return ""
    else: 
        return str[1:-1]

print(remove_ends('Led Zeppelin Rules'))
print(remove_ends('a'))

#-----------------------------------------------



# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

#-----------------------------------------------

def is_palindrome(str):
    str = str.lower().replace(" ", "")
    return str == str[::-1]

print(is_palindrome('SEI Rocks'))
print(is_palindrome('rotor'))
print(is_palindrome('A nut for a jar of tuna'))
print(is_palindrome(''))

#-----------------------------------------------



# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(29))
print(is_prime(200))

#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

# shopping_cart = [ 
#   {"item": "headphones", "price": 25},
#   {"item": "speakers", "price": 40 },
#   {"item": "microphone", "price": 70},
#   {"item": "lamp", "price": 15 },
#   {"item": "tower fan", "price": 35 },
# ]


#-----------------------------------------------

def c_total_cost(shopping_cart, state):
    subtotal = sum(item["price"] for item in shopping_cart)

    tax_rate = 0.085
    tax = subtotal * tax_rate

    if state in ["HI", "AK", "TX", "FL"]:
        shipping_fee = 10
    elif state in ["AL", "MS", "NV", "IL"]:
        shipping_fee = 5
    else:
        shipping_fee = 0

    total_cost = subtotal + tax + shipping_fee
    
    return total_cost

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]

print(c_total_cost(shopping_cart, 'HI'))

#-----------------------------------------------


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not A umber"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------

def fizz_buzz(n):
    if not isinstance(n, int):
        return str(n) + " is not a Number"
    elif n % 3 == 0 and n % 5 == 0:
        return str(n) + " FizzBuzz"
    elif n % 3 == 0:
        return str(n) + " Fizz"
    elif n % 5 == 0:
        return str(n) + " Buzz"
    else:
        return str(n)

print(fizz_buzz(10))
print(fizz_buzz(30))
print(fizz_buzz(18))
print(fizz_buzz(22))
print(fizz_buzz(2))

#-----------------------------------------------




# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
# And chess_board(3,7) should return this:


[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


#-----------------------------------------------

def create_chessboard(r, c):
    board = []
    for i in range(r):
        row = []
        for j in range(c):
            if (i + j) % 2 == 0:
                row.append('O')
            else:
                row.append('X')
        board.append(row)
    return board

print(create_chessboard(6, 4))
print(create_chessboard(3, 7))

#-----------------------------------------------
