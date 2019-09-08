######################### Prime Hunter (Python)

author = 'Roberto Bastone'
email = 'robertobastone93@gmail.com'

version = 1.01
# code

################################################### IMPORT

import time
from termcolor import colored

################################################### CLASS
class PrimeHunter:
    yes = {'Y','y','YES','yes','Yes'}
    no = {'N','n','NO','no','No'}

#### INITIALIZING
    def __init__(self):
        self.primenumbers_array = []
        self.execution_time_array = []
        print( colored("Initializing... Prime Hunter version " + str(version), 'blue') )
        print( colored("(Author: " + author+')', 'blue') )
        print( colored("For info - or anything else - please, feel free to reach me at " + email, 'blue') )

    def hunter(self):
        div = 2
        while True:
            #try:
                num = int(input("Type an integer, the hunter will tell whether it is a prime number:"))
                start_time = time.time()
                while  ( num % div != 0):
                    div +=  1
                if  num == div:
                    execution_time = time.time() - start_time
                    print("The Hunter says that " + str(num) + " is prime (hunting time: " + str(execution_time) + " s)")
                    self.primenumbers_array.append(num)
                    self.execution_time_array.append(execution_time)
                    self.keepOnHunting(self.yes,self.no)
                    break
                else:
                    print("The Hunter says that " + str(div) + " is the divisor of " + str(num) +" (hunting time: " + str(time.time() - start_time) + " s).")
                    self.keepOnHunting(self.yes,self.no)
                    break
            #except:
            #        print( colored("This is not an integer.",'red') )
            #        continue

    ### KEEP ON Hunting?
    def keepOnHunting(self, yes, no):
        while True:
            choice = input(">Do you want to hunt again? [y/n] \n").lower()
            if choice in yes:
                self.hunter()
                break
            elif choice in no:
                print( colored("Prime numbers found: ","blue"))
                print(*self.primenumbers_array, sep = ", ")
                print( colored("Execution time: ","blue"))
                print(*self.execution_time_array,sep = ",")
                self.sayingGoodbye()
                break
            else:
                print( colored(">Please, select [y/n] only",'yellow'))
                continue

    ### SAYING GOODBYE
    def sayingGoodbye(self):
        print( colored("Terminating... Prime Hunter version " + str(version),'blue') )
        print( colored("If you find any bug, please do not hesitate to contact me at "+ email,'blue') )
