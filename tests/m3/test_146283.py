
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
    import tests.m3.DLList as DLList
    import random
    
    def TestCase():
      student = DLList.DLList()
      
      try:
        idx = random.randint(0, 10)
        student.remove(idx)
        msg = f"Created empty DLList and called remove({idx}).\nResult: IndexError was not raised.\nTest failed."
        return TestOutput(passed=False, logs=msg)
      except IndexError:
        return TestOutput(passed=True, logs=f"Created empty DLList and called remove({idx}).\nResult: IndexError is correctly raised. \nTest passed.")
      except Exception as e:
        return TestOutput(passed=False, logs=f"Created empty DLList and called remove({idx}).\n\nThe following unexpected error occurred: {e}")

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146283.json", "w")
json.dump({"id": "146283", "passed": output.passed, "log": output.logs}, f)
f.close()
