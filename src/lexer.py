import re 

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self):
        self.KEYWORDS_BOOLEANS_OPERATORS = {
            'let': 'LET', 'if': 'IF', 'then': 'THEN', 'print': 'PRINT',
            'T': 'TRUE', 'F': 'FALSE',
            'AND': 'AND', 'OR': 'OR', 'NOT': 'NOT', 'IMPLIES': 'IMPLIES',
        }

        self.SYMBOLS = {
            '=': 'EQ',
            '(': 'L_PAREN',
            ')': 'R_PAREN'
        }

        keyword_pattern = r'\b(' + '|'.join(re.escape(k) for k in self.KEYWORDS_BOOLEANS_OPERATORS.keys()) + r')\b'
        symbol_pattern = '|'.join(re.escape(s) for s in sorted(self.SYMBOLS.keys(), key=len, reverse=True))
        variable_pattern = r'\b[a-z]+\b' 
        whitespace_pattern = r'\s+'
        unknown_pattern = r'.'

        self.token_regex = re.compile(
            rf'(?P<KEYWORD>{keyword_pattern})|'
            rf'(?P<SYMBOL>{symbol_pattern})|'
            rf'(?P<VARIABLE>{variable_pattern})|'
            rf'(?P<WHITESPACE>{whitespace_pattern})|'
            rf'(?P<UNKNOWN>{unknown_pattern})'
        )
    
    def tokenize(self, input_code):
        all_tokens_by_line = []
        
        for line_num, line_content in enumerate(input_code.splitlines(), 1):
            line_tokens = []
            pos = 0 
            
            while pos < len(line_content):
                match = self.token_regex.match(line_content, pos)
                
                if not match:
                    raise LexerError(
                        f"Lexical error on line {line_num}, column {pos + 1}: "
                        f"Unexpected character '{line_content[pos]}'"
                    )
                
                lexeme = match.group(0)
                pos = match.end()
                
                if match.group('WHITESPACE'):
                    continue
                elif match.group('KEYWORD'):
                    line_tokens.append(self.KEYWORDS_BOOLEANS_OPERATORS[lexeme])
                elif match.group('SYMBOL'):
                    line_tokens.append(self.SYMBOLS[lexeme])
                elif match.group('VARIABLE'):
                    line_tokens.append(f"VAR_{lexeme.upper()}")
                elif match.group('UNKNOWN'):
                    raise LexerError(
                        f"Lexical error on line {line_num}: "
                        f"Unrecognized token '{lexeme}'"
                    )
                else:
                    raise LexerError(
                        f"Internal Lexer Error: Unhandled match type for '{lexeme}' "
                        f"on line {line_num}"
                    )
            
            if line_tokens:
                all_tokens_by_line.append({"line": line_num, "tokens": line_tokens})
        
        return all_tokens_by_line
    
if __name__ == "__main__":
    code = """let p = T
if (p AND ) then print p
"""
    lexer = Lexer()
    tokens = lexer.tokenize(code)
    for line in tokens:
        tokens_str = str(line['tokens']).replace("'", '"')
        print(f'" line ": {line["line"]}, " tokens ": {tokens_str}')