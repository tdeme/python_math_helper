from tokens import Token, TokenType

WHITESPACE = ' \t\n\r'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        """Advance the 'cursor' through the text."""
        try:
            self.current_char = next(self.text)

        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        """This generator yields a sequence of tokens from the given text."""
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char=='.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char=='+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char=='-':
                yield Token(TokenType.MINUS)
                self.advance()
            elif self.current_char=='*':
                yield Token(TokenType.MULTIPLY)
                self.advance()
            elif self.current_char=='/':
                yield Token(TokenType.DIVIDE)
                self.advance()
            elif self.current_char=='(':
                yield Token(TokenType.LPAREN)
            elif self.current_char==')':
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character: {self.current_char}")

    def generate_number(self):
        """Generate a number token."""
        decimal_point_seen = False 
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char=='.' or self.current_char in DIGITS):
            if self.current_char=='.':
                if decimal_point_seen:
                    break
                decimal_point_seen = True
            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
            if number_str.endswith('.'):
             number_str = number_str[:-1]
        elif number_str.endswith('.'):
            number_str += '0'
        
        return Token(TokenType.NUMBER, float(number_str))
        
            
