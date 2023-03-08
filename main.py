import random

questionnum = random.randint(1,9)  
print(questionnum)

class AnswerLineIndex:
  def __init__(self, startline=0, lastline=0):
    self.startline = startline
    self.lastline = lastline

firstQ = AnswerLineIndex(1,1)
secondQ = AnswerLineIndex(3,3)
thirdQ = AnswerLineIndex(5,5)
fourthQ = AnswerLineIndex(8,21)
fifthQ = AnswerLineIndex (24,30)
sixthQ = AnswerLineIndex(33,40)
seventhQ = AnswerLineIndex(43,51)
eigthQ = AnswerLineIndex(53,53)
ninthQ = AnswerLineIndex(55,55)


with open ("Answers.txt","r") as filevar:
  wholefile = filevar.read()
  splitted = wholefile.splitlines()
  #print(splitted)


  #Print Question and determine answer form

  with open ("Questions.txt","r") as filevariable:
    Questions = filevariable.read()
    splitqs = Questions.splitlines()

    questionline = splitqs[questionnum-1]
    questiontype = questionline[2]
    questiononly = questionline[5:]

    print("Question: " + questiononly + "\n")
    if questiontype == "S":
      answergiven = input("Short answer needed. Please enter the answer into the shell: ")
    if questiontype == "P":
      answergiven = input("Programming Q. Please do this on a seperate virtual environment and then enter 'show answer' to compare programs:  ")

  #Print answers


    
  start = 0
  end = 0

  if questionnum == 1:
    start = firstQ.startline
    end = firstQ.lastline
  if questionnum == 2:
    start = secondQ.startline
    end = secondQ.lastline
  if questionnum == 3:
    start = thirdQ.startline
    end = thirdQ.lastline
  if questionnum == 4:
    start = fourthQ.startline
    end = fourthQ.lastline
  if questionnum == 5:
    start = fifthQ.startline
    end = fifthQ.lastline
  if questionnum == 6:
    start = sixthQ.startline
    end = sixthQ.lastline
  if questionnum == 7:
    start = seventhQ.startline
    end = seventhQ.lastline
  if questionnum == 8:
    start = eigthQ.startline
    end = eigthQ.lastline
  if questionnum == 9:
    start = ninthQ.startline
    end = ninthQ.lastline
  
  start = int(start)
  end = int(end)


  if questiontype == "S":   #For short answer questions
    
    correctanswer = str(splitted[start-1])
    if answergiven == correctanswer: 
      print("That is correct. Rerun for next Q.")
    if answergiven != correctanswer:
      print("The correct answer is: ", correctanswer[4:])


  if questiontype == "P":
    if answergiven == "show answer": 
      for i in range(start-1,end+1):
        print(splitted[i] + "\n")
  

   
