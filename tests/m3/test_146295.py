
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
      # TestCase must return a TestOutput Object
      # TestObject is initialized
      try:
          msg = "Creating an empty MaxQueue...\n"
          answer_queue = MaxQueueCP.MaxQueue()
          student_queue = MaxQueue.MaxQueue()
    
          test_input = []
          
          for i in range(2):
            integer = random.randint(0, 100)
            answer_queue.add(integer)
            student_queue.add(integer)
            test_input.append(integer)
            msg += f"\nAdding value {integer}"
    
          r = random.randint(300, 350)  #first max expected
          answer_queue.add(r)
          student_queue.add(r)
          test_input.append(r)
          msg += f"\nAdding value {r}"
    
          for i in range(3):
            integer = random.randint(0, 100)
            answer_queue.add(integer)
            student_queue.add(integer)
            test_input.append(integer)
            msg += f"\nAdding value {integer}"
    
    
          r = random.randint(200, 250)  #second max expected
          answer_queue.add(r)
          student_queue.add(r)
          test_input.append(r)
          msg += f"\nAdding value {r}"
    
          for i in range(2):
            integer = random.randint(0, 100)
            answer_queue.add(integer)
            student_queue.add(integer)
            test_input.append(integer)
            msg += f"\nAdding value {integer}"
    
          r = random.randint(110, 150)  #third max expected
          answer_queue.add(r)
          student_queue.add(r)
          test_input.append(r)
          msg += f"\nAdding value {r}"
    
    
          expected_queue = str(answer_queue)
          actual_queue = str(student_queue)
    
    
    
          #Comparing the original queue contents
          queue_is_correct = expected_queue.replace(' ', '') == actual_queue.replace(' ', '')
      
          
          msg += "\n\nExpected queue: " + str(test_input) +  "...\nStudent queue: " + str(student_queue)
    
          max1_expected = answer_queue.max()
          max1_returned = student_queue.max()
    
    
          msg += "\nExpected max: " + str(max1_expected) + "\nReturned max: " + str(max1_returned)
          msg += "\n\n" + "-"*50
    
          #----------------------------------------------------------- 
          #Removing 3 elements     
          expected_removal_1 = ""
          actual_removal_1 = ""
    
          for i in range(3):
            expected_removal_1 += str(answer_queue.remove()) + " "
    
          for i in range(3):
            actual_removal_1 += str(student_queue.remove()) + " "
    
          msg += "\n\nRemoving three elements..."+ "\nExpected order of removal: " + str(expected_removal_1) + "\nReturned order of removal: " + str(actual_removal_1)
          msg += "\n\nExpected Queue: " + str(answer_queue) + "\nResult: " + str(student_queue)
    
          max2_expected = answer_queue.max()
          max2_returned = student_queue.max()
          msg += "\n\nExpected max: " + str(max2_expected) + "\nReturned max: " + str(max2_returned)
          msg += "\n\n" + "-"*50
    
          #-----------------------------------------------------------
          #Removing 4 elements     
          expected_removal_2 = ""
          actual_removal_2 = ""
    
          for i in range(4):
            expected_removal_2 += str(answer_queue.remove()) + " "
    
          for i in range(4):
            actual_removal_2 += str(student_queue.remove()) + " "   
    
          msg += "\n\nRemoving four elements..."+ "\nExpected order of removal: " + str(expected_removal_2) + "\nReturned order of removal: " + str(actual_removal_2)
          msg += "\n\nExpected MaxQueue: " + str(answer_queue) + "\nReceived MaxQueue: " + str(student_queue)    
    
          max3_expected = answer_queue.max()
          max3_returned = student_queue.max()
    
          msg += "\n\nExpected max: " + str(max3_expected) + "\nReturned max: " + str(max3_returned)     
          msg += "\n\n" + "-"*50
    
          #Comparing the order of removed queue elements
          removal_is_correct = actual_removal_1 == expected_removal_1 and actual_removal_2 == expected_removal_2
          max1_bool = max1_expected == max1_returned
          max2_bool = max2_expected == max2_returned
          max3_bool = max3_expected == max3_returned
    
    
          maxima_are_correct = max1_bool and max2_bool and max3_bool
          print(maxima_are_correct)
          print(queue_is_correct)
          print(removal_is_correct)
    
          if (queue_is_correct and removal_is_correct and maxima_are_correct):
            msg += "\n\nTest PASSED." 
            return TestOutput(passed=True, logs=msg)
          elif not queue_is_correct:
            msg += "\n\nQueue is incorrect.\n\nTest FAILED." 
            return TestOutput(passed=False, logs=msg)
          elif not removal_is_correct:
            msg += "\n\nRemoval order is incorrect.\n\nTest FAILED." 
            return TestOutput(passed=False, logs=msg)
          else:  
            msg += "\n\nAt least one max is incorrect.\n\nTest FAILED." 
            return TestOutput(passed=False, logs=msg)
      except Exception as e:
          msg += f"\nAn unexpected error was raised:\n\n{str(e)}\n\nTest FAILED."
          return TestOutput(passed = False, logs = msg)
    output = TestCase()
    assert(isinstance(output, TestOutput))
except Exception as e:
    errorLogs = traceback.format_exc()
    output = TestOutput(False, str(errorLogs))
f = open("/outputs/146295.json", "w")
json.dump({"id": "146295", "passed": output.passed, "log": output.logs}, f)
f.close()
