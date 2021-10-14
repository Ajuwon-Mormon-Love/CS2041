def first_function():
  myFile = input("Enter file: ")
  return myFile
def second_function(myFile):
  maainfile = open(myFile, "r")
  countone = 0
  counttwo = 0
  for line in maainfile:
    counttwo += 1
    words = line.split()
    countone += len(words)
  maainfile.close()
  return (counttwo, countone)
def main():
   myFile = first_function()
   (counttwo, countone) = second_function(myFile)
   print("The file contains {} lines and {} words." .format(counttwo, countone))
if __name__ == "__main__":
    main()