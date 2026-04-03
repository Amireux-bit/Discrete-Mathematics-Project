class ParserError(Exception):
    def __init__(self, message, line_num=None):
        super().__init__(message)
        self.line_num = line_num

    def __str__(self):
        if self.line_num is not None:
            return f"Syntax Error on line {self.line_num}: {super().__str__()}"
        return f"Syntax Error: {super().__str__()}"

class Parser:
    def __init__(self):
        self.all_tokens_by_line = [] 
        self.current_line_tokens = [] 
        self.current_line_num = 0    
        self.pos = 0                  

    def parse(self, all_tokens_by_line_input):
        self.all_tokens_by_line = all_tokens_by_line_input
        
        parsed_statements = []
        
        for line_data in self.all_tokens_by_line:
            self.current_line_tokens = line_data['tokens']
            self.current_line_num = line_data['line']
            self.pos = 0 

            try:
                ast_for_line = self.parse_statement()

                if self.pos < len(self.current_line_tokens):
                    unexpected_token = self.current_token()
                    raise ParserError(f"Unexpected token '{unexpected_token}' after statement. "
                                      f"Check for missing operators or malformed expressions.", self.current_line_num)
                    
                parsed_statements.append({"line": self.current_line_num, "ast": ast_for_line})

            except ParserError as e:
                raise e 

        return parsed_statements

    def current_token(self):
        if self.pos < len(self.current_line_tokens):
            return self.current_line_tokens[self.pos]
        return None

    def consume(self, expected_type=None):
        current_token = self.current_token()
        if current_token is None:
            raise ParserError(f"Unexpected end of input. Expected {expected_type if expected_type else 'a token'}.", self.current_line_num)

        if expected_type and current_token != expected_type:
            if expected_type == 'R_PAREN':
                raise ParserError("Mismatched parentheses: missing right parenthesis ')'.", self.current_line_num)
            
            raise ParserError(f"Expected '{expected_type}', found '{current_token}'.", self.current_line_num)
        
        self.pos += 1
        return current_token

    def parse_statement(self):
        token_type = self.current_token()
        if token_type is None:
            raise ParserError("Unexpected end of input: expecting a statement.", self.current_line_num)

        if token_type == 'LET':
            return self.parse_let()
        elif token_type == 'IF':
            return self.parse_if()
        elif token_type == 'PRINT':
            return self.parse_print()
        else:
            return self.parse_expression()

    def parse_let(self):
        self.consume('LET')
        var_name_token = self.current_token()
        if var_name_token is None or not var_name_token.startswith('VAR_'):
            raise ParserError(f"Expected a variable name (e.g., VAR_P) after 'LET', found '{var_name_token}'.", self.current_line_num)
        var_name = self.consume() 
        
        self.consume('EQ')
        expr = self.parse_expression()
        return ['LET', var_name, expr]

    def parse_if(self):
        self.consume('IF')
        condition = self.parse_expression()
        self.consume('THEN')
        consequent = self.parse_statement() 
        return ['IF', condition, consequent]

    def parse_print(self):
        self.consume('PRINT')
        
        var_to_print_token = self.current_token()
        if var_to_print_token is None or not var_to_print_token.startswith('VAR_'):
            raise ParserError(f"Expected a variable name (e.g., VAR_P) after 'PRINT', found '{var_to_print_token}'.", self.current_line_num)
        
        var_name = self.consume() 
        return ['PRINT', var_name]


    def parse_expression(self):
        return self.parse_implies()

    def parse_implies(self):
        left = self.parse_or()
        while self.current_token() == 'IMPLIES':
            op = self.consume('IMPLIES')
            right = self.parse_or() 
            left = [op, left, right]
        return left

    def parse_or(self):
        left = self.parse_and()
        while self.current_token() == 'OR':
            op = self.consume('OR')
            right = self.parse_and()
            left = [op, left, right]
        return left

    def parse_and(self):
        left = self.parse_not()
        while self.current_token() == 'AND':
            op = self.consume('AND')
            right = self.parse_not()
            left = [op, left, right]
        return left

    def parse_not(self):
        if self.current_token() == 'NOT':
            op = self.consume('NOT')
            operand = self.parse_not() 
            return [op, operand]
        return self.parse_primary()

    def parse_primary(self):
        token = self.current_token()
        
        if token is None:
            raise ParserError("Unexpected end of input: missing expression or operand.", self.current_line_num)

        if token == 'L_PAREN':
            self.consume('L_PAREN') 
            expr = self.parse_expression() 
            self.consume('R_PAREN') 
            return expr
        elif token.startswith('VAR_') or token in {'TRUE', 'FALSE'}:
            return self.consume() 
        else:
            raise ParserError(f"Expected an expression (variable, boolean, or parenthesized expression), found '{token}'.", self.current_line_num)
