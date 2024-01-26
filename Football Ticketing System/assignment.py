import sys
reading_file_name = sys.argv[1]   
writing_file_name = 'output.txt'     
with open(reading_file_name) as f:    #read the text file as data
	data = f.readlines()
    
with open(writing_file_name, "w") as f:    #print to the file named output.txt

    k = []
    alphabe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic = {}

    def create_category():
        a = []      #it is for the last row in matrix, this row will include just numbers
        matrix = []      #to gather all rows in a list
        categ_name = lines.split()[1]
        row = lines.split()[2][:2]
        column = lines.split()[2][3:]       
        for c in range(int(row)):
            matrix.append(alphabe[c] + "  X"*int(column))    
        matrix.reverse()
        a.append("   ")     #to begin with spaces to last row
        for b in range(int(column)):  #this statement created for append spaces to between numbers
            if len(str(b)) == 1:
                a.append(str(b) + "  ")
            else:
                a.append(str(b) + " ")
        string = ''.join([str(item) for item in a if 'X' not in item])   #to be added to the matrix, this row(incuding numbers) evaluated to a string
        matrix.append(string)
        if categ_name not in dic.keys():       
            dic[categ_name] = matrix      #key is category name and its' value is matrix
            f.write("The category " +categ_name+ " having " +str(int(row)*int(column)) + " seats has been created\n")
            print("The category " +categ_name+ " having " +str(int(row)*int(column)) + " seats has been created\n" ,end="")
        else:
            f.write("Warning: Cannot create the category for the second time. The stadium has already " + categ_name+ "\n")
            print("Warning: Cannot create the category for the second time. The stadium has already " + categ_name+ "\n" ,end="")       

    def sell_ticket():
        k = lines.split()[2]   #student or full or season
        categ_name = lines.split()[3]
        loc = lines.split()[4:]   #seat numbers
        if lines.split()[2] == "season":    #to write "T" instead of "X" when "season" is entered
            k = "ticket"  
        s = []        
        loca = lines.split()[3][9:]   #category name's number
        for a in dic[categ_name]:
            a = list(a)   #to be able to evaluate a's elements
            for i in loc:
                if "-" not in i:    #select just one seat
                    if i[0] == a[0]:  #to select a's row which starts with locations of tickets row
                        if (int(i[1:])*3+3) <= len(a):    #the calculation is for locations of tickets in row
                            if a[int(i[1:])*3+3] == "X":
                                a[int(i[1:])*3+3] = k[0].title()
                                f.write("Success: " + lines.split()[1] + " has bought " + i + " at " + categ_name + "\n")
                                print("Success: " + lines.split()[1] + " has bought " + i + " at " + categ_name + "\n" ,end="")
                            else:
                                f.write("Warning: The seat "+ i +" cannot be sold to " +lines.split()[1]+ " since it was already sold!\n")
                                print("Warning: The seat "+ i +" cannot be sold to " +lines.split()[1]+ " since it was already sold!\n" ,end="")
                        else:
                            f.write("Error: The category " +categ_name+ " has less column than the specified index " + i + "!\n")
                            print("Error: The category " +categ_name+ " has less column than the specified index " + i + "!\n" ,end="")
                else:   #like c2-10
                    if i[0] == a[0]:
                        d = i.index("-")  #to select locations of tickets before and after "-"
                        z = i[1:d]
                        g = i[d+1:]
                        if int(g)*3+3 <= len(a):  #check if column number is enough for category or not
                            for b in a[int(z)*3+3:int(g)*3+3:3]:
                                if b != "X":  #check if seat is sold or not
                                    f.write("Warning: The seats " + i + " cannot be sold to " + lines.split()[1] + " due some of them have already been sold!\n")
                                    print("Warning: The seats " + i + " cannot be sold to " + lines.split()[1] + " due some of them have already been sold!\n" ,end="")
                                    break
                                else:
                                    a[int(z)*3+3:int(g)*3+4:3] = k[0].title()*(int(g)-int(z)+1)
                                    f.write("Success: " +lines.split()[1]+ " has bought " + i + " at " + categ_name + "\n")
                                    print("Success: " +lines.split()[1]+ " has bought " + i + " at " + categ_name + "\n" ,end="")
                                    break
                        else:
                            f.write("Error: The category " + categ_name + " has less column than the specified index " + i + " !\n")
                            print("Error: The category " + categ_name + " has less column than the specified index " + i + " !\n" ,end="")
            a = ''.join(a)           #these for change the value of category names 
            s.append(a)
        dic[categ_name] = s

    def cancel_ticket():
        c = []
        d = []
        loc = lines.split()[2:]   #seat numbers
        categ_name = lines.split()[1]       
        for a in dic[categ_name]:
            a = list(a)
            for i in loc:
                c.append(a[0])    #use this list for errors
                if len(c) == (len(dic[categ_name])-1):
                    for a in dic[categ_name]:
                        a = list(a)
                        if i[0] not in c and (int(i[1:])*3+3) > len(a):
                            f.write("Error: The category '" + categ_name + "' has less row and column than the specified index " + i + "!\n")  
                            print("Error: The category '" + categ_name + "' has less row and column than the specified index " + i + "!\n" ,end="")                      
                        else:                       
                            if i[0] not in c:
                                f.write("Error: The category '" + categ_name + "' has less row than the specified index " + i + "!\n")
                                print("Error: The category '" + categ_name + "' has less row than the specified index " + i + "!\n" ,end="")
                                
                            else:                               
                                if i[0] == a[0]:
                                    if (int(i[1:])*3+3) <= len(a):
                                        if a[(int(i[1:])*3+3)] != "X":
                                            a[(int(i[1:])*3+3)] = "X"                                       
                                            f.write("Success: The seat " + i + " at " + categ_name + " has been canceled and now ready to sell again\n")
                                            print("Success: The seat " + i + " at " + categ_name + " has been canceled and now ready to sell again\n" ,end="")
                                        else:
                                            f.write("Error: The seat " + i + " at " + categ_name + " has already been free! Nothing to cancel\n")
                                            print("Error: The seat " + i + " at " + categ_name + " has already been free! Nothing to cancel\n" ,end="")
                                    else:
                                        f.write("Error: The category " + categ_name + " has less column than the specified index " + i + "!\n")
                                        print("Error: The category " + categ_name + " has less column than the specified index " + i + "!\n" ,end="")
                        a = ''.join(a)
                        d.append(a)
                    dic[categ_name] = d

    def balance():
        categ_name = lines.split()[1]
        b = 0
        c = 0
        d = 0
        for i in dic[categ_name]: #to find the number of student, full and season tickets in the category
            a = i[1:].count("S")
            b += a
            e = i[1:].count("F")
            c += e
            y = i[1:].count("T")
            d += y
        f.write("Category report of '" + categ_name + "'\n")
        f.write("---------------------------------\n")
        f.write("Sum of students = " + str(b) + ", Sum of full pay = " + str(c) + ", Sum of season ticket= " + str(d) + ", and Revenues = " + str(10*b+20*c+250*d) + " Dollars\n")
        print("Category report of '" + categ_name + "'\n" ,end="")
        print("---------------------------------\n" ,end="")
        print("Sum of students = " + str(b) + ", Sum of full pay = " + str(c) + ", Sum of season ticket= " + str(d) + ", and Revenues = " + str(10*b+20*c+250*d) + " Dollars\n" ,end="")

    def show_category():
        categ_name = lines.split()[1]
        f.write("Printing category layout of " + categ_name + "\n")
        f.write("\n")
        print("Printing category layout of " + categ_name + "\n")
        for a in dic[categ_name]:   #matrix is already ready to be printed line by line
            f.write(a + "\n")
            print(a + "\n" ,end="")

    for lines in data:     #call functions in the order they should be 
        if "CREATECATEGORY" in lines:
            create_category()         
        elif "SELLTICKET" in lines:
            sell_ticket()           
        elif "CANCELTICKET" in lines:
            cancel_ticket()   
        elif "BALANCE" in lines:
            balance()
        elif "SHOWCATEGORY" in lines:          
            show_category()