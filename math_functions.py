import math
import statistics
import parse_tree
from lexer import Lexer
from parser_ import Parser

#function to find primes within a certain range
def findPrimes(start, finish):
#x = the numbers being tested
    for x in range(start, finish):
#i = the numbers being used to test x
        for i in range(2, int((finish/2)+1)):
#if the numbers are equal, the remainder will be 0... but that doesn't mean the number is prime!
            if x==i:
                continue
#stop checking the number once a factor is found
            elif x % i == 0:
                a = "Composite"
                break
            else:
                a = "Prime"
        print(x)
        print(a)

def check_ifPrime(num):
    for x in range(2, num+1):
        if num == 2:
            return "Prime"
            break
        
        elif num == x:
            continue

        elif num % x == 0:
            return "Composite"
            break

        else:
            return "Prime"

        


        
'''def findFactorial(num):
    product = 1
    for x in range(0, num):
        product = product * (x + 1)
    print(product)'''

def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)
   

def findFactors(num):
    for x in range(2, int((0.5 * num)+1)):
        if num % x == 0:
            print(x)

def exponent(int1, int2):
    product = 1
    for x in range(0, int2):
        product = product * int1
    print(product)

def findMultiples1(num, start, finish):
    for x in range(start, finish):
        if x % num == 0:
            print(x)
            
def findMultiples2(num1, num2, start, finish):
    for x in range(start, finish):
        if x % num1 == 0 and x % num2 == 0:
            print(x)

def findMultiples3(num1, num2, num3, start, finish):
    for x in range(start, finish):
        if x % num1 == 0 and x % num2 == 0 and x % num3 == 0:
            print(x)

def findInterest(start, rate, time):
    power = pow(rate, time)
    print(round(start * power, 2))

def evaluate(expression):
    tree = parse_tree.build_parse_tree(expression)
    return parse_tree.evaluate(tree)


def main():
    text = input("calc > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()

    print(evaluate(str(tree)))


if __name__=='__main__':
    main()