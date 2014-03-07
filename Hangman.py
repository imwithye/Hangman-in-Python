#################################################
# Author      : Ciel, imwithye
# Matric No   : U1220539K
# Group       : FS4
#################################################
import time
import random
easy = ['PHONE','HAPPY','APPLE','EARTH','GONGYIWEI']
normal = ['PYTHON','PIONEER','SINGAPORE','FATHER','MOTHER','GONGYIWEI']
#################################################
#clear          : This function will clear the whole screen with 30 blank lines
#
#pre-condition  : NONE
#post-condition : print out 30 blank lines
#################################################
def clear():
        for i in range(30):
                print ('\n')

#################################################
#hangmanInterface       : This function will print a basic interface of Hangman.
#                         The argument index means how many steps left.
#pre-condition          : index is the number of steps left and should GREATTER or EQUALS to 0!
#post-condition         : print out a basic interface of Hangman
#################################################
def hangmanInterface(index):
        if index==0:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('        / \  | ')
                print('             | ')
                print('     ________|_')
                return
        if index==1:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('        /    | ')
                print('             | ')
                print('     ________|_')
                return
        if index==2:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|\  | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==3:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('        /|   | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==4:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('         |   | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==5:
                print('         _____ ')
                print('         |   | ')
                print('         O   | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==6:
                print('         _____ ')
                print('         |   | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==7:
                print('         _____ ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==8:
                print('               ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('             | ')
                print('     ________|_')
                return
        if index==9:
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('     ________|_')
                return

#################################################
#startInterface : startInterface in the first user interface
#pre-condition  : input should be a interger between 1 to 3
#post-condition : this function will give out user's choice of gaming!
#################################################               
def startInterface():
        clear()
        print('####################')
        print('#                  #')
        print('#      Hangman     #')
        print('#                  #')
        print('####################')
        print('       1.Start     #')
        print('       2.Copyright #')
        print('       3.Exit      #')
        choice = input('Input Selection: ')
        return choice

#################################################
#startInterface2 : startInterface2 is the second interface user will see
#pre-condition   : input should be a integer between 1 to 3
#post-condition  : this function will give out user's choice of degree of difficulty
#################################################
def startInterface2():
        clear()
        print('####################')
        print('#                  #')
        print('#      Hangman     #')
        print('#                  #')
        print('####################')
        print('        1.Easy     #')
        print('        2.Normal   #')
        print('        3.Expert   #')
        choice = input('Input Selection: ')
        return choice
        
#################################################
#copyrightInterface : this function shows Copyright
#pre-condition      : input can be anything
#post-condition     : bring user back to first user interface
#################################################
def copyrightInterface():
        clear()
        print('####################')
        print('#                  #')
        print('#      Hangman     #')
        print('#                  #')
        print('####################')
        print('# Author: Ciel, imwithye')
        print('# School of Computer Engeineering')
        print('# Nanyang Technological University')
        print('key in any input to go back')
        input('')
        return
        
#################################################
#gameInterface  : gameInterface is the main user interface in gaming.
#pre-condition  : user's guess,miss_attempts should not greater than 6,misses is the history of mistake
#post-condition : print out the interface and return # if restart, return ! if call for
#                 help,return character else
#################################################
def gameInterface(guess,miss_attempts,misses,hintleft):
        clear()
        left = 9-miss_attempts
        hangmanInterface(left)
        print('###########################################')
        print('Word: ',end='')
        for i in guess:
                print(i,' ',end='')
        print()
        print('# Misses: ',end='')
        for i in misses:
                print(i,' ',end='')
        print()
        if left != 0:
            print('# You have ',left,' attempt(s) left')
            print('# You have ',hintleft,' hint(s) left')
            print('# input ? to get hint, # to restart and ! to see answer')
            _in = input('# Guess: ')
            if len(_in)>1:
                return '<'
            else: 
                if _in == '?' or _in == '#' or _in == '!':
                    return _in
                elif _in.isalpha():
                    return _in.upper()
                else:
                    return '<'
        else:
            print('# key in any input to Try Again!')
            _in = input('')
            return '#'

#################################################
#game           : game is the process of gaming. return false if game ends
#pre-condition  : the answer 'word' should be a string. hintMax should not be greater than 3
#post-condition : return false if game ends
#################################################
def game(word,hintMax):
        length = len(word)
        miss = 0
        hintTimes = 0
        misses = []
        guess = ['_' for i in range(length)]
        while True:
            operation = gameInterface(guess,miss,misses,hintMax-hintTimes)
            if operation == '#':
                print('Restarting...')
                time.sleep(3)
                return True
            elif operation == '?':
                if hintTimes<hintMax:
                    operation = hint(word,guess)
                    for i in range(length):
                        if word[i]==operation:
                            guess[i] = operation
                    hintTimes = hintTimes+1
                else:
                    print('# Can not get hint any more!Try your best!')
                    print('# Wait for 2 seconds')
                    time.sleep(2)
                    continue
            elif operation == '<':
                print('# Please input correctly!')
                print('# Wait for 2 seconds')
                time.sleep(2)
                continue
            elif operation == '!':
                clear()
                hangmanInterface(9-miss)
                print('###########################################')
                print('# The answer is',word)
                print('# wait fewer seconds to back to main menu')
                time.sleep(3)
                return False
            else:
                flag=0
                for i in range(length):
                    if word[i]==operation:
                        guess[i] = operation
                        flag = 1
                if flag==0:
                    miss = miss+1
                    if not operation in misses:
                        misses.append(operation)
                        
            if not '_' in guess:
                clear()
                hangmanInterface(9-miss)
                print('###########################################')
                print('# ',end='')
                for i in guess:
                    print(i,' ',end='')
                print()
                print('# Great!')
                time.sleep(3)
                return False
                                        

#################################################
#hint           : this function will return a correct character
#pre-condition  : word should be a string and guess should be a list
#post-condition : return back a correct character
#################################################
def hint(word,guess):
    length = len(word)
    for i in range(length):
        if guess[i]=='_':
            hintletter = word[i]
            return hintletter
                                        
#################################################
#getWord        : getWord function will get a get a word randomly
#                 Admin model can see the whole library and add words
#pre-condition  : sel is the degree of difficulty and should be less than 3
#                 if sel is greater then 3, that means Admin model!
#post-condition : return a word whose type is string.
#                 Or Admin model to access library!
#################################################
def getWord(sel):
    global easy,normal
    if sel==3:
        sel = 2
    if sel == 1:
        length = len(easy)
        index = random.randrange(0,length)
        return easy[index]
    elif sel == 2:
        length = len(normal)
        index = random.randrange(0,length)
        return normal[index]
    else:
        while True:
            clear()
            print('####################################')
            print('# Edit Library, input "exit()" to go back to main menu:')
            print('# 1.Show Library')
            print('# 2.Add word; Program will automatically select degree of difficulty')
            print('# 3.RESET to default.')
            print('####################################')
            selection = input('Selection: ')
            if selection == 'exit()':
                return 'DONE'
            elif selection == '1':
                print('_________________Library Files___________________')
                print('easy:')
                for i in easy:
                    print('    ',i)
                print()
                print('normal and expert:')
                for i in normal:
                    print('    ',i)
                print()
                print('_________________Library Files___________________')
                print('# key in any input to return')
                temp = input()
            elif selection == '2':
                while True:
                    print('_________________Addition___________________')
                    print('Use end() to end')
                    add = input()
                    if add != 'end()':
                        if add.isalpha():
                            degree = check(add)
                            if degree == 1:
                                if not add.upper() in easy:
                                    easy.append(add.upper())
                                    print('# Add successfully!')
                                else:
                                    print('# REPEAT! Words has ready added!')
                                        
                            else:
                                if not add.upper() in normal:
                                    normal.append(add.upper())
                                    print('# Add successfully!')
                                else:
                                    print('# REPEAT! Words has ready added!')
                        else:
                            print('# Please input correctly!')
                            continue
                    else:
                        print('_________________Addition___________________')
                        print('Addition Done')
                        time.sleep(2)
                        break
            elif selection == '3':
                    while True:
                        print('# Please be sure all data will be set to default!')
                        print('# key in "confirm()" to continue and key in anything else to cancel')
                        temp = input()
                        if temp=='confirm()':
                                easy = ['PHONE','HAPPY','APPLE','EARTH','GONGYIWEI']
                                normal = ['PYTHON','PIONEER','SINGAPORE','FATHER','MOTHER','GONGYIWEI']
                                print('# Successfully! wait 2 seconds.')
                                time.sleep(2)
                                break
                        else:
                                print('# Canceled! wait 2 seconds.')
                                time.sleep(2)
                                break
            else:
                continue

#################################################
#check          : Check the whether is easy or normal
#pre-condition  : addition should be a string only contenting alpha
#post-condition : return 1 if it is easy return 2 if it is normal
#################################################
def check(addition):
    sign = 0
    result = ['CHECK']
    for i in addition:
        if not i in result:
            result.append(i)
    sign = len(result)
    if sign>6:
        return 2
    else:
        return 1


#################################################
# mainfunction: Hangman's main function
# goal        : A command line Hangman game
# explain     : There are three degrees of difficulties to choose;
#               esay is a short word with repeat
#               nomal degree, the word will not be too long
#               expert will be very difficult.
#               nomal and expert will use the same library but expert's hint is less
# Author      : GONG YIWEI
# Matric No   : U1220539K
# Group       : FS4
#################################################
clear()
print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.")
print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |")
print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |")
print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |")
print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |")
print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|")
print('#######################################################')
print('#    key in admin to get in admin model!              #')
print('#    key in whosyourdaddy to get in special model!    #')
print('#    Warnning! admin mode is ONLY for developers!     #')
print('#    any bugs please report to                        #')
print('#              http://github.com/imwithye             #')
print('#    email: imwithye@gmail.com                        #')
print('#######################################################')
print()
print('#    Wait for starting...',end='')
print('<====',end='')
print('====',end='')
print('====',end='')
print('====',end='')
print('====> 100% DONE!')
input('#    Press Enter')

while True:
    gameProcess = True
    sel = startInterface()
    if sel=='1':
        while True:
            sel2 = startInterface2()
            if not sel2.isdigit():
                continue
            elif len(sel2)>1:
                continue
            elif int(sel2)>3 or int(sel2)<0:
                continue
            else:
                word = getWord(int(sel2))
                while gameProcess:
                    gameProcess = game(word,4-int(sel2))
                break
    elif sel=='2':
        copyrightInterface()
        continue
    elif sel=='3':
        break
    elif sel=='admin':
        getWord(4)
    elif sel=='whosyourdaddy':
                    word = 'HANGMAN'
                    temp = game(word,1000)      
    else:
        continue
