from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance() #__init__ and advance() look very similar as in lexer.py

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token==None:
            return None

        result = self.expr()

        if self.current_token != None:
            self.raise_error()

        return result

    def expr(self): #All expressions are terms added or subtracted to/from another term
        result = self.term() #"term" is the lower, or "child", grammar rule with respect to "expr"
        
        while self.current_token!=None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type==TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term()) #Joining terms on either side of +
            elif self.current_token.type==TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term()) 
    
        return result

    def term(self): #All terms are factors multiplied or divided by another factor
        result = self.factor() #"factor" is the lower, or "child", grammar rule with respect to "termr"
        
        while self.current_token!=None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type==TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor()) #Joining terms on either side of +
            elif self.current_token.type==TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor()) 
    
        return result

    def factor(self): #All factors are just numbers...
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        self.raise_error()
