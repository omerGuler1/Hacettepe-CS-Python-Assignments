input_file = "doctors_aid_inputs.txt"
f = open("doctors_aid_outputs.txt", "w")

with open(input_file) as f1:
    data = f1.readlines()

for index, element in enumerate(data):
    split_element = element.split(", ")
    last_word = split_element[-1]
    cleaned_word = last_word.rstrip("\n")
    split_element[-1] = last_word.replace(last_word, cleaned_word)
    data[index] = ", ".join(split_element)

patients = []

def create(line, patients):
    line = line.split(", ")
    line[0] = line[0][7:]

    if line[0] not in patients:
        patients.append(line)
        f.write("Patient " + line[0] + " is recorded.\n")
    else:
        f.write("Patient " + line[0] + " cannot be recorded due to duplication.\n")

def remove(line, patients):
        line = line.split(" ")
        a = 0
        for i in patients:
            if i[0] == line[1]:
                patients.remove(i)
                f.write("Patient " + line[1] + " is removed.\n")
                a = 1

        if a == 0:
            f.write("Patient " + line[1] + " cannot be removed due to absence.\n")

def list(patients):
        f.write("{:8}{:12}{:16}{:12}{:16}{}{:8}{:12}{:16}{:12}{:16}{}".format('Patient','Diagnosis','Disease','Disease','Treatment','Treatment\n','Name','Accuracy','Name','Incidence','Name','Risk\n'))
        f.write("-"*73 + "\n")
        for patient in patients:
            formatted = f"{patient[0]:8}{float(patient[1])*100:<5.2f}%      {patient[2]:16}{patient[3]:12}{patient[4]:16}{str(int(float(patient[5])*100))}%\n"
            f.write(formatted)

def probability(line, patients):
    index = -1 
    for i in range(len(patients)):
        if patients[i][0] == line.split()[1]: 
            index = i
    
    if index != -1:
        patient = patients[index]
        incidence_list = patient[3].split('/')
        zz = int(incidence_list[0]) / int(incidence_list[1])
        probability = float(100*(zz / (zz + 1 - float(patient[1]))))
        probability = float(str(probability)[:5])
        if int(probability) == float(probability):
            probability = int(probability)

        f.write("Patient " + patient[0] + " has a probability of " + str(probability) + "%" + " of having " + 
                patient[2].replace('Cancer',' Cancer'+"\n"))
    else:
        f.write("Probability for " +line.split()[1]+ " cannot be calculated due to absence.\n")

def recommendation(line, patients):
        index = -1 
        for i in range(len(patients)):
            if patients[i][0] == line.split()[1]:
                index = i
                
        if index != -1 :
            patient = patients[index]
            incidence = patient[3].split('/')
            incidence_list = int(incidence[0]) / int(incidence[1])
            probability = int(100*(incidence_list / (incidence_list + 1 - float(patient[1]))))
            value = int(100 * float(patient[-1]))
            if value < probability:
                f.write("System suggests "+ patient[0]+" to have the treatment.\n")
            else:
                f.write("System suggests "+patient[0]+" NOT to have the treatment.\n")
                
        else:
            f.write("Recommendation for "+ line.split()[1] +" cannot be calculated due to absence.\n")


for line in data:
    if line.startswith("create"):
        create(line, patients)
    elif line.startswith("remove"):
        remove(line, patients)
    elif line.startswith("list"):
        list(patients)
    elif line.startswith("probability"):
        probability(line, patients)
    elif line.startswith("recommendation"):
        recommendation(line, patients)
