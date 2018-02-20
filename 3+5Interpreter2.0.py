'''
    In this 2.0 version
    I will finish next jobs
    1.make sure text like '12+3' can go well
    2.have my interpreter accept blank
    3.have my interpreter accept '-'
'''
INTEGER,PLUS,EOF,BLANK,MINUS='INTEGER','PLUS','EOF','BLANK','MINUS'
class Token:
    def __init__(self,type,value):
        #token types:INTEGER PLUS EOF
        self.type=type
        #token value:1,2,3,4,5,6,7,8,9,'+',' ','-',or None
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
        #deal with the blank
        if current_char==' ':
            self.pos+=1
            return Token(BLANK,current_char)
        if current_char.isdigit():
            self.pos+=1
            return Token(INTEGER,current_char)
        #deal with the '-'
        if current_char=='-':
            self.pos+=1
            return Token(MINUS,current_char)
        if current_char=='+':
            self.pos+=1
            return Token(PLUS,current_char)
        self.error()
    def eat(self,token_type):
        if self.current_token.type==token_type:
            self.current_token=self.get_next_token()
        else:
            self.error()
        while self.current_token.type==BLANK:
            self.current_token=self.get_next_token()
    def expr(self):
        #handle the left num
        self.current_token=self.get_next_token()
        left=[]
        while self.current_token.type==INTEGER:
            left.append(self.current_token.value)
            self.eat(INTEGER)
        left=int(''.join(left))

        #handle the middle op
        op=self.current_token
        if op.value=='+':
            self.eat(PLUS)
        if op.value=='-':
            self.eat(MINUS)

        #handle the right num
        right=[]
        while self.current_token.type==INTEGER:
            right.append(self.current_token.value)
            self.eat(INTEGER)
        right=int(''.join(right))

        if op.type==PLUS:
            result=left+right
        if op.type==MINUS:
            result=left-right
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

