import datetime
print('Date: ',datetime.date.today().day)
print('Date: ',datetime.date.today())

import time
print('Time :',time.strftime('%H:%M:%S'))

odd=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
next='y'
while next=='y':
    cm = datetime.datetime.today().minute
    if cm in odd:
        print('Minute now is odd = ',cm)
    else:
        print('Minute now is not odd ')
    next=input('Are You Continue? (y/n)')

''' Seccond Method for Compare min by for loop'''
import random
birkac=int(input('How many repeat do you need? '))

for i in range(birkac):
    cm = datetime.datetime.today().minute
    if cm in odd:
        print('Minute now is odd = ',cm)
    else:
        print('Minute now is not odd ')
    if i<birkac:
         birsanieh = random.randint(0,59)
         print('Please wait ',birsanieh,'second')         
         time.sleep(birsanieh)




