
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
    import SLLQueue
    
    def TestCase():
      # TestCase must return a TestOutput Object
      # TestObject is initialized
      student_q = SLLQueue.SLLQueue()
      
      try:
        student_q.remove()
        msg = "Created empty SLLQueue and attempted to remove an element.\nResult: IndexError was not raised.\nTest failed."
        return TestOutput(passed=False, logs=msg)
      except IndexError:
        return TestOutput(passed=True, logs="Created empty SLLQueue and attempted to remove an element.\nResult: IndexError is correctly raised. \nTest passed.")
      except Exception as e:
        return TestOutput(passed=False, logs=f"Created empty SLLQueue and attempted to remove an element.\n\nThe following unexpected error occurred: {e}")

    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146280.json", "w")
json.dump({"id": "146280", "passed": output.passed, "log": output.logs}, f)
f.close()
