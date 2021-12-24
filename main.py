import part1
import part2
import part3
import part4
import part5

program = int()

while program != '':
  program = int(input("Which part are you testing? Type in 1, 2, 3, 4, or 5."))
  if program == 1:
    part1.parta()
  elif program == 2:
    part2.partb()
  elif program == 3:
    part3.partc()
  elif program == 4:
    part4.partd()
  elif program == 5:
    part5.parte()
