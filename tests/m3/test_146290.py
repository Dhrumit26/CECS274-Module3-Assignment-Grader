
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
    
            for i in range(random.randint(4, 6)):
                letter = chr(random.randint(65, 90))
                answer_list.add_first(letter)
                student_list.add_first(letter)
            msg = "Testing DLLDeque...\n\nCreating DLLDeque:\n" + str(answer_list) + "\tSize: " + str(answer_list.size())
            
    
            msg += f"\n\nRemoving all elements...."
            while answer_list.size() > 0:
              expected = answer_list.remove_last()
              received = student_list.remove_last()
              msg += f"\n\nCalled remove_last():\n\tExpected element: {expected}\n\tReceived element: {received}\n\tExpected deque: {str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived deque: {student_list}\t\tSize: {student_list.size()}"
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
f = open("/outputs/146290.json", "w")
json.dump({"id": "146290", "passed": output.passed, "log": output.logs}, f)
f.close()
