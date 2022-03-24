import winsound
import time 

def playsound(word):
    ting = list(word)
    h=0
    for i in ting:
      word = ting[h]
      h = h+1
      if word == "-":
          print("long beep")
          winsound.Beep(500, 300)
      elif word ==".":
          print("short beep")
          winsound.Beep(500, 75)
      elif word =='/':
          print("space")
          winsound.Beep(37,700)    
      else:
        print("not owkring")  


morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '/':'/'
                    }

userInp = input("write a word: ").upper()
userInp1 = list(userInp)
print(userInp1)

x=0
print(len(userInp1))
for i in userInp1:
    word1 = morse_code_dict[userInp1[x]]
    print(userInp1[x])
    print(word1)
    playsound(word1)
    x = x+1
    time.sleep(1)
    print("\n")



