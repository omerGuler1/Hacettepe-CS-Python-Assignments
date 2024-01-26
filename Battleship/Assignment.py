import os
import sys
input_files = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]  
f = open("Battleship.out", "w")
a = []
try:                          # Check if the entered inputs match the real ones. 
    all_files_exist = True 
    for file in input_files:
        if not os.path.exists(file):
            all_files_exist = False
            a.append(file)
    if all_files_exist == False:
        raise IOError
        
except IOError:  
  if len(a) > 1:    # works when more than one input entered wrong
    print("IOError: input files {} are not reachable.".format(", ".join(a)))
    f.write("IOError: input files {} are not reachable.\n".format(", ".join(a)))
    exit()
  else:             # works when a file is mistyped
    print("IOError: input file {} is not reachable.".format(a[0]))
    f.write("IOError: input file {} is not reachable.\n".format(a[0]))
    exit()

    ####  to gather data from files
with open(sys.argv[1]) as f1:
    data1 = f1.readlines()
with open(sys.argv[2]) as f2:
    data2 = f2.readlines()
with open(sys.argv[3]) as f3:
    bomb1 = f3.readlines()
with open(sys.argv[4]) as f4:
    bomb2 = f4.readlines()

player1_hidden_board = {}
dict1 = {}
player2_hidden_board = {}

for i in range(1,11):    # create boards full of "-" to play 
    player1_hidden_board[i] = ["-"]*10
    player2_hidden_board[i] = ["-"]*10

dict_real = {}

dict2 = {}
v = []
###  get rid of the "\n" in the lines if any, then create a list separated by ";"
for i in [line.replace("\n","").split(";") for line in data1]:
    v.append(i)
for i in range(1,11):
    dict2[i] = v[i-1]  # create temporary dict. which includes ships units coordinates

dict_real["player1's_board"] = dict2

v = []
dict3 = {}
for i in [line.replace("\n","").split(";") for line in data2]:
    v.append(i)
for i in range(1,11):
    dict3[i] = v[i-1]
    
dict_real["player2's_board"] = dict3
##### dict_real includes all ships units coordinates for two side

###  get rid of the "\n" in the lines if any, then create a list separated by ";"
bomb1 = ''.join(bomb1)
bomb1 = bomb1.replace("\n","").split(";")

bomb2 = ''.join(bomb2)
bomb2 = bomb2.replace("\n","").split(";")

################# get spesific coordinates for ships
def get_ships(board):
    ships = {}
    for row in board:
        for col in range(len(board[row])):  # len(board[row] == 10) always true but this more sensible
            if board[row][col] != '':
                if len(board[row][col]) > 1:  # if ships overlap, kaboom
                    print("kaBOOM: run for your life!")
                    f.write("kaBOOM: run for your life!")
                    exit()
                if board[row][col] not in ships:
                    ships[board[row][col]] = []
                ships[board[row][col]].append((row, col))
    return ships

ships1 = get_ships(dict_real["player1's_board"])
ships2 = get_ships(dict_real["player2's_board"])

####### seperate Patrol boats like [(1,2),(1,3), (4,5), 3,5] to [[(1,2),(1,3)], [(4,5),(3,5)]]
j = []
for i,k in ships1["P"]:     # ships1["P"] have tuples 
    for x,y in ships1["P"]:
        v = []
        if i == x and abs(k-y) == 1 or k == y and abs(i-x) == 1:
            v.append((i,k))
            v.append((x,y))
        if v != []:
            j.append(v)

m = []
for i in j:
    i.sort()
    m.append(i)

m = set(map(tuple, m))
m = list(map(list, m))
ships1["P"] = m  ### done
####### do the same for player2
j = []
for i,k in ships2["P"]:
    for x,y in ships2["P"]:
        v = []
        if i == x and abs(k-y) == 1 or k == y and abs(i-x) == 1:
            v.append((i,k))
            v.append((x,y))
        if v != []:
            j.append(v)

