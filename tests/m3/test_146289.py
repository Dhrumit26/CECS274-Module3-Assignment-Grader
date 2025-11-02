
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
    
    
            msg = f"Testing DLLDeque add_last(x)...\n\nCreated empty deque: {student_list}\t\tSize: {student_list.size()}"
            
    
            for i in range(random.randint(3, 5)):
                ele = chr(random.randint(97, 122))
                answer_list.add_last(ele)
                student_list.add_last(ele)
                msg += f"\n\nCalled add_last('{ele}')\n\tExpected:{str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived:{ str(student_list)}\t\tSize: {str(student_list.size())}"
                
                if student_list.size() != answer_list.size() or str(student_list) != str(answer_list):
                  msg += "\n\nTest failed."
                  return TestOutput(passed = False, logs = msg)
            msg += f"\n\nRemoving all elements...."
            while answer_list.size() > 0:
              expected = answer_list.remove_first()
              received = student_list.remove_first()
              msg += f"\n\nCalled remove_first():\n\tExpected element: {expected}\n\tReceived element: {received}\n\tExpected deque: {str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived deque: {student_list}\t\tSize: {student_list.size()}"
              if expected != received or str(answer_list) != str(student_list) or answer_list.size() != student_list.size():
                msg += "\n\nTest FAILED."
                return TestOutput(passed=False, logs=msg)
            msg += "\n\nTest passed."
            return TestOutput(passed=True, logs=msg)
        except Exception as e:
            msg += f"\n\nThe following unexpected error occurred:\n{e}"
            return TestOutput(passed=False, logs=msg)

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146289.json", "w")
json.dump({"id": "146289", "passed": output.passed, "log": output.logs}, f)
f.close()
