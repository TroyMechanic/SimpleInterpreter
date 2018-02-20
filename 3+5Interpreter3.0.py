'''Considering "3+5Interpreter2.0" do not have very good modularization,
this problem will be fixed in this file'''
# Token types
#
# EOF(enf-of-file) token is used to indicate that
# there is no more input left for lexcial analyzer
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token:
    def __init__(self, type, value):
        # token types:INTEGER PLUS EOF
        self.type = type
        # token value:1,2,3,4,5,6,7,8,9,'+',or None
        self.value = value

    def __str__(self):
        '''String representation of the class instance

       Example:
           Token(INTEGER,6)
           Token(PLUS,'+')
       '''
        return 'Token({type},{value})'.format(type=self.type, value=self.value)

    def __repr__(self):
        return self.__str__()


class Interpreter:
    def __init__(self, text):
        # client string input, e.g. '3+5'
        self.text = text
        # self.pos is  a index
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = text[self.pos]

    def advance(self):
        '''advance the 'pos' pointer and set 'current_char' variable'''
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        '''return an (mutidigit) integer consumed from the input'''
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def error(self):
        raise Exception("Error parsing input")

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)
        op = self.current_token
        if op.value == '+':
            self.eat(PLUS)
        if op.value == '-':
            self.eat(MINUS)
        right = self.current_token
        if op.value == '+':
            result = int(left.value) + int(right.value)
        if op.value == '-':
            result = int(left.value) - int(right.value)
        return result


def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