m = []
for i in j:
    i.sort()
    m.append(i)      

m = set(map(tuple, m))
m = list(map(list, m))
ships2["P"] = m
### seperate the battle ships
l0 = []
l = []
l1 = []
for i in ships1["B"]:
    for a in ships1["B"]:
        for s in ships1["B"]:
            for d in ships1["B"]:
                if i[0] == a[0] == s[0] == d[0] and i[1] != a[1] and i[1] != s[1] and i[1] != d[1]:
                    l.append(i)
                elif i[1] == a[1] == s[1] == d[1] and i[0] != a[0] and i[0] != s[0] and i[0] != d[0]:
                    l1.append(i)
l = [*set(l)]
l1 = [*set(l1)]
for i in l:
    if len(l) - len(l1) == 1 and i in l1:
        l.remove(i)
    elif len(l1) - len(l) == 1 and i in l1:
        l1.remove(i)
l0.append(l)
l0.append(l1)
ships1["B"] = l0

c = ["-"]
b = ["-","-"]
d = ["-"]
s = ["-"]
p = ["-","-","-","-"]

c2 = ["-"]
b2 = ["-","-"]
d2 = ["-"]
s2 = ["-"]
p3 = ["-","-","-","-"]

uu = [] 
yy = []
tt = []
for i in ships2["B"]:
    for a in ships2["B"]:
        for q in ships2["B"]:
            for ee in ships2["B"]:
                if i[0] == a[0] == q[0] == ee[0] and i[1] != a[1] and i[1] != q[1] and i[1] != ee[1]:
                    yy.append(i)
                elif i[1] == a[1] == q[1] == ee[1] and i[0] != a[0] and i[0] != q[0] and i[0] != ee[0]:
                    tt.append(i)
yy = [*set(yy)]
tt = [*set(tt)]
for i in l:
    if len(yy) - len(tt) == 1 and i in l1:
        yy.remove(i)
    elif len(tt) - len(yy) == 1 and i in l1:
        l1.remove(i)
uu.append(yy)
uu.append(tt)
ships2["B"] = uu

print("Battle of Ships Game\n")
f.write("Battle of Ships Game\n\n")

z = 0 # these will be number of "X" in the hidden board board1
j = 0 # these will be number of "X" in the hidden board board2
bumC = [] # these will include coordinates of hitted places for player1
bumB = []
bumD = []
bumS = []
bumP = []

bumC2 = [] # these will include coordinates of hitted places for player2
bumB2 = []
bumD2 = []
bumS2 = []
bumP2 = []

