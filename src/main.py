from lexer import Lexer, LexerError
from parser import Parser, ParserError
from optimizer import Optimizer, OptimizerError
import json
import sys

def main(test_file_path, output_file_path):
    input_code = ""
    with open(test_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            input_code += line

    lexer = Lexer()
    try:
        tokens_by_line = lexer.tokenize(input_code)
        parser = Parser()
        ast = parser.parse(tokens_by_line)
        optimizer= Optimizer()
        ast = optimizer.optimize(ast)
    except (LexerError, ParserError, OptimizerError) as e:
        print(e)