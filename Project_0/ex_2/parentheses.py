#stack
class sTack:
    
    def __init__(self):
        #create one empty list
        self.stack_ = []

    def push(self, element):
        #push element 
        self.stack_.append( element)
    
    def pop(self):
        str = self.stack_.pop()
        return str

    def empty(self):
        if len(self.stack_) == 0:
            return True
        
        return False


######################


#read parentheses
symbol = input("GIVE US STRING WITH PARENTHESES\n")

stack_1 = sTack()

#the string from input is symbol
#we will change it in the list
lists = list(symbol)

#i is the seat from the list and start from zero
i = 0

while i < len(lists):
    str = lists[i]
    
    #if str is (,{,[ than push in stack, other check the previous str
    if str == '(' or str == '{' or str == '[':
        stack_1.push(str)
    else:
        previous_str = stack_1.pop()
        if str == ')' and previous_str == '(':
            i += 1
            continue
        elif str == ']' and previous_str == '[':
            i +=1
            continue
        elif str == '}' and previous_str == '{':
            i +=1
            continue
        else:
            print("The parentheses is wrong!!!")
            exit()

    i += 1

#if stack is empty, the parentheses is correct 
if stack_1.empty() == True:
    print("The parentheses is correct")
else:
    print("The parentheses is wrong!!!")