old1 = ["-"]
old2 = ["-", "-"]
old3 = ["-"]
old4 = ["-"]
old5 = ["-", "-", "-", "-"]
round = 1
while z != 27 and j != 27:

    def print_grids():       ### print grids grids side by side
        for i in range(1,11):
            row1 = " ".join(str(x) for x in player1_hidden_board[i])
            row2 = " ".join(str(x) for x in player2_hidden_board[i])
            if i < 10:
                print("{}{}\t\t{}{}".format(str(i) + " ", row1, str(i) + " ", row2))
                f.write("\n{}{}\t\t{}{}".format(str(i) + " ", row1, str(i) + " ", row2))
            else:
                print("{}{}\t\t{}{}".format(str(i) + "", row1, str(i) + "", row2))
                f.write("\n{}{}\t\t{}{}".format(str(i) + "", row1, str(i) + "", row2))
    
    def print_ships1(k):    # this function prints the number of sailing or sinking ships 
        x2 = int(x1)        # look at the coordinates bombed if there is a ship unit add to the list, if a ship is on this list then sink the ship
        if k == "C":
            list = c            
            if (x2,y2) in ships1[k]:
                if (x2,y2) not in bumC:
                        bumC.append((x2,y2))
                        bumC.sort()
                else:
                    pass
            if bumC == ships1[k]:
                list = ["X"]
        elif k == "P":
            list = p
            for i in ships1[k]:
                if (x2,y2) in i:
                    if (x2,y2) not in bumP:
                        bumP.append((x2,y2))
                        bumP.sort()
                    else:
                        pass
                    if i[0] in bumP and i[1] in bumP:
                        if list[0] != "X":
                            list[0] = "X"
                        elif list[1] != "X":
                            list[1] = "X"
                        elif list[2] != "X":
                            list[2] = "X"
                        elif list[3] != "X":
                            list[3] = "X"     
        elif k == "D":
            list = d            
            if (x2,y2) in ships1[k]:
                if (x2,y2) not in bumD:
                        bumD.append((x2,y2))
                        bumD.sort()
                else:
                    pass
            if bumD == ships1[k]:
                list = ["X"]   
        elif k == "S":
            list = s            
            if (x2,y2) in ships1[k]:
                if (x2,y2) not in bumS:
                        bumS.append((x2,y2))
                        bumS.sort()
                else:
                    pass
            if bumS == ships1[k]:
                list = ["X"]
        elif k == "B":
            list = b
            for i in ships1[k]:
                if (x2,y2) in i:
                    if (x2,y2) not in bumB:
                        bumB.append((x2,y2))
                        bumB.sort()
                    else:
                        pass
                    if i[0] in bumB and i[1] in bumB and i[2] in bumB and i[3] in bumB:
                        if list[0] != "X":
                            list[0] = "X"
                        elif list[1] != "X":
                            list[1] = "X"     
        for i in list:
            print(i,end=" ")
        f.write(" ".join(list))

        return list

    def print_ships2(h):
        x3 = int(x)
        if h == "C":
            list2 = c2            
            if (x3,y0) in ships2[h]:
                if (x3,y0) not in bumC2:
                    bumC2.append((x3,y0))
                    bumC2.sort()
                else:
                    pass
            if bumC2 == ships2[h]:
                list2 = ["X"]
        elif h == "P":
            list2 = p3
            for i in ships2["P"]:
                if (x3,y0) in i:
                    if (x3,y0) not in bumP2:
                        bumP2.append((x3,y0))
                        bumP2.sort()
                    else:
                        pass
                    if i[0] in  bumP2 and i[1] in  bumP2:
                        if list2[0] != "X":
                            list2[0] = "X"
                        elif list2[1] != "X":
                            list2[1] = "X"
                        elif list2[2] != "X":
                            list2[2] = "X"
                        elif list2[3] != "X":
                            list2[3] = "X"     
        elif h == "D":
            list2 = d2            
            if (x3,y0) in ships2[h]:
                if (x3,y0) not in bumD2:
                    bumD2.append((x3,y0))
                    bumD2.sort()
                else:
                    pass
            if bumD2 == ships2[h]:
                list2 = ["X"]   
        elif h == "S":
            list2 = s2            
            if (x3,y0) in ships2[h]:
                if (x3,y0) not in bumS2:
                    bumS2.append((x3,y0))
                    bumS2.sort()
                else:
                    pass
            if bumS2 == ships2[h]:
                list2 = ["X"]
        elif h == "B":
            list2 = b2
            for i in ships2[h]:
                if (x3,y0) in i:
                    if (x3,y0) not in bumB2:
                        bumB2.append((x3,y0))
                        bumB2.sort()
                    else:
                        pass
                    if i[0] in bumB2 and i[1] in bumB2 and i[2] in bumB2 and i[3] in bumB2:
                        if list2[0] != "X":
                            list2[0] = "X"
                        elif list2[1] != "X":
                            list2[1] = "X"
        for i in list2:
            print(i,end=" ")
        f.write(" ".join(list2))
        return list2

    r = "Round : " + str(round)
    r1 = "Grid Size: 10x10\n"
    letters = "  A B C D E F G H I J"
    p1 = "Player1's Hidden Board"
    p2 = "Player2's Hidden Board"

    print("Player1's Move\n")
    print("{}\t\t\t{}".format(r,r1))
    print("{}\t\t{}".format(p1,p2))
    print("{}\t\t{}".format(letters, letters))

    f.write("Player1's Move\n") 
    f.write("\n{}\t\t\t\t\t{}".format(r,r1))  
    f.write("\n{}\t\t{}\n".format(p1,p2))  
    f.write("{}\t\t{}".format(letters, letters))
    print_grids()

    if round == 1:     # there is no possibility of sinking ship in first round so we can just print just "-"
        f.write("\n\nCarrier\t\t-\t\t\t\tCarrier\t\t-")
        f.write("\nBattleship\t- -\t\t\t\tBattleship\t- -")
        f.write("\nDestroyer\t-\t\t\t\tDestroyer\t-")
        f.write("\nSubmarine\t-\t\t\t\tSubmarine\t-")
        f.write("\nPatrol Boat\t- - - -\t\t\tPatrol Boat\t- - - -")
        print("\nCarrier"+" "*7+"-"+"\t\t\tCarrier"+" "*7+"-")
        print("Battleship"+" "*4+"- -"+"\t\tBattleship"+" "*4+"- -")
        print("Destroyer"+" "*5+"-"+"\t\t\tDestroyer"+" "*5+"-")
        print("Submarine"+" "*5+"-"+"\t\t\tSubmarine"+" "*5+"-")
        print("Patrol Boat"+" "*3+"- - - -"+"\t\tPatrol Boat"+" "*3+ "- - - -")

    else:
        print("\nCarrier"+" "*7, end="")
        f.write("\n\nCarrier\t\t")
        eski1 = print_ships1("C")
        print("\t\tCarrier"+" "*7, end="")
        for i in old1:
            print(i, end=" ")

        f.write("\t\t\t\tCarrier\t\t")
        f.write(" ".join(old1))

        print("\nBattleship"+" "*4, end="")
        f.write("\nBattleship\t")
        eski2 = print_ships1("B")
        print("\t\tBattleship"+" "*4, end="")
        for i in old2:
            print(i, end=" ")

        f.write("\t\t\t\tBattleship\t")
        f.write(" ".join(old2))
        
        print("\nDestroyer"+" "*5, end="")
        f.write("\nDestroyer\t")
        eski3 = print_ships1("D")
        print("\t\tDestroyer"+" "*5, end="")
        for i in old3:
            print(i, end=" ")

        f.write("\t\t\t\tDestroyer\t")
        f.write(" ".join(old3))

        print("\nSubmarine"+" "*5, end="")
        f.write("\nSubmarine\t")
        eski4 = print_ships1("S")
        print("\t\tSubmarine"+" "*5, end="")
        for i in old4:
            print(i, end=" ")

        f.write("\t\t\t\tSubmarine\t")
        f.write(" ".join(old4))

        print("\nPatrol Boat"+" "*3, end="")
        f.write("\nPatrol Boat\t")
        eski5 = print_ships1("P")
        print("\t\tPatrol Boat"+" "*3, end="")
        for i in old5:
            print(i, end=" ")

        f.write("\t\t\tPatrol Boat\t")
        f.write(" ".join(old5))
        
    try:
        a = bomb1[round -1].index(",") 
        x = bomb1[round -1][:a]    #number coordinate
        y = bomb1[round -1][a+1:]  #letter coordinate
    except:        #it is just for the last element in bomb1, normally elements are like "5,H" but last element is "" because of the split(";")
        pass
