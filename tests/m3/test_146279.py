
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
    # To call a student's method, uncomment the following line and call <fileName>.<method>
    
    # import <insert student's fileName here>
    import SLLStackCP
    import SLLStack
    import random
    
    def TestCase():
      try:
        test_input = [chr(random.randint(97, 107)) for j in range(10)]
        msg = f"Creating SLLStack object 'sll_stack'..."
        answer_stack = SLLStackCP.SLLStack()
        student_stack = SLLStack.SLLStack()
      
       
        for i in range(len(test_input)):
          letter = test_input[i]
          answer_stack.push(letter)
          student_stack.push(letter)
          msg += f"\n\nCalled sll_stack.push('{letter}')\n\tExpected stack: {answer_stack}\t\tSize: {answer_stack.size()}\n\tReceived stack: {student_stack}\t\tSize: {student_stack.size()}"
          
          #Comparing the original stack contents
          expected_str = str(answer_stack)
          received_str = str(student_stack)
          
          if expected_str != received_str or answer_stack.size() != student_stack.size():
            msg += "\n\nTest FAILED."
            return TestOutput(passed=False, logs=msg)
          
    
        #Removing all elements in the queues      
        expected_removal = []
        actual_removal = []
    
        while answer_stack.size() > 0:
          
          expected = answer_stack.pop()
          received = student_stack.pop()
          expected_str = str(answer_stack)
          received_str = str(student_stack)
          msg += f"\n\nCalled sll_stack.pop()\n\tExpected element: {expected}\n\tReceived element: {received}\n\tExpected stack: {expected_str}\t\tSize: {answer_stack.size()}\n\tReceived stack: {received_str}\t\tSize: {student_stack.size()}"
          
          if expected_str != received_str or expected != received:
            msg += "\n\nTest FAILED."
            return TestOutput(passed=False, logs=msg)
    
        msg += "\nTest PASSED." 
        return TestOutput(passed=True, logs=msg)
    
      except Exception as e:
        msg += f"\n\nThe following unexpected error occurred:\n{e}"
        return TestOutput(passed=False, logs=msg)
        
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146279.json", "w")
json.dump({"id": "146279", "passed": output.passed, "log": output.logs}, f)
f.close()
