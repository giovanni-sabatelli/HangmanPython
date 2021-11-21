import string
from typing import Type

def displayCurrStage(spriteList, noDelete = False):
  if noDelete != True:
    spriteList.pop(0)
  print(spriteList[0])

def spriteRes(desiredWidth):
  desiredWidth = round(desiredWidth/10)*10
  spacingWidth = (desiredWidth-6)//2
  return [
      f"""{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  """,
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth}/|   |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth}/|\  |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth}/|\  |{" "*spacingWidth}
  {" "*spacingWidth}/    |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
      f"""
{"-"*desiredWidth}

  {" "*spacingWidth} +~~~+{" "*spacingWidth}
  {" "*spacingWidth} |   |{" "*spacingWidth}
  {" "*spacingWidth} 0   |{" "*spacingWidth}
  {" "*spacingWidth}/|\  |{" "*spacingWidth}
  {" "*spacingWidth}/ \  |{" "*spacingWidth}
  {" "*spacingWidth}     |{" "*spacingWidth}""",
  ]

def config(option = True):
  if option == True:
    with open("D:\\OldFiles\\FullTop\\LeetcodeAttempt\\hangman\\config.txt", "r") as res:
      resSplit = res.readlines()
      resSplit = [resSplit[i].split(" = ") for i in range(len(resSplit))]
      return {k:int(v) for k, v in resSplit}
  try:
    with open("D:\\OldFiles\\FullTop\\LeetcodeAttempt\\hangman\\config.txt", "w+") as des:
      des.writelines(f"desiredWidth = {int(option)}")
  except ValueError:
    return "Error Code 0: Please Enter a Number!"

def wordDict(word):
  wordKeep = {x:[] for x in string.ascii_lowercase}; wordKeep.update(space = [])
  for y, z in enumerate(word.lower()):
    if z.isspace():
      wordKeep["space"].append(y)
    else:
      wordKeep[z].append(y)
  return wordKeep

#ord(guess) in list(range(65, 91)) or list(range(97, 123))
def guessHandler(word, charDict, guess, setup = False):
  if setup == True:
    return " ".join("_" if char.isalpha() else char for char in word)
  try:
    guess = guess.lower()
    if charDict[guess] == []:
      return False
    splitList = list(word)
    for pos in charDict[guess]:
      splitList[pos * 2] = guess
    return "".join(splitList)
  except KeyError:
    return "Error Code 1: Please Enter a Character!"
  
