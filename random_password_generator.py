#import random and string
from utill_functions import *
import random
#make a funtion for random password generator
def make_password():
    #return string ascii lower as a string
    leng=10
    lowwerc=True
    upperc=True 
    symbol=True 
    num=True 
    #make a loop in range of 5
    for _ in range(5):
        #make counter 0 and make password set start and starter
        counter=0
        password_set={"start","starter"}
        #make password set remove start and starter
        password_set.remove("start")
        password_set.remove("starter")
        #if symbol is true then make random randint 1 thorugh 4
        if symbol:
            rand1=random.randint(1,4)
            #if the random number is 1,make a random randint 33-47
            if rand1==1:
                rand2=random.randint(33,47)
            #if random is 2 make a random number form 58 through 64
            if rand1==2:
                rand2=random.randint(58,64)
            #if random number is 3 make the computer choose a number 91-96
            if rand1==3:
                rand2=random.randint(91,96)
            #if random number is 4 make random randint 123-126
            if rand1==4:
                rand2=random.randint(123,126)
            #maake password set add character from rand2
            password_set.add(chr(rand2))
            #make counter add one 
            counter+=1
        #if upper case is real add the chracter from numbers to readable chracter and add 1 to the counter
        if upperc:
            password_set.add(chr(random.randint(65,90)))
            counter+=1
        #if lower case is real 
        if lowwerc:
            #make password set add charters from random number and add 1 to the counter
            password_set.add(chr(random.randint(97,122)))
            counter+=1
        #if num is read add a chrater to password set and add one to the counter
        if num:
            password_set.add(chr(random.randint(48,57)))
            counter+=1
        #make counter 2 be counter 
        counter2=counter
        #make a loop with counter 2 ! be lenght 
        while counter2!=leng:
            #make random 3 be random randint 1 through 4
            rand3=random.randint(1,4)
            #if random 3 is one and symbol make rand 1 pick a random number 1-4
            if rand3==1 and symbol:
                rand1=random.randint(1,4)
                #if rand1 is one make rand2 be a random number from 33-47
                if rand1==1:
                    rand2=random.randint(33,47)
                #if rand1 is 2 make rand2 pick a number from 58-64
                if rand1==2:
                    rand2=random.randint(58,64)
                #if rand1 is 3 make rand2 pick a number from 91-96
                if rand1==3:
                    rand2=random.randint(91,96)
                #if rand1 is 4 make rand 2 choose a random number from 123-126
                if rand1==4:
                    rand2=random.randint(123,126)
                #add character to password set and add one to counter2
                password_set.add(chr(rand2))
                counter2+=1
            #if rand3 is 2 and uppercase
            if rand3==2 and upperc:
                #make password set add charater with random number and add one to counter2
                password_set.add(chr(random.randint(65,90)))
                counter2+=1
            #if random3 is 3 and lowercase make password set add character with random number
            if rand3==3 and lowwerc:
                password_set.add(chr(random.randint(97,122)))
                counter2+=1
            #if rand3 is 4 and num add to password set the chracters with random numbers
            if rand3==4 and num:
                password_set.add(chr(random.randint(48,57)))
                counter2+=1
        #make out be ""
        out=""
        #make a while loop for x in password set
        for x in password_set:
            #make out be out with x,return out 
            out=f"{out}{x}"
        return(out)
