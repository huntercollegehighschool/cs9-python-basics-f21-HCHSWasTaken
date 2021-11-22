'''
______
PART 3
______
There are (at least) 6 errors in this code. Fix them so that it runs properly.

'''

#code starts here
def partc():
  import time

  number1 = int(input("Enter a number: "))
  time.sleep(0.5)
  number2 = int(input("Enter another number: "))
  time.sleep(0.5)
  print ("The sum of your numbers is", number1 + number2)
  time.sleep(0.5)
  print ("Seven times your second number is", 7 * number2)