import re

class LexicalAnalyzer:
    def __init__(self, code):
        self.code = code
        self.keywords = {'if', 'else', 'do', 'while', 'var', 'begin', 'end', 'program', 'procedure'}
        self.operators = {'+', '-', '*', '/', ':=', '=', '<', '>', '<=', '>=', '!=', '&&', '||', 'not'}
        self.datatypes = {'integer', 'float', 'string', 'array', 'stack'}

    def tokenize(self):
        tokens = []
        # Regular expression pattern to match tokens
        pattern = r'(\b\w+\b)|([+-]?\d+(\.\d+)?)|("[^"]*")|([<>=!]=?)|([+\-*/])|(\|\||&&)|([()\[\]\{\};])'

        # Use re.finditer to find all matches of the pattern in the code
        for match in re.finditer(pattern, self.code):
            token = match.group()

            if token in self.keywords:
                tokens.append(('KEYWORD', token))
            elif token in self.operators:
                tokens.append(('OPERATOR', token))
            elif token in self.datatypes:
                tokens.append(('DATATYPE', token))
            elif re.match(r'[a-zA-Z_]\w*', token):  # Identifiers
                tokens.append(('IDENTIFIER', token))
            elif re.match(r'^[+-]?\d+(\.\d+)?$', token):  # Numbers (integers or floats)
                tokens.append(('LITERAL', token))
            elif re.match(r'^".*"$', token):  # String literals
                tokens.append(('LITERAL', token))
            else:
                tokens.append(('SYMBOL', token))
        return tokens

# Sample Zara code to test the lexical analyzer
code = """
program example;

var
    num: integer;
    text: string;

begin
    num := 10;
    text := "Hello, world!";

    if num > 5 then
        write(text);
    else
        writeln("Number is less than or equal to 5.");
end.
"""

# Create a lexical analyzer and tokenize the Zara code
analyzer = LexicalAnalyzer(code)
tokens = analyzer.tokenize()

# Print the tokens
for token in tokens:
    print(token)
