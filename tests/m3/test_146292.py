
import json
import traceback
import os

class TestOutput:
    def __init__(self, passed, logs):
        assert (isinstance(passed, bool))
        assert (isinstance(logs, str))
        self.passed = passed
        self.logs = logs

try:
    import Calculator
    import random
    from calc_tester import uses_sll
    from expression_builder import build_math_expr, generate_balanced_expr
    
    
    def TestCase():
      msg = "Testing Calculator balanced_parens()..."
      try:
        # Checking if method uses SLLQueue in balanced_parens
        if not uses_sll("Calculator.py"):
          msg += "\n\nbalanced_parens() uses data structures other than SLLStack to perform operation.\n\nTest FAILED."
          return TestOutput(passed=False, logs=msg)
        
        # Generating balanced expression
        greeks = ['alpha', 'beta', 'omega', 'tau', 'epsilon', 'lambda', 'eta', 'pi']
        variables = [x + '_' + str(i) for x in greeks for i in range(0, 21)]
        expr = generate_balanced_expr(3, variables)
        
        # Creating calculator and calling balanced_parens
        calculator = Calculator.Calculator()
        is_balanced = calculator.balanced_parens(expr)
    
      # Creating feedback
        msg += f"\n\nExpression: {expr}"
        msg += "\nExpected: True"
        msg += f"\nReturned: {is_balanced}"
    
        # Test determination
        if (is_balanced):
          msg += "\nTest passed."
          return TestOutput(passed=True, logs=msg)
        else:
          msg += "\nTest failed."
          return TestOutput(passed=False, logs=msg)
    
      except Exception as e:
        msg += f"\n\nThe following unexpected error occurred:\n{e}"
        return TestOutput(passed=False, logs=msg)

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146292.json", "w")
json.dump({"id": "146292", "passed": output.passed, "log": output.logs}, f)
f.close()
