
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
    import DLListCP
    import tests.m3.DLList as DLList
    import random
    import traceback
    
    def TestCase():
        msg = "Testing DLList remove(i)..."
        try:
          answer_list = DLListCP.DLList()
          student_list = DLList.DLList()
          
          n = random.randint(6, 9)
          for i in range(n):
              letter = chr(65 + i)
              answer_list.append(letter)
              student_list.append(letter)
          msg += f"\n\nCreated list:  {str(answer_list)}"
          
          while answer_list.size() > 0:
              r = random.randint(0, answer_list.size() - 1)
              msg += "\n\n" + "-"*50
              msg += f"\n\nCalling remove({r}): "
              expected_removal = answer_list.remove(r)
              student_removal = student_list.remove(r)
              msg += "\n\tExpected element: " + str(expected_removal)
              msg += "\n\tReturned element: " + str(student_removal)
              msg += f"\n\tExpected list: {str(answer_list)}\t\tSize: {answer_list.size()}"
              msg += f"\n\tReceived list: {str(student_list)}\t\tSize: {student_list.size()}"
              r_bool = expected_removal != student_removal
              l_bool = str(answer_list) != str(student_list)
              s_bool = student_list.size() != answer_list.size()
              if r_bool or l_bool or s_bool: 
                msg += "\n\nTest FAILED."
                return TestOutput(passed=False, logs=msg)
                
          msg += "\n\nTest PASSED."
          return TestOutput(passed=True, logs=msg)    
    
        except Exception as e:
            msg += f"\nThe following unexpected error was raised:\n"
            msg += str(traceback.format_exc())
            msg += f"\n\nTest failed."
            return TestOutput(passed=False, logs=msg)
    
            

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146285.json", "w")
json.dump({"id": "146285", "passed": output.passed, "log": output.logs}, f)
f.close()
