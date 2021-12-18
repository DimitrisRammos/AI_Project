import csp

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