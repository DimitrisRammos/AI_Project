import csp
#mathomata me rergastirio h sto 1o slot h sto 2o slot
#tha prepei na desmeysoyme to epomeno slot an 1o ------> 2o
#otan  vlepo lab na ftiaxno ekstra mathima poy prepei na bei meta toi theoria
class BigProblem( csp.CSP):
    
    def __init__( HalfYear, Name_Lessons, names_teachers, Duskolo, Lab):
        
        variables = []
        domains = dict()
        neighbors = dict()
        constraints = []
        size = len( Name_Lessons)
        for i in range(size):
            lesson = Name_Lessons[i]
            variables.append( lesson)
        
        #exoume 21 meres
        #me 3 slot kathe mera
        #
        #px 1h mera -> 9-12, 12-3, 3-6
        #ara ena tuple (1, 9-12) (1, 12-3), (1, 3-6)
        #to proto stoixeio toy tuple dhlonei poia mera tis eksetastikis kai to 2o poio slot
        #ara 1...21 meres * 3 = 63 tuple synolika 
        SlotList = []
        for i in range( 21):
            t1 = ( i, "9-12")
            t2 = ( i, "12-3")
            t3 = ( i, "3-6")
            SlotList.append( t1)
            SlotList.append( t2)
            SlotList.append( t3)
            
        #for domains
        for i in range(size):
            lesson = Name_Lessons[i]
            halfyear = HalfYear[i]
            Slot = []
            for j in range(21):
                t = SlotList[j]
                Slot.append( t)
                t = SlotList[j+1]
                Slot.append( t)
                if Lab[i] != True:
                    t = SlotList[j+2]
                    Slot.append( t)

            domains[lesson] = Slot
        print(domains)        
        
        #####
        # for j in range(size):
                # if HalfYear[j] == halfyear:
                     
        
        super().__init__(variables, domains, neighbors, constraints)
        
#variables v1...vl
#domains d1....dn











#############################################################################
##                                                                         ##
##                                                                         ##
##                                kodikas                                  ##    
##                                                                         ##
##                                                                         ##
#############################################################################
with open("Files/" + "mathimata.csv") as file:
    lines = file.readlines()

Number_lessons = len(lines) -1 #beacause the first is information
Name_Lessons = []
names_teachers = []
Eksamino = []
Duskolo = []
Lab = []
is_the_first = True
for line in lines:
    
    #beacause the first is information
    if is_the_first == True:
        is_the_first = False
        continue
    
    line = line.strip()
    length = len(line)
    num_for_other = 0
    previous_start = 0
    
    for i in range(length):
        if line[i] == ",":
            if num_for_other == 0 :
                if previous_start == i-1:
                   Eksamino.append( line[0])
                else: 
                    eksamino = int(line[previous_start:i-1])
                    Eksamino.append(eksamino)
            
            elif num_for_other == 1:
                
                word = line[previous_start:i-1]
                Name_Lessons.append(word)
            
            elif num_for_other == 2:
                
                word = line[previous_start:i-1]
                names_teachers.append(word)
            
            elif num_for_other == 3:
                
                duskolo = bool(line[previous_start:i-1])
                Duskolo.append(duskolo)
                
                lab = bool(line[i+1:length])
                Lab.append( lab)
                break
                
                
            previous_start = i+1
            num_for_other+=1

for i in range( Number_lessons):
    print(Eksamino[i], Name_Lessons[i], names_teachers[i], Duskolo[i], Lab[i])
    
    
#ok tora exo diavasei ta panta kai ta exo xorisei se pinakes
# def __init__(self, variables, domains, neighbors, constraints):
#  csp.CSP CS( variables, domains, neighbors, constraints)

# A CSP is specified by the following inputs:
#         variables   A list of variables; each is atomic (e.g. int or string).
#         domains     A dict of {var:[possible_value, ...]} entries.
#         neighbors   A dict of {var:[var,...]} that for each variable lists
#                     the other variables that participate in constraints.
#         constraints A function f(A, a, B, b) that returns true if neighbors
#                     A, B satisfy the constraint when they have values A=a, B=b
                    
problem = BigProblem( Eksamino, Name_Lessons, names_teachers, Duskolo, Lab)
