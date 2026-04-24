class OptimizerError(Exception):
    pass


class Optimizer:
    def optimize_expression(self, expr):
        # return if it's a variable or boolean constant
        if isinstance(expr, str):
            return expr

        op = expr[0]
        if op == 'NOT':
            operand = self.optimize_expression(expr[1])

            # double negation law
            if isinstance(operand, list) and operand and operand[0] == 'NOT':
                return self.optimize_expression(operand[1]) 
            
            # not true -> false, not false -> true
            if operand == 'TRUE':
                return 'FALSE'
            if operand == 'FALSE':
                return 'TRUE'

            # De Morgan's laws
            if isinstance(operand, list) and len(operand) == 3:
                inner_op = operand[0]
                left = operand[1]
                right = operand[2]

                if inner_op == 'AND':
                    return self.optimize_expression(['OR', ['NOT', left], ['NOT', right]])
                if inner_op == 'OR':
                    return self.optimize_expression(['AND', ['NOT', left], ['NOT', right]])
            
            return ['NOT', operand]

        else: # op in {'AND', 'OR', 'IMPLIES'}
            left = self.optimize_expression(expr[1])
            right = self.optimize_expression(expr[2])

            # implication law
            if op == 'IMPLIES':
                return self.optimize_expression(['OR', ['NOT', left], right])

            # universal bound laws, identity laws, idempotent laws, negation laws and absorption laws
            if op == 'AND':
                if left == 'FALSE' or right == 'FALSE':
                    return 'FALSE'
                if left == 'TRUE':
                    return right
                if right == 'TRUE':
                    return left
                if left == right:
                    return left
                if left == ['NOT', right] or right == ['NOT', left]:
                    return 'FALSE'
                if isinstance(right, list) and right[0] == 'OR':
                    if left == right[1] or left == right[2]:
                        return left
                if isinstance(left, list) and left[0] == 'OR':
                    if right == left[1] or right == left[2]:
                        return right
                return ['AND', left, right]

            if op == 'OR':
                if left == 'TRUE' or right == 'TRUE':
                    return 'TRUE'
                if left == 'FALSE':
                    return right
                if right == 'FALSE':
                    return left
                if left == right:
                    return left
                if left == ['NOT', right] or right == ['NOT', left]:
                    return 'TRUE'
                if isinstance(right, list) and right[0] == 'AND':
                    if left == right[1] or left == right[2]:
                        return left
                if isinstance(left, list) and left[0] == 'AND':
                    if right == left[1] or right == left[2]:
                        return right
                return ['OR', left, right]

    def optimize_statement(self, ast):
        # handle LET, IF, PRINT statements
        stmt_type = ast[0]
        if stmt_type == 'LET':
            return ['LET', ast[1], self.optimize_expression(ast[2])]
        if stmt_type == 'IF':
            return ['IF', self.optimize_expression(ast[1]), self.optimize_statement(ast[2])]
        if stmt_type == 'PRINT':
            return ['PRINT', ast[1]]

    def optimize(self, parsed_statements):
        optimized_statements = []
        for line in parsed_statements:
            optimized_ast = self.optimize_statement(line['ast'])
            optimized_statements.append({"line": line['line'], "ast": optimized_ast})
        return optimized_statements