
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
    import DLListCP
    import tests.m3.DLList as DLList
    import random
    
    def TestCase():
        try:
          answer_list = DLListCP.DLList()
          student_list = DLList.DLList()
          n = random.randint(6, 10)
          elements = [chr(random.randint(65, 90)) for i in range(n)]
          
          for letter in elements:
            answer_list.append(letter)
            student_list.append(letter)
          msg = "Testing DLList...\n\nCreating an initial DLList:\n" + str(answer_list) + "\tSize: " + str(answer_list.size())
          
          ele = chr(random.randint(65, 90))
          while ele in elements:
            ele = chr(random.randint(65, 90))
          expected = answer_list.index_of(ele)
          received = student_list.index_of(ele)
          msg += f"\n\nCalled index_of('{ele}')\nExpected: {expected}\nReceived: {received}"
          if expected == received:
            msg += "\n\nTest PASSED."
            return TestOutput(passed=True, logs=msg)
          else:
            msg += "\n\nTest FAILED."
            return TestOutput(passed=True, logs=msg)
            
        except Exception as e:
          msg += f"The following unexpected error occurred:\n{e}"
          return TestOutput(passed=False, logs=msg)

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146288.json", "w")
json.dump({"id": "146288", "passed": output.passed, "log": output.logs}, f)
f.close()
