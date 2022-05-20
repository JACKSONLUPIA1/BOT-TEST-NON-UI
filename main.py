import random

wordArr = []
userGuessArr = []
debugArr = []
green = []
greenPos = []
yellowPos = []

wordGuess = "zebra"

with open('words.txt') as f:
    for line in f:
        wordArr.append(line.strip())

def removeYellow(arr):
    temp_arr = []
    yellowLen = int(input("How many yellow letters: "))
    if yellowLen == 27:
        for word in arr:
            temp_arr.append(word)
        return temp_arr
    for i in range(yellowLen):
        letterYellow = str(input("Letter: "))
    for word in arr:
        if letterYellow in word:
        # print("REMOVED Y: " + word)
            temp_arr.append(word)
    return temp_arr
    
def getPos(word):
    test_str = '|||||'
    for letter in word:
        pos = int(input("What is the position of letter " + letter + ": "))
        test_str = test_str[:pos] + letter + test_str[pos + 1:]
    return test_str
        
def getUserInput():
    green = []
    greenLen = int(input("How many green letters: "))
    for i in range(greenLen):
        letterGreen = str(input("Letter: "))
        green.append(letterGreen.lower())
    green_array_str = ''.join(map(str, green))
    return green_array_str

def searchWords(str_test, arr):
    temp_arr = []
    temp_arr2 = []
    temp_arr3 = []
    temp_arr4 = []
    pos_letter = []
    length = len(str_test)
    if length == 5:
        for letter in str_test:
            if letter != '|':
                pos_letter.append(letter + str(str_test.index(letter)))
    # SEARCHES THE FIRST LETTER
    if str_test != "|||||":
        for word in arr:
          if pos_letter[0][0] in word:
            if pos_letter[0][1] == str(word.index(pos_letter[0][0])):
              temp_arr.append(word)
    
        # IF A SECOND LETTER IS VALID, IT WILL RUN THROUGH AGAIN
        if len(pos_letter) > 1:
          for word in temp_arr:
            if pos_letter[1][0] in word and pos_letter[1][1] == str(word.index(pos_letter[1][0])):
              # print("REMOVED 2 : " + word)
              temp_arr2.append(word)
              
        # THIRD LETTER TEST
        if len(pos_letter) > 2:
          for word in temp_arr2:
            if pos_letter[2][0] in word:
              if pos_letter[2][1] == str(word.index(pos_letter[2][0])):
                temp_arr3.append(word)
        
        # FOUR LETTER TEST
        if len(pos_letter) == 4:
          for word in temp_arr3:
            if pos_letter[3][0] in word:
              if pos_letter[3][1] == str(word.index(pos_letter[3][0])):
                temp_arr4.append(word)
            
    if len(pos_letter) == 1:
      return temp_arr
    if len(pos_letter) == 2:
      return temp_arr2
    if len(pos_letter) == 3:
      return temp_arr3
    if len(pos_letter) == 4:
      return temp_arr4
    else:
        return arr

def removeNull(arr):
    null_arr = []
    temp_arr = []
    temp_arr2 = []
    temp_arr3 = []
    temp_arr4 = []
    temp_arr5  = []
    
    nullLen = int(input("How many letters not in word: "))
    for i in range(nullLen):
        letterNull = str(input("Letter: "))
        null_arr.append(letterNull)
    for word in arr:
        if null_arr[0] not in word:
            temp_arr.append(word)
    # 2 
    if nullLen > 1:
        for word in temp_arr:
            if null_arr[1] not in word:
                temp_arr2.append(word)
    # 3 
    if nullLen > 2:
        for word in temp_arr2:
            if null_arr[2] not in word:
                temp_arr3.append(word)
    #4
    if nullLen > 3:
        for word in temp_arr3:
            if null_arr[3] not in word:
                temp_arr4.append(word)
    #5 
    if nullLen > 4:
        for word in temp_arr4:
            if null_arr[4] not in word:
                temp_arr5.append(word)
    if nullLen == 1:
        return temp_arr
    if nullLen == 2:
        return temp_arr2
    if nullLen == 3:
        return temp_arr3
    if nullLen == 4:
        return temp_arr4
    if nullLen == 5:
        return temp_arr5

def findBest(arr):
    # random oper for now but acutal equation will be made later
    # use yellow words to figure the best word to try
    return random.choice(arr)
            
# 1
null = removeNull(wordArr)
# yellow = removeYellow(null)
green_test = getUserInput()
new_green_str = getPos(green_test)
search_test_idk = searchWords(new_green_str, null)
# print(search_test_idk)

# 2
confirm = int(input("Continue?: \n 0 = No \n 1 = Yes "))
if confirm == 1:
    print(findBest(search_test_idk))
    null1 = removeNull(search_test_idk)
    green_test1 = getUserInput()
    new_green_str1 = getPos(green_test1)
    search_test_idk1 = searchWords(new_green_str1, null1)
    # print(search_test_idk1)
else:
    print(search_test_idk)
confirm = int(input("Continue?: \n 0 = No \n 1 = Yes "))
# 3
if confirm == 1:
    print(findBest(search_test_idk1))
    null2 = removeNull(search_test_idk1)
    green_test2 = getUserInput()
    new_green_str2 = getPos(green_test2)
    search_test_idk2 = searchWords(new_green_str2, null2)
    # print(search_test_idk2)
else:
    print(search_test_idk1)
# 4
confrim = int(input("Continue?: \n 0 = No \n 1 = Yes "))
if confrim == 1:
    print(findBest(search_test_idk2))
    null3 = removeNull(search_test_idk2)
    green_test3 = getUserInput()
    new_green_str3 = getPos(green_test3)
    search_test_idk3 = searchWords(new_green_str3, null3)
    # print(search_test_idk3)
else:
    print(search_test_idk2)
# 5 
confirm = int(input("Continue?: \n 0 = No \n 1 = Yes "))
if confirm == 1:
    print(findBest(search_test_idk3))
    null4 = removeNull(search_test_idk3)
    green_test4 = getUserInput()
    new_green_str4 = getPos(green_test4)
    search_test_idk4 = searchWords(new_green_str4, null4)
    print("FINAL: " + str(search_test_idk4))
else:
    print(search_test_idk3)


