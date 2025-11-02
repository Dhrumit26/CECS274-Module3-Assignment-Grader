
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
    
            for i in range(random.randint(4, 6)):
                letter = chr(random.randint(65, 90))
                answer_list.append(letter)
                student_list.append(letter)
            msg = "Testing DLList...\n\nCreating an initial DLList:\n" + str(answer_list) + "\tSize: " + str(answer_list.size())
            
    
            for i in range(7):
                idx = random.randint(0, answer_list.size() - 1)
                ele = chr(random.randint(97, 122))
                answer_list.add(idx, ele)
                student_list.add(idx, ele)
                msg += f"\n\nCalled add({idx}, '{ele}')\n\tExpected:{str(answer_list)}\t\tSize: {answer_list.size()}\n\tReceived:{ str(student_list)}\t\tSize: {str(student_list.size())}"
                
                if student_list.size() != answer_list.size() or str(student_list) != str(answer_list):
                  msg += "\n\nTest failed."
                  return TestOutput(passed = False, logs = msg)
    
    
            msg += "\n\nTest passed."
            return TestOutput(passed=True, logs=msg)
        except Exception as e:
            msg += f"The following unexpected error occurred:\n{e}"
            return TestOutput(passed=False, logs=msg)

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146284.json", "w")
json.dump({"id": "146284", "passed": output.passed, "log": output.logs}, f)
f.close()
