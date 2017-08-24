from math import sqrt
import sys

def application():
    print "Welcome to the pythagorean theorem solver!"
    print "Please type this data to get your answer"
    side = raw_input("Whis side are we going to calculate?")
    if side == "c":
        sidea = int(raw_input("What is the length of side a?"))
        sideb = int(raw_input("What is the length of side b?"))
        result = sqrt(sideb * sideb + sidea * sidea)
        print "The result is %s " % result
    elif side == "b":
      sidea = int(raw_input("What is the length of side a?"))
      sidec = int(raw_input("What is the length of side c?"))
      result = sqrt(sidea * sidea - sidec * sidec)
      print "The result is %s " % result 
    elif side == "a":
      sideb = int(raw_input("What is the length of side b?"))
      sidec = int(raw_input("What is the length of side c?"))
      result = sqrt(sideb * sideb - sidec * sidec)
      print "The result is %s " % result 
    else:
      print "Please pick one of the abc sides"

def start():
    print "Welcome to the pythagorean theorem solver!"
    print "Please type this data to get your answer"
    decision = raw_input("Would you like to continue? if yes, press enter")
    if decision == "":
      application()
    else:
      print "Exiting program"
      sys.exit('5')
      
start()
        