from lexer import lexer

class Parser:
    def __init__(self, input_str):
        lexer.input(input_str)
        self.tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            self.tokens.append(tok)
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        tok = self.current_token()
        if tok and tok.type == token_type:
            self.pos += 1
            return tok
        raise SyntaxError(f"Esperava token {token_type}, mas recebi {tok.type if tok else 'EOF'}")

    def parse(self):
        result = self.expr()
        if self.current_token() is not None:
            raise SyntaxError("Tokens a mais no fim da expressão.")
        return result

    def expr(self):
        result = self.term()
        return self.exprp(result)

    def exprp(self, inherited):
        tok = self.current_token()
        if tok is not None and tok.type in ('PLUS', 'MINUS'):
            self.eat(tok.type)
            right = self.term()
            if tok.type == 'PLUS':
                return self.exprp(inherited + right)
            else:
                return self.exprp(inherited - right)
        return inherited

    def term(self):
        result = self.factor()
        return self.termp(result)

    def termp(self, inherited):
        tok = self.current_token()
        if tok is not None and tok.type in ('TIMES', 'DIVIDE'):
            self.eat(tok.type)
            right = self.factor()
            if tok.type == 'TIMES':
                return self.termp(inherited * right)
            else:
                return self.termp(inherited / right)
        return inherited

    def factor(self):
        tok = self.current_token()
        if tok.type == 'NUM':
            self.eat('NUM')
            return tok.value
        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result
        else:
            raise SyntaxError(f"Token inesperado em factor: {tok}")
