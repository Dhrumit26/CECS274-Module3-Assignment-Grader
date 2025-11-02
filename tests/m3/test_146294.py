
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
    import MaxQueueCP
    import MaxQueue
    import random
    
    def TestCase():
      try:
        test_input = [chr(random.randint(97, 107)) for j in range(10)]
        msg = f"Creating MaxQueue object 'm_queue'..."
        answer_q = MaxQueueCP.MaxQueue()
        student_q = MaxQueue.MaxQueue()
      
       
        for i in range(len(test_input)):
          letter = test_input[i]
          answer_q.add(letter)
          student_q.add(letter)
          msg += f"\n\nCalled m_queue.add('{letter}')\n\tExpected queue: {answer_q}\t\tSize: {answer_q.size()}\n\tReceived queue: {student_q}\t\tSize: {student_q.size()}"
          
          #Comparing the original queue contents
          expected_str = str(answer_q)
          received_str = str(student_q)
          
          if expected_str != received_str or answer_q.size() != student_q.size():
            msg += "\n\nTest FAILED."
            return TestOutput(passed=False, logs=msg)
          
    
        #Removing all elements in the queues      
        expected_removal = []
        actual_removal = []
    
        while answer_q.size() > 0:
          
          expected = answer_q.remove()
          received = student_q.remove()
          expected_str = str(answer_q)
          received_str = str(student_q)
          msg += f"\n\nCalled m_queue.remove()\n\tExpected element: {expected}\n\tReceived element: {received}\n\tExpected queue: {expected_str}\t\tSize: {answer_q.size()}\n\tReceived queue: {received_str}\t\tSize: {student_q.size()}"
          
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
f = open("/outputs/146294.json", "w")
json.dump({"id": "146294", "passed": output.passed, "log": output.logs}, f)
f.close()
