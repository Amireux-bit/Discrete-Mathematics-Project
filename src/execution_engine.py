class Executor:
    def collect_variables(self, expr):
        if isinstance(expr, str):
            if expr.startswith('VAR_'):
                return {expr}
            return set()
        
        op = expr[0]
        if op == 'NOT':
            return self.collect_variables(expr[1])
        left_vars = self.collect_variables(expr[1])
        right_vars = self.collect_variables(expr[2])
        return left_vars.union(right_vars)
    
    def generate_truth_assignments(self, variables):
        sorted_vars = sorted(variables)
        if not sorted_vars:
            return [{}]

        first_var = sorted_vars[0]
        rest_vars = sorted_vars[1:]
        smaller_assignments = self.generate_truth_assignments(rest_vars)
        assignments = []
        for assignment in smaller_assignments:
            true_case = assignment.copy()
            true_case[first_var] = 'TRUE'
            assignments.append(true_case)

        for assignment in smaller_assignments:
            false_case = assignment.copy()
            false_case[first_var] = 'FALSE'
            assignments.append(false_case)
        return assignments

    def evaluate_expression(self, expr, state):
        if isinstance(expr, str):
            if expr == 'TRUE' or expr == 'FALSE':
                return expr
            if expr.startswith('VAR_'):
                return state[expr]
        
        op = expr[0]
        if op == 'NOT':
            operand_value = self.evaluate_expression(expr[1], state)
            if operand_value == 'TRUE':
                return 'FALSE'
            return 'TRUE'
        left_value = self.evaluate_expression(expr[1], state)
        right_value = self.evaluate_expression(expr[2], state)
        if op == 'AND':
            if left_value == 'TRUE' and right_value == 'TRUE':
                return 'TRUE'
            return 'FALSE'
        if op == 'OR':
            if left_value == 'TRUE' or right_value == 'TRUE':
                return 'TRUE'
            return 'FALSE'
        if op == 'IMPLIES':
            if left_value == 'TRUE' and right_value == 'FALSE':
                return 'FALSE'
            return 'TRUE'
    
    def verify_equivalence(self, original_expr, optimized_expr, line_num):
        variables = sorted(self.collect_variables(original_expr).union(self.collect_variables(optimized_expr)))
        assignments = self.generate_truth_assignments(variables)
        original_column = []
        optimized_column = []
        for state in assignments:
            original_column.append(self.evaluate_expression(original_expr, state))
            optimized_column.append(self.evaluate_expression(optimized_expr, state))

        return {
            'line': line_num,
            'variables_tested': variables,
            'ast_original_column': original_column,
            'ast_optimized_column': optimized_column,
            'is_equivalent': 'TRUE' if original_column == optimized_column else 'FALSE'
        }

    def execute_statement(self, ast, state, printed_output, line_num):
        stmt_type = ast[0]
        if stmt_type == 'LET':
            var_name = ast[1]
            expr = ast[2]
            state[var_name] = self.evaluate_expression(expr, state)
            return
        if stmt_type == 'IF':
            condition = ast[1]
            consequent = ast[2]
            if self.evaluate_expression(condition, state) == 'TRUE':
                self.execute_statement(consequent, state, printed_output, line_num)
            return
        if stmt_type == 'PRINT':
            var_name = ast[1]
            printed_output.append({'line': line_num, 'output': state[var_name]})
            return
        
    def collect_changed_expression_pairs(self, original_ast, optimized_ast, line_num):
        changed_pairs = []
        stmt_type = original_ast[0]
        if stmt_type == 'LET':
            original_expr = original_ast[2]
            optimized_expr = optimized_ast[2]
            if original_expr != optimized_expr:
                changed_pairs.append((original_expr, optimized_expr, line_num))
            return changed_pairs
        if stmt_type == 'IF':
            original_condition = original_ast[1]
            optimized_condition = optimized_ast[1]
            if original_condition != optimized_condition:
                changed_pairs.append((original_condition, optimized_condition, line_num))
            # recursively check the consequent statements for changes as well
            original_consequent = original_ast[2]
            optimized_consequent = optimized_ast[2]
            changed_pairs.extend(self.collect_changed_expression_pairs(original_consequent, optimized_consequent, line_num))
            return changed_pairs
        if stmt_type == 'PRINT':
            return changed_pairs
        
    def verify_and_execute(self, phase_2, phase_3):
        verifications = []
        state = {}
        printed_output = []

        # first verify every changed expression before executing any statement
        for original_line, optimized_line in zip(phase_2, phase_3):
            original_ast = original_line['ast']
            optimized_ast = optimized_line['ast']
            line_num = optimized_line['line']
            changed_pairs = self.collect_changed_expression_pairs(original_ast, optimized_ast, line_num)
            for original_expr, optimized_expr, expr_line_num in changed_pairs:
                verifications.append(self.verify_equivalence(original_expr, optimized_expr, expr_line_num))

        # then execute the optimized program after verification is complete
        for optimized_line in phase_3:
            optimized_ast = optimized_line['ast']
            line_num = optimized_line['line']
            self.execute_statement(optimized_ast, state, printed_output, line_num)

        return {
            'verifications': verifications,
            'final_state_dictionary': state,
            'printed_output': printed_output
        }