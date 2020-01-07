import sys 
import re
import itertools as ite
import random
'''
args = str(sys.argv[1])
args_split = args.split(" ")
number = args_split[0]
numbers = [] #List to hold the numbers from Command Line
calc = args_split[1] #Variable to hold the number to evaluate expressions to (gotten from Command Line)
'''
num, target = (int(x) for x in sys.argv[1:])
count = 1
print(num, target)
numList = list(str(num))

#Get each value from number argument and add to a list called numbers
#for i in number:
 #   numbers.append(i)
resultList = []


def generateExpressions(digits):
    str1 = ""
    
    operators = ['+', '-', '*']
    combos = ite.combinations_with_replacement(operators, len(digits))

    for i in combos:
        combo2 = ite.permutations(i, len(digits))
        
        combo3 = list(set([i for i in combo2]))
           
        for m in combo3:
            evalNum([sub[j] for j in range(len(m)) for sub in [m, digits]])
        


def evalNum(func):
    if(func[0] == '+' or func[0] == '*'):
        func[0] = ""
    elif (func[0] == '-'):
        func[0] = ""
        func[1] = "-" + func[1]
    #print(func)
    str1 = ""
    for i in func:
        str1 = str1 + i
    result = eval(str1)
    if (result == 0):
        resultList.append(str1)
    
def segment(numl):
    def sub(n):
        elements = len(numl)
        if len(n) == 0:
            yield []
        for i in range(1, min(elements, len(n) + 1)):
            for s in sub(n[i:]):
                yield [''.join(n[:i])] + s
                #digits = list(sub(numl))
                #generateExpressions(digits)
                #print(digits)
                #print(generateExpression(digits))
    return list(sub(numl))

    # And if you want a list of strings:
def str_segment(nl):
    return [' '.join(n) for n in segment(nl)]

r = segment(numList)

for i in r:
    generateExpressions(i)

resultList = list(set(resultList))

print(len(resultList))
#for i in range(0,200):
    #print(i, resultList[i])
    
