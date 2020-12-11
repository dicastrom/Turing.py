
# L = {w#w: w∈{1,0}*}
def printTape(tape, index):
    print("Index is = ", index)
    print(len(tape) * "--"+'-')
    print("|", end="")
    for i in tape:
        print(i, end="|")
    print("\n", end="")
    print(len(tape) * "--"+'-')
    if (index == 0):
        print(" ^")
    else:
        print(index * "  ", "^")

str = input("Enter the string : ")

tape = []
tape[:] = str
tape.insert(0," ")
tape.insert(len(tape)," ")

#Adding to the tape to "pretend" its infinately long


Process = True
state =0
index = 0
operation = 0
# for i in range(0,10):
#     printTape(tape,i)


while(Process==True):
    if(state==-1):
        printTape(tape,index)
        print("REJECT")
        Process=False
    elif(state == 0):
        print("In state 0!")
        #print(index, " ->", tape[index])
        printTape(tape,index)
        index=index+1
        if(tape[index]==" "):
            print("TURE")
        while(tape[index]==' ' or tape[index]==''):
            print("In LOOP")
            index=index+1
            printTape(tape,index)
        if(tape[index]=='1'):
            tape[index]=' '
            index=index+1
            printTape(tape,index)
            #print("Current State = State 2 ")
            state=2
        elif (tape[index] == '0'):
            tape[index] = ' '
            index=index+1
            printTape(tape,index)
            #print("Current State = State 1 ")
            state = 1
        elif(tape[index]=='#'):
            printTape(tape,index)
            print("ACCEPT")
            break
    elif(state == 1):
        print("In state 1!")
        #print(index, " ->", tape[index])
        while(tape[index]=='1' or tape[index]=='0'):
            index = index + 1
            printTape(tape,index)
        if(tape[index]=='#'):
            state=3
    elif(state == 2):
        print("In state 2!")
        #print(index, " ->", tape[index])
        while (tape[index] == '1' or tape[index] == '0'):
            #print("in loop!")
            index = index + 1
            printTape(tape,index)
        if (tape[index] == '#'):
            state = 4
    elif(state==3):
        print("In state 3!")
        #print(index, " ->", tape[index])
        index=index+1
        #print(index, " ->", tape[index])
        while(tape[index]==' '):
            index = index + 1
            printTape(tape,index)
        if(tape[index]=='0'):
            state=5
        elif(tape[index]=='1'):
            state=-1
    elif(state==4):
        print("In state 4!")
        #print(index, " ->", tape[index])
        #print(index, " ->", tape[index])
        index=index+1
        while(tape[index]==' '):
            index = index +1
            printTape(tape,index)
        if(tape[index]=='1'):
            printTape(tape,index)
            state=6
        elif(tape[index]=='0'):
            state=-1
    elif(state == 5):
        print("In state 5!")
        #print(index, " ->", tape[index])
        printTape(tape,index)
        tape[index] = ' '
        while (tape[index] == ' '):
            index = index - 1
            printTape(tape, index)
        print(index, " ->", tape[index])
        if (tape[index] == '#'):
            state = 7
    elif(state == 6):
        print("In state 6!")

        #print(index, " ->", tape[index])
        printTape(tape,index)
        tape[index]=" "
        while(tape[index]==' '):
            index=index-1
            printTape(tape,index)
        print(index, " ->", tape[index])
        if(tape[index]=='#'):
            state=8
    elif(state ==7):
        print("In state 7!")
        #print(index, " ->", tape[index])
        index = index - 1
        printTape(tape,index)
        while (tape[index] == '1' or tape[index] == '0'):
            index = index - 1
            printTape(tape, index)
        state=0
    elif(state == 8):
        print("In state 8!")
        #print(index, " ->", tape[index])
        index = index - 1
        printTape(tape,index)
        while (tape[index] == '1' or tape[index] == '0'):
            index = index - 1
            printTape(tape, index)
        state=0










