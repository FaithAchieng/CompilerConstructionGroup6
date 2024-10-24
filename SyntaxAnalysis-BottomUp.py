import re

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.input = []
        self.index = 0

    def parse(self, tokens):
        self.input = tokens
        while True:
            action = self.get_action()
            if action == "shift":
                self.shift()
            elif action == "reduce":
                self.reduce()
            elif action == "accept":
                print("Input accepted.")
                return
            else:
                print(f"Error: {action}")
                return

    def shift(self):
        token = self.input[self.index]
        self.stack.append(token)
        self.index += 1
        print(f"Shift: {token}, Stack: {self.stack}")

    def reduce(self):
        for lhs, rhs in self.grammar.items():
            if self.stack[-len(rhs):] == rhs:
                print(f"Reduce: {lhs} -> {' '.join(rhs)}, Stack before: {self.stack}")
                del self.stack[-len(rhs):]
                self.stack.append(lhs)
                print(f"Stack after: {self.stack}")
                return
        print("No applicable reduction found.")

    def get_action(self):
        if self.index < len(self.input):
            return "shift"
        elif self.stack and self.stack[-1] in self.grammar.keys():
            return "reduce"
        elif self.index == len(self.input) and len(self.stack) == 1 and self.stack[0] == 'S':
            return "accept"
        else:
            return "error"

def tokenize(code):
    token_pattern = r'\s*(?:(\d+|[a-zA-Z_][a-zA-Z0-9_]*)|(\S))\s*'
    tokens = []
    for match in re.finditer(token_pattern, code):
        token = match.group(1) if match.group(1) else match.group(2)
        if token:
            tokens.append(token)
    return tokens

grammar = {
    'S': ['E'],
    'E': ['E', '+', 'E'],
    'E': ['E', '-', 'E'],
    'E': ['E', '*', 'E'],
    'E': ['E', '/', 'E'],
    'E': ['(', 'E', ')'],
    'E': ['id']
}

def main():
    zara_code = "id + id * id"
    tokens = tokenize(zara_code)
    print(f"Tokens: {tokens}")

    parser = Parser(grammar)
    parser.parse(tokens)

if __name__== "__main__":
    main()
