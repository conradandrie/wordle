#imports
import time
import os
import sys
import random
from time import sleep
from random import randint

#colours
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'

#wordbank

wordbank = ['about','above','abuse','actor','acute','admit','adopt','adult','after','again','agent','agree','ahead','along','alter','among','anger','angle','angry','apart','apple','apply','aware','badly','baker','bases','basic','basis','beach','began','begin','begun','being','below','bench','billy','birth','black','blame','blind','block','blood','board','boost','booth','bound','brain','brand','bread','break','breed','brief','bring','broad','broke','brown','build','built','buyer','chest','chief','child','china','chose','civil','claim','class','clean','clear','click','clock','close','coach','coast','could','count','court','cover','craft','crash','cream','crime','cross','crowd','crown','curve','cycle','daily','dance','dated','dealt','death','dying','eager','exist','extra','faith','false','fault','fiber','field','fifth','fifty','fight','final','first','fixed','flash','fleet','floor','fluid','focus','force','forth','forty','funny','giant','given','glass','globe','japan','jimmy','joint','jones','judge','known','label','large','laser','later','laugh','layer','learn','lease','least','leave','legal','level','lewis','light','limit','links','lives','local','logic','loose','lower','lucky','lunch','lying','magic','major','maker','march','maria','match','maybe','mayor','meant','media','metal','month','moral','mouth','movie','music','needs','never','mewly','night','noise','north','noted','novel','nurse','occur','ocean','offer','often','order','other','ought','paint','panel','paper','party','peace','peter','phase','phone','photo','piece','pilot','pitch','place','prize','proof','proud','prove','queen','quick','quiet','quite','radio','seven','shall','shape','share','sharp','sheet','shelf','shell','shift','shirt','shock','shoot','short','shown','sight','since','sixth','sixty','sized','skill','sleep','slide','small','smart','smile','smith','smoke','solid','solve','sorry','sound','super','sweet','thick','thing','think','third','those','three','trend','trial','tried','tries','truck','truly','trust','truth','twice','upper','upset','urban','usage','usual','valid','value','video','voice','worth','would','wound','write','wrong','wrote','yield','young','youth','zebra']

with open("wordleword.txt") as file_object:
    wordleword = file_object.read()
counter=0

#fancy write
def clear(t):
  time.sleep(t)
def p(t):
  print(t)
def clear():
  os.system('clear')
def write(words):
  for char in words:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
clear()

done = False 
numb = 0

outcome = ''
word = wordbank[randint(0,len(wordbank)-1)]

write('Hello and welcome to... ')
time.sleep(1)
print('')
write(Cyan +'''      
┏┓┏┓┏┓╋╋╋╋╋╋┏┳┓
┃┃┃┃┃┃╋╋╋╋╋╋┃┃┃
┃┃┃┃┃┣━━┳━┳━┛┃┃┏━━┓
┃┗┛┗┛┃┏┓┃┏┫┏┓┃┃┃┃━┫
┗┓┏┓┏┫┗┛┃┃┃┗┛┃┗┫┃━┫
╋┗┛┗┛┗━━┻┛┗━━┻━┻━━┛'''+ White)
print('')
print('')
write('If the letter is ')
write(Green + 'Green' + White)
write(' then the letter is in the correct place.')
print('')
time.sleep(1.5)
write('If the letter is ')
write(yellow + 'Yellow' + White)
write(' then the letter is inside the word but in the wrong position.')
print('')
time.sleep(1.5)
print('')
print('')
write('For example, if the guess is ')
write(Green + 'T' + White + 'AS' + yellow + 'ER'+ White)
print('')
write('The "' + Green + 'T' + White + '" is in the right spot, The "AS" is not in the word and the "'+ yellow + 'ER'+ White + '" is in the word just in the wrong position.')
print('')
print('')
write("With the rules out of the way I think it's time to start!")
print('')
print('')

while done == False:
  write('Make your guess: ')
  print ('')
  print('')
  guess = input()
  guess = guess.lower()
  for x in wordleword:
    if x == guess:
      print("valid word")
  if len(guess) > 5 or len(guess) < 4:
    write('Only five letter words allowed please. ')
    print('')
  elif guess not in wordleword:
    write('That is not a valid word. ')
    print('')
    print('')
  else:
    numb += 1
    for letters in range(5):
      if guess[letters] not in word:
        outcome += guess[letters]
      elif guess[letters] == word[letters]:
        outcome += Green + guess[letters] + White
      else:
        outcome += yellow + guess[letters] + White
    print(outcome)
    print('')
    if guess == word.upper():
      write('You guessed it correctly. ')
      write('You did it in ' + Red + str(numb) + White +' trys. Good Job!')
      done = True 
    outcome = ""
