#Token types
#
#EOF(enf-of-file) token is used to indicate that
#there is no more input left for lexcial analyzer
INTEGER,PLUS,EOF='INTEGER','PLUS','EOF'
class Token:
    def __init__(self,type,value):
        #token types:INTEGER PLUS EOF
        self.type=type
        #token value:1,2,3,4,5,6,7,8,9,'+',or None
        self.value=value
    def __str__(self):
        '''String representation of the class instance

       Example:
           Token(INTEGER,6)
           Token(PLUS,'+')
       '''
        return 'Token({type},{value})'.format(type=self.type,value=self.value)
    def __repr__(self):
        return self.__str__()

class Interpreter:
    def __init__(self,text):
        #client string input, e.g. '3+5'
        self.text=text
        #self.pos is  a index
        self.pos=0
        #current token instance
        self.current_token=None
    def error(self):
        raise Exception("Error parsing input")
    def get_next_token(self):
        text=self.text
        pos=self.pos
        if pos>len(text)-1:
            return Token(EOF,None)
        current_char=text[pos]
        if current_char.isdigit():
            self.pos+=1
            return Token(INTEGER,current_char)
        if current_char=='+':
            self.pos+=1
            return Token(PLUS,current_char)
        self.error()
    def eat(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.get_next_token()
        else:
            self.error()
    def expr(self):
        self.current_token=self.get_next_token()
        left=self.current_token
        self.eat(INTEGER)
        op=self.current_token
        self.eat(PLUS)
        right=self.current_token
        result=int(left.value)+int(right.value)
        return result

def main():
    while True:
        try:
            text=input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter=Interpreter(text)
        result=interpreter.expr()
        print(result)

if __name__=='__main__':
    main()

