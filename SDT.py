#Expression handling
class ExpressionNode:
    def __init__(self, place, code):
        self.place = place  # Temporary variable for holding the result
        self.code = code    # Generated intermediate code

def expression():
    E1 = term()
    while current_token in ['PLUS', 'MINUS']:  # Handle addition or subtraction
        op = current_token
        next_token()
        T = term()
        temp = new_temp()
        code = E1.code + T.code + f"{temp} = {E1.place} {op} {T.place}\n"
        E1 = ExpressionNode(temp, code)
    return E1
#Assignment statements
def assignment():
    identifier = current_token  # variable on the left side
    next_token()  # skip identifier
    expect('ASSIGN')
    expr = expression()
    expect('SEMICOLON')
    code = expr.code + f"{identifier} = {expr.place}\n"
    return code

#Control statements
def if_statement():
    expect('IF')
    expect('LPAREN')
    expr = expression()
    expect('RPAREN')
    true_label = new_label()
    false_label = new_label()
    code = expr.code
    code += f"if {expr.place} goto {true_label}\n"
    code += f"goto {false_label}\n"
    code += f"{true_label}:\n"
    stmt_code = statement()
    code += stmt_code
    code += f"{false_label}:\n"
    return code

def for_statement():
    expect('FOR')
    expect('LPAREN')
    init = assignment()  # Initialization code
    expect('SEMICOLON')
    cond = expression()  # Loop condition
    expect('SEMICOLON')
    increment = assignment()  # Increment step
    expect('RPAREN')
    loop_body = statement()  # Loop body code

    loop_start = new_label()
    loop_end = new_label()
    code = init
    code += f"{loop_start}:\n"
    code += cond.code
    code += f"ifFalse {cond.place} goto {loop_end}\n"
    code += loop_body
    code += increment
    code += f"goto {loop_start}\n"
    code += f"{loop_end}:\n"
    return code

#subprograms/functions
def function_definition():
    expect('DEF')
    func_name = current_token
    next_token()
    expect('LPAREN')
    params = parameter_list()
    expect('RPAREN')
    expect('LBRACE')
    stmt_list_code = statement_list()
    expect('RBRACE')
    code = f"func {func_name}:\n"
    code += params.code
    code += stmt_list_code
    code += "return\n"
    return code