class SymbolTable:
  def __init__(self):
      self.symbols = {}

  def add_symbol(self, name, type):
      if name not in self.symbols:
          self.symbols[name] = type
          print(f"Symbol added: {name} of type {type}")
      else:
          print(f"Error: Symbol '{name}' already exists.")

  def update_symbol(self, name, new_type):
      if name in self.symbols:
          self.symbols[name] = new_type
          print(f"Symbol updated: {name} of type {new_type}")
      else:
          print(f"Error: Symbol '{name}' not found.")

  def retrieve_symbol(self, name):
      if name in self.symbols:
          return self.symbols[name]
      else:
          print(f"Error: Symbol '{name}' not found.")

  def log_symbols(self):
      print("Symbol Table Entries:")
      for name, type in self.symbols.items():
          print(f"{name}: {type}")
"""program symbol_table_example;

var
    num_int: integer;
    num_float: float;
    text_str: string;
    arr_int: array[1..10] of integer;
    stack_char: stack of char;

procedure my_procedure;
var
    local_var: float;

begin
    { Access and update symbols }
    num_int := 42;
    num_float := 3.14;
    text_str := "Hello, world!";
    arr_int[5] := 100;
    push(stack_char, 'A');

    { Log symbol table entries }
    symbol_table.log_symbols();

    { Call a sub-program }
    my_procedure();
end;

procedure my_procedure;
begin
    { Access local symbol }
    local_var := 2.718;

    { Log symbol table entries }
    symbol_table.log_symbols();
end;

begin
    { Initialize symbol table }
    symbol_table := SymbolTable();

    { Declare and use symbols }
    num_int := 10;
    num_float := 3.14;
    text_str := "Hello";
    arr_int[1] := 5;

    { Log symbol table entries }
    symbol_table.log_symbols();

    { Call the main procedure }
    my_procedure();
end."""