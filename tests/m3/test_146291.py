
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
    import DLLDequeCP
    import DLLDeque
    import random
    
    def TestCase():
        try:
            answer_list = DLLDequeCP.DLLDeque()
            student_list = DLLDeque.DLLDeque()
    
    
            msg = f"Testing DLLDeque clear()...\n\nCreated empty deque: {student_list}\t\tSize: {student_list.size()}"
            
    
            for i in range(random.randint(5, 7)):
                ele = chr(random.randint(97, 122))
                dice = random.randint(1, 50)
                if dice % 2 == 0:
                  answer_list.add_last(ele)
                  student_list.add_last(ele)
                  msg += f"\n\nCalled add_last('{ele}')\n\tExpected:{str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived:{ str(student_list)}\t\tSize: {str(student_list.size())}"
                else:
                  answer_list.add_first(ele)
                  student_list.add_first(ele)
                  msg += f"\n\nCalled add_first('{ele}')\n\tExpected:{str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived:{ str(student_list)}\t\tSize: {str(student_list.size())}"
                  
                
                if student_list.size() != answer_list.size() or str(student_list) != str(answer_list):
                  msg += "\n\nTest failed."
                  return TestOutput(passed = False, logs = msg)
            answer_list.clear()
            student_list.clear()
            msg += f"\n\nCalled clear():\n\tExpected deque: {str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived deque: {str(student_list)}\t\tSize: {student_list.size()}"
            if str(student_list) != str(answer_list) or student_list.size() != answer_list.size():
              msg += "\n\nTest FAILED."
              return TestOutput(passed=False, logs=msg)
            else:
              msg += "\n\nTest PASSED."
              return TestOutput(passed=True, logs=msg)
        except Exception as e:
            msg += f"\n\nThe following unexpected error occurred:\n{e}"
            return TestOutput(passed=False, logs=msg)

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146291.json", "w")
json.dump({"id": "146291", "passed": output.passed, "log": output.logs}, f)
f.close()
