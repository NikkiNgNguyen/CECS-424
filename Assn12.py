import sys

#Take the arguments from the command line
args = str(sys.argv[1])

#Split the string arguments into a list called args_split
args_split = args.split()

#Create a stack and iniitate with a placeholder
#value to not get the IndexOut of error exception
stack = [] 
#stack = []

#Boolean function where a value is passed in
#returns true if the value is an operator 
#returns false if the value is a digit
def isOperator(value):
    if value == "+" or value == "-":
        return True
    if value == "*" or value == "/":
        return True
    
    return False 

#Iterate throught the prefixed expression in the args_split list
for i in reversed(args_split):

    #If the value is NOT an operator then it is a digit/expression therfore append to stack
    if isOperator(i) == False:
        #print("Operand: " + i)
        stack.append(i)
        #print("Adding " + i + " to stack")
        #print(stack)
    
    #If the value IS an operator then pop() two digits 
    #from the stack and create expression along with the 
    #detected operator symbol
    if isOperator(i) == True:
        
        #print("Operator: " + i)
        digit1 = stack.pop()
        #print("Removing " + digit1 + " from stack")

        
        if not stack:
            #print(stack)
            stack.append(digit1)
            #print("Since stack is empty adding back to the stack: " + digit1)

            #print("Creating expression")
            #expr = " " + i + " " +  digit1 
            #print("Adding expression " + expr + " to stack")

            #stack.append(expr) #Append the expression into the stack

            #print(stack)
            continue

        digit2 = stack.pop()
        #print("Removing " + digit2 + " from stack")

        #print("Update stack")
        #print(stack)


        #print("Creating expression")
        expr = "(" + digit1 + " " + i + " " + digit2 + ")"
        #print("Adding expression " + expr + " to stack")

        stack.append(expr) #Append the expression into the stack

        #print(stack)

expression = stack[0]
#print(expression)
#expression = stack
result = eval(expression)
print(expression + " = " + str(result))