import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    from src.parser import Parser
    from src.parser import ParserError
    from src.lexer import Lexer
    from src.lexer import LexerError

    test_file_path = os.path.join(os.path.dirname(__file__), 'test.txt')

    input_code = ""
    with open(test_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            input_code += line

    lexer = Lexer()
    try:
        tokens_by_line = lexer.tokenize(input_code)
        parser = Parser()
        ast = parser.parse(tokens_by_line)
        print(ast)
    except (LexerError, ParserError) as e:
        print(e)