###### exception handling
    while True:
        try:
            if len(bomb1[round -1]) < 3:
                raise IndexError
            elif not (1 <= int(x) <= 10) or (y not in ["A","B","C","D","E","F","G","H","I","J"]) and y in ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                raise AssertionError
            elif type(int(x)) != int or y not in ["A","B","C","D","E","F","G","H","I","J"]:
                raise ValueError
            else:
                break
        except IndexError:
            try:
                wrong_move = bomb1[round -1]
                del bomb1[round -1]
                print("\nIndexError:", wrong_move, "is incorrect move")
                f.write("\n\nIndexError: ")
                f.write(wrong_move)
                f.write(" is incorrect move")
                a = bomb1[round -1].index(",") 
                x = bomb1[round -1][:a]    #number coordinate
                y = bomb1[round -1][a+1:]  #letter coordinate
            except:         # if this statement works that means player has less move than expected
                print("\nkaBOOM: run for your life!")
                f.write("\nkaBOOM: run for your life!")
                exit()
        except AssertionError:
            wrong_move = bomb1[round -1]
            del bomb1[round -1]
            print("\nAssertionError: Invalid Operation.", wrong_move)
            f.write("\n\nAssertionError: Invalid Operation.")
            f.write(wrong_move)
            a = bomb1[round -1].index(",") 
            x = bomb1[round -1][:a]    #number coordinate
            y = bomb1[round -1][a+1:]  #letter coordinate
        except ValueError:
            wrong_move = bomb1[round -1]
            del bomb1[round -1]
            print("\nValueError:", wrong_move, "is incorrect move")
            f.write("\n\nValueError: ")
            f.write(wrong_move)
            f.write(" is incorrect move")
            a = bomb1[round -1].index(",") 
            x = bomb1[round -1][:a]    #number coordinate
            y = bomb1[round -1][a+1:]  #letter coordinate
        except:
            print("\nkaBOOM: run for your life!")
            f.write("\nkaBOOM: run for your life!")
            exit()

    letter_to_int1 = { "A": 0, "B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6,"H": 7,"I": 8,"J": 9} # see the letter coordinates as number
    try:
        y0 = letter_to_int1[y]    
    except:
        pass   
    
    f.write("\n\nEnter your move: " + x +"," + y + "\n\n")
    f.write("Player2's Move\n")   
    f.write("\n{}\t\t\t\t\t{}".format(r, r1))
    try:
        e = bomb2[round -1].index(",")
        x1 = bomb2[round -1][:e]
        y1 = bomb2[round -1][e+1:]
    except:
        pass        

    letter_to_int2 = { "A": 0, "B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G": 6,"H": 7,"I": 8,"J": 9}
    try:
        y2 = letter_to_int2[y1]
    except:
        pass
    
    def attack_to_player1():
        if dict_real["player1's_board"][int(x1)][y2] == "":
            player1_hidden_board[int(x1)][y2] = "O"
        else:
            player1_hidden_board[int(x1)][y2] = "X"
        
    def attack_to_player2():
        if dict_real["player2's_board"][int(x)][y0] == "":
            player2_hidden_board[int(x)][y0] = "O"
        else:
            player2_hidden_board[int(x)][y0] = "X"

    attack_to_player2()     

    print("\n\nEnter your move: " + x +"," + y + "\n")
    print("Player2's Move\n")   
    print("{}\t\t\t{}".format(r, r1))
    print("{}\t\t{}".format(p1,p2))
    print("{}\t\t{}".format(letters, letters))
    
    f.write("\n{}\t\t{}\n".format(p1,p2))
    f.write("{}\t\t{}".format(letters, letters))
    
    print_grids()

    if round == 1:  # there is no possibility of sinking ship in first round so we can just print just "-"
        f.write("\n\nCarrier\t\t-\t\t\t\tCarrier\t\t-")
        f.write("\nBattleship\t- -\t\t\t\tBattleship\t- -")
        f.write("\nDestroyer\t-\t\t\t\tDestroyer\t-")
        f.write("\nSubmarine\t-\t\t\t\tSubmarine\t -")
        f.write("\nPatrol Boat\t- - - -\t\t\tPatrol Boat\t- - - -")
        print("\nCarrier"+" "*7+"-"+"\t\t\tCarrier"+" "*7+"-")
        print("Battleship"+" "*4+"- -"+"\t\tBattleship"+" "*4+"- -")
        print("Destroyer"+" "*5+"-"+"\t\t\tDestroyer"+" "*5+"-")
        print("Submarine"+" "*5+"-"+"\t\t\tSubmarine"+" "*5+"-")
        print("Patrol Boat"+" "*3+"- - - -"+"\t\tPatrol Boat"+" "*3+ "- - - -")
        def print_shps2(h):   # we should bomb the coordinates if player guess right
            t = []
            x3 = int(x)
            for i in ships2[h]:
                    if (x3,y0) in i:
                        if (x3,y0) not in t:
                            t.append((x3,y0))
            return t
        bumC2 = print_shps2("C")
        bumS2 = print_shps2("S")
        bumB2 = print_shps2("B")
        bumD2 = print_shps2("D")
        bumP2 = print_shps2("P")
    else:
        print("\nCarrier"+" "*7, end="")
        for i in eski1:
            print(i,end=" ")
        f.write("\n\nCarrier\t\t")
        f.write(" ".join(eski1))
        print("\t\tCarrier"+" "*7, end="")
        f.write("\t\t\t\tCarrier\t\t")
        old1 = print_ships2("C")

        print("\nBattleship"+" "*4, end="")
        for i in eski2:
            print(i,end=" ")
        f.write("\nBattleship\t")
        f.write(" ".join(eski2))
        print("\t\tBattleship"+" "*4, end="")
        f.write("\t\t\t\tBattleship\t")
        old2 = print_ships2("B")

        print("\nDestroyer"+" "*5, end="")
        for i in eski3:
            print(i,end=" ")
        f.write("\nDestroyer\t")
        f.write(" ".join(eski3))
        print("\t\tDestroyer"+" "*5, end="")
        f.write("\t\t\t\tDestroyer\t")
        old3 = print_ships2("D")

        print("\nSubmarine"+" "*5, end="")
        for i in eski4:
            print(i,end=" ")
        f.write("\nSubmarine\t")
        f.write(" ".join(eski4))
        print("\t\tSubmarine"+" "*5, end="")
        f.write("\t\t\t\tSubmarine\t")
        old4 = print_ships2("S")

        print("\nPatrol Boat"+" "*3, end="")
        for i in eski5:
            print(i,end=" ")
        f.write("\nPatrol Boat\t")  
        f.write(" ".join(eski5))
        print("\t\tPatrol Boat"+" "*3, end="")
        f.write("\t\t\tPatrol Boat\t")
        old5 = print_ships2("P")

    while True:
        try:
            if len(bomb2[round -1]) < 3:
                raise IndexError
            elif not (1 <= int(x1) <= 10) or (y1 not in ["A","B","C","D","E","F","G","H","I","J"]) and y1 in ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                raise AssertionError
            elif not x1.isdigit() or y1 not in ["A","B","C","D","E","F","G","H","I","J",'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                raise ValueError
            else:
                break
        except IndexError:
            try:
                wrong_move = bomb2[round -1]
                del bomb2[round -1]
                e = bomb2[round -1].index(",") 
                x1 = bomb2[round -1][:e]    #number coordinate
                y1 = bomb2[round -1][e+1:]  #letter coordinate
                print("\nIndexError:", wrong_move, "is incorrect move")
                f.write("\nIndexError: ")
                f.write(wrong_move)
                f.write(" is incorrect move\n")
                
            except:
                print("\nkaBOOM: run for your life!")
                f.write("\nkaBOOM: run for your life!")
                exit()
        except AssertionError:
            wrong_move = bomb2[round -1]
            del bomb2[round -1]
            print("\nAssertionError: Invalid Operation.", wrong_move)
            f.write("\nAssertionError: Invalid Operation.")
            f.write(wrong_move)
            f.write("\n")
            e = bomb2[round -1].index(",") 
            x1 = bomb2[round -1][:e]    #number coordinate
            y1 = bomb2[round -1][e+1:]  #letter coordinate
        except ValueError:
            wrong_move = bomb2[round -1]
            del bomb2[round -1]
            print("\nValueError:", wrong_move, "is incorrect move" )
            f.write("\nValueError:")
            f.write(wrong_move)
            f.write(" is incorrect move\n")
            e = bomb2[round -1].index(",") 
            x1 = bomb2[round -1][:e]    #number coordinate
            y1 = bomb2[round -1][e+1:]  #letter coordinate
        except:
            print("\nkaBOOM: run for your life!")
            f.write("\nkaBOOM: run for your life!")
            exit()

    attack_to_player1()
    
    print("\n\nEnter your move: " + x1 +"," + y1 + "\n")
    f.write("\n\nEnter your move: " + x1 +"," + y1 + "\n\n")
    ### count the number of ship units which are shot down, when it is 27 that means game over
    z = 0
    j = 0
    for i in player1_hidden_board.values():
        z += i.count("X")
    
    for i in player2_hidden_board.values():
        j += i.count("X")

    round += 1
if z == 27 and j == 27:
    print("Player1 Wins!", "Player2 Wins!", "It is a Draw!\n")
    f.write("Player1 Wins! "+ "Player2 Wins! "+ "It is a Draw!\n")
elif z == 27:
    print("Player2 Wins!\n")
    f.write("Player2 Wins!\n")
elif j == 27:
    print("Player1 Wins!\n")
    f.write("Player1 Wins!\n")

print("Final Information\n")
f.write("\nFinal Information\n\n")

if z == 27:    # show player2's unhitched places when player1 wins
    for i in range(1,11):
        for a in range(10):
            if player2_hidden_board[i][a] == "-" and dict_real["player2's_board"][i][a] != "":
                player2_hidden_board[i][a] = dict_real["player2's_board"][i][a]
else:          # # show player1's unhitched places when player2 wins
    for i in range(1,11):
        for a in range(10):
            if player1_hidden_board[i][a] == "-" and dict_real["player1's_board"][i][a] != "":
                player1_hidden_board[i][a] = dict_real["player1's_board"][i][a]

print("{}\t\t\t{}".format("Player1's Board", "Player2's Board"))
print("{}\t\t{}".format(letters, letters))
f.write("{}\t\t{}".format(letters, letters))
print_grids()
# print grids side by side
print("\nCarrier"+" "*7, end="")
f.write("\n\nCarrier\t\t")
print_ships1("C")
print("\t\tCarrier"+" "*7, end="")
f.write("\t\t\t\tCarrier\t\t")
print_ships2("C")

print("\nBattleship"+" "*4, end="")
f.write("\nBattleship\t")
print_ships1("B")
print("\t\tBattleship"+" "*4, end="")
f.write("\t\t\t\tBattleship\t")
print_ships2("B")

print("\nDestroyer"+" "*5, end="")
f.write("\nDestroyer\t")
print_ships1("D")
print("\t\tDestroyer"+" "*5, end="")
f.write("\t\t\t\tDestroyer\t")
print_ships2("D")

print("\nSubmarine"+" "*5, end="")
f.write("\nSubmarine\t")
print_ships1("S")
print("\t\tSubmarine"+" "*5, end="")
f.write("\t\t\t\tSubmarine\t")
print_ships2("S")

print("\nPatrol Boat"+" "*3, end="")
f.write("\nPatrol Boat\t")
print_ships1("P")  
print("\t\tPatrol Boat"+" "*3, end="")
f.write("\t\t\tPatrol Boat\t")
print_ships2("P")

f.close()
# b2210356084 omer faruk guler