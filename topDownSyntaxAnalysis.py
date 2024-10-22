class ZaraParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        self.current_token = self.tokens.pop(0) if self.tokens else None

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.next_token()
        else:
            raise SyntaxError(f"Expected {expected_token}, but found {self.current_token}")

    def parse_program(self):
        while self.current_token is not None:
            self.parse_statement()

    def parse_statement(self):
        if self.current_token == 'if':
            self.parse_if_statement()
        elif self.current_token == 'for':
            self.parse_for_statement()
        elif self.current_token == 'do':
            self.parse_do_while_statement()
        elif self.is_identifier(self.current_token):
            self.parse_assignment()
        else:
            raise SyntaxError(f"Invalid statement starting with {self.current_token}")

    def parse_if_statement(self):
        self.match('if')
        self.match('(')
        self.parse_expression()
        self.match(')')
        self.parse_statement()
        if self.current_token == 'else':
            self.match('else')
            self.parse_statement()

    def parse_for_statement(self):
        self.match('for')
        self.match('(')
        self.parse_assignment()
        self.match(';')
        self.parse_expression()
        self.match(';')
        self.parse_assignment()
        self.match(')')
        self.parse_statement()

    def parse_do_while_statement(self):
        self.match('do')
        self.parse_statement()
        self.match('while')
        self.match('(')
        self.parse_expression()
        self.match(')')
        self.match(';')

    def parse_assignment(self):
        self.match(self.current_token)  
        self.match('=')
        self.parse_expression()
        self.match(';')

    def parse_expression(self):
        self.parse_term()
        while self.current_token in ('+', '-'):
            operator = self.current_token
            self.match(operator)
            self.parse_term()

    def parse_term(self):
        self.parse_factor()
        while self.current_token in ('*', '/'):
            operator = self.current_token
            self.match(operator)
            self.parse_factor()

    def parse_factor(self):
        if self.is_number(self.current_token):
            self.match(self.current_token)
        elif self.is_identifier(self.current_token):
            self.match(self.current_token)
        elif self.current_token == '(':
            self.match('(')
            self.parse_expression()
            self.match(')')
        else:
            raise SyntaxError(f"Unexpected token {self.current_token}")

    def is_identifier(self, token):
        return token.isalpha()  

    def is_number(self, token):
        return token.isdigit()


test_program = """
if (x > 0) {
    y = y + 1;
} else {
    y = y - 1;
}

for (i = 0; i < 10; i = i + 1) {
    sum = sum + i;
}

do {
    x = x - 1;
} while (x > 0);
"""

tokens = [
    "if", "(", "x", ">", "0", ")", "{", "y", "=", "y", "+", "1", ";", "}", "else", "{", "y", "=", "y", "-", "1", ";", "}",
    "for", "(", "i", "=", "0", ";", "i", "<", "10", ";", "i", "=", "i", "+", "1", ")", "{", "sum", "=", "sum", "+", "i", ";", "}",
    "do", "{", "x", "=", "x", "-", "1", ";", "}", "while", "(", "x", ">", "0", ")", ";"
]


parser = ZaraParser(tokens)

try:
    parser.parse_program()
    print("Parsing successful!")
except SyntaxError as e:
    print(f"Syntax Error: {e}")
