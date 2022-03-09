#!/usr/bin/env python3
"""
parse_tree.py
Parses mathematical expressions from fully-parenthesized strings.
"""

__author__ = "Theo Demetriades"
__version__ = "2020-04-15"

from atds import Stack, BinaryTree

def build_parse_tree(fpexpr):#Parser
    """Creates a binary tree from the fully-parenthesized
    expression. We'll do this by pushing the current tree
    (current_focus) onto a stack when we descend to its 
    subtree to edit that subtree), then pop the stack
    to get back to previous parent trees when we've completed
    filling out the subtree.
    """
    
    tokens = tokenize(fpexpr)

    pt = BinaryTree()
    stack = Stack() #I think I'll have to do something with this stack in order to get it to work without all being in parentheses
    #For example, if I wrote something like if(stack.isEmpty()): I would know I have some operation to apply to the rest
    stack.push(pt)
    current_focus = pt

    for token in tokens:
        if token=='(':
            current_focus.insertLeft('')
            stack.push(current_focus)
            current_focus = current_focus.getLeftChild()

        elif token in ('+', '-', '*', '/'):
            current_focus.setRootVal(token)
            current_focus.insertRight('')
            stack.push(current_focus)
            current_focus = current_focus.getRightChild()

        elif token==')':
            current_focus = stack.pop()

        elif token not in ('+', '-', '*', '/'):
            current_focus.setRootVal(float(token))
            current_focus = stack.pop()



    return pt


def tokenize(fpexpr): #Lexer
    """This function takes a string of a mathematical expression, and returns
    a list of tokens (still strings). The tokens are either numbers (.0123456789), operations (+,-,*,/), or parentheses."""

    last_type = 'nothing'
    tokens = []
    for c in fpexpr:
        if c in '.0123456789':
            new_type = 'number'
            if new_type==last_type:
                tokens[-1] += c
            else:
                tokens.append(c)
                last_type = new_type
        elif c in '+-*/':
            tokens.append(c)
            last_type = 'operation'
        elif c in '()':
            tokens.append(c)
            last_type = 'parenthesis'
        
        else:#c is not a number, operation, or parenthesis (probably a space)
            continue
    return tokens
    


def evaluate(parse_tree):#Interpreter
    """Now that the binary parse tree has been assembled, we can
    traverse through it recursively, using the values of each 
    node to calculate the final result of the mathematical expression.
    
    Because we'll be recursing, what is the base case? How will we know 
    when we need to return a result?
    """
    

    leftChild = parse_tree.getLeftChild()
    rightChild = parse_tree.getRightChild()

    if not (leftChild and rightChild):
        return parse_tree.getRootVal()

    else:
        operation = parse_tree.getRootVal()
        if operation=='+':
            return evaluate(parse_tree.getLeftChild())+evaluate(parse_tree.getRightChild())
        elif operation=='-':
            return evaluate(parse_tree.getLeftChild())-evaluate(parse_tree.getRightChild())
        return evaluate(parse_tree.getLeftChild())*evaluate(parse_tree.getRightChild())\
            if operation=='*' else evaluate(parse_tree.getLeftChild())/evaluate(parse_tree.getRightChild())

    


def main():
    EPSILON = 0.001     # Used to accept results of limited precision
    tests = [("( 2 + 3 )", 5), ("( 1 / 3 )", 1/3), ("( ( 3 + 5 ) * 2 )", 16),\
        ("( 3 + ( 5 * 2 ) )", 13), ("( ( 2 + ( 6 * 7 ) ) - 1 )", 43),\
            ("( ( ( ( 4 / 1 ) - ( 4 / 3 ) ) + ( 4 / 5 ) ) - ( 4 / 7 ) )", 3.1416)]

    '''
    Add these tests laster on once the first test is working:
             ("( 1 / 3 )", 1/3),
             ("( ( 3 + 5 ) * 2 )", 16),
             ("( 3 + ( 5 * 2 ) )", 13),
             ("( ( 2 + ( 6 * 7 ) ) - 1 )", 43),
             ("( ( ( ( 4 / 1 ) - ( 4 / 3 ) ) + ( 4 / 5 ) ) - ( 4 / 7 ) )", 3.1416)]
    ''' 

    for i in range(len(tests)):
        # Build the parse tree based on fully-parenthesized 
        # expression
        print("Testing expression",tests[i][0])
        pt = build_parse_tree(tests[i][0])
        # print("DEBUG:",pt)
        # Now evaluate the expression, recursively!
        # result = evaluate(pt)
        # print("DEBUG:",result)
        print("Result:",evaluate(pt))
        if abs(evaluate(pt) - tests[i][1]) < EPSILON:
            print("Test",i + 1,"passed")
        else:
            print("Test",i + 1,"failed")
    print("""Test 6 should fail. It's an attempt to calculate pi that doesn't 
get very far.""")


if __name__ == "__main__":
    main()