'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. Those two number will be the base and height of a triangle. 
The program will then output the area of that triangle. (Reminder: the area of a triangle can be calculated by (base * height)/2 ).

What should appear on the console when this code runs:

Enter the base: 8
Enter the height: 3
The area of the triangle is 12.0

'''
#start writing your code below
def partd():
  import time
  num0 = int(input("Enter the height of the triangle: "))

  num1 = int(input("Enter the height of the triangle: ")) 


  area = int((num0 * num1)/2)
  add = int((num0 + num1))
  question = input("Do you want the area (a) or the sum of the height and base (s) of the triangle? ")
  while question not in ["a", "s"]:
    print("Sorry, I did not understand the input.")
    time.sleep(1) 
    question = input("Do you want the area (a) or the sum of the height and  base (s) of the triangle? ")
  if question == 'a':
    print("PLEASE NOTE THE AREA IS AN INTEGER NUMBER")
    print("Fetching area...")
    time.sleep(1)
    print ("The area is: ", area)
  elif question == 's':
    print ("The sum is: ", add)

  