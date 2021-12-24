
'''
______
PART 2
______

Run the code below. Fix it so that the program will print the product of the number 
and 10 in the formatted sentence that's already there, and the sum of 99 and the 
number in the formatted sentence that's already there.

'''

#code starts here
def partb():
  import time

  number = int(input("Enter a number: "))
  time.sleep(1)
  print("Ten times your number is", 10 * number)
  print("Ninety-nine more than your number is", 99 + number)


