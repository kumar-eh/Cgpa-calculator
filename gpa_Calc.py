def grade_points(grades):
    points = []
    for i in grades:
        if((i == "O") or (i == "o")):
            points.append(10)
        if((i == 'A+') or (i == 'a+')):
            points.append(9)
        if((i == 'A') or (i == 'a')):
            points.append(8)
        if((i == 'b+') or (i == 'B+')):
            points.append(7)
        if((i == 'B') or (i == 'b')):
            points.append(6)
        if((i == 'RA') or (i == 'ra')):
            points.append(0)
    return points
a = int(input("Semester to calculate gpa\n"))
if a == 1:
    g = []
    sem1 = {"Communicative English" : 4 , "Engineering Mathematics I" : 4 , "Engineering Physics" : 3 , "Engineering Chemistry" : 3 , "Problem Solving and Python Programming" : 3 , "Engineering Graphics" : 4 , "Problem Solving and Python Programming Laboratory" : 2 , "Physics and Chemistry Laboratory" : 2}
    d = dict.keys(sem1)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem1)
    print((sem1["Communicative English"]*points[0] + sem1["Engineering Mathematics I"] * points[1] + sem1["Engineering Physics"] * points[2] + sem1["Engineering Chemistry"]* points[3] + sem1["Problem Solving and Python Programming"]* points[4] + sem1["Engineering Graphics"] * points[5] + sem1["Problem Solving and Python Programming Laboratory"]* points[6] + sem1["Physics and Chemistry Laboratory"]* points[7])/25)
if a == 2:
    g = []
    sem2 = {"Technical English" : 4 , "Engineering Mathematics II" : 4 , "Physics for Information Science" : 3 , "BEEE" : 3 , "IT essentials" : 3 , "C programming" : 3 , "Engineering practices lab" : 2 , "C Laboratory" : 2 , "IT Lab" : 1}
    d = dict.keys(sem2)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem2)
    print(points)
    print((sem2["Technical English"]*points[0] + sem2["Engineering Mathematics II"] * points[1] + sem2["Physics for Information Science"] * points[2] + sem2["BEEE"]* points[3] + sem2["IT essentials"]* points[4] + sem2["C programming"] * points[5] + sem2["Engineering practices lab"]* points[6] + sem2["C Laboratory"]* points[7] + sem2["IT Lab"] * points[8])/25)
if a == 3:
    g = []
    sem3 = {"Discrete Mathematics" : 4 , "DPSD" : 4 , "Data Structures" : 3 , "OOPS" : 3 , "ADC" : 3 , "DS lab" : 2 , "OOPS lab" : 2 , "Digital Systems Lab" : 2 , "Eng lab" : 1}
    d = dict.keys(sem3)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem3)
    print(points)
    print((sem3["Discrete Mathematics"]*points[0] + sem3["DPSD"] * points[1] + sem3["Data Structures"] * points[2] + sem3["OOPS"]* points[3] + sem3["ADC"]* points[4] + sem3["DS lab"] * points[5] + sem3["OOPS lab"]* points[6] + sem3["Digital Systems Lab"] * points[7] + sem3["Eng lab"] * points[8])/24)
if a == 4:
    g = []
    sem4 = {"P & S" : 4 , "CA" : 3 , "DBMS" : 3 , "DSA" : 3 , "OS" : 3 , "EVS" : 3 , "DBMS lab" : 2 , "OS Lab" : 2 , "Eng lab" : 1}
    d = dict.keys(sem4)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem4)
    print(points)
    print((sem4["P & S"]*points[0] + sem4["CA"] * points[1] + sem4["DBMS"] * points[2] + sem4["DSA"]* points[3] + sem4["OS"]* points[4] + sem4["EVS"] * points[5] + sem4["DBMS lab"]* points[6] + sem4["OS Lab"] * points[7] + sem4["Eng lab"] * points[8])/24)
if a == 5:
    g = []
    sem5 = {"ANT" : 4 , "CN" : 3 , "MPMC" : 3 , "Web tech" : 3 , "Software engg" : 3 , "OE1" : 3 , "MPMC lab" : 2 , "Networks Lab" : 2 , "Web tech lab" : 2}
    d = dict.keys(sem5)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem5)
    print(points)
    print((sem5["ANT"]*points[0] + sem5["CN"] * points[1] + sem5["MPMC"] * points[2] + sem5["Web tech"]* points[3] + sem5["Software engg"]* points[4] + sem5["OE1"] * points[5] + sem5["MPMC lab"]* points[6] + sem5["Networks Lab"] * points[7] + sem5["Web tech lab"] * points[8])/25)
if a == 6:
    g = []
    sem6 = {"CI" : 3 , "OOAD" : 3 , "Mobile comm" : 3 , "Big data" : 3 , "computer graphics" : 3 , "PE1" : 3 , "Mobile lab" : 2 , "OOAD Lab" : 2 , "Mini project" : 1 , "eng lab" : 1}
    d = dict.keys(sem6)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem6)
    print(points)
    print((sem6["CI"]*points[0] + sem6["OOAD"] * points[1] + sem6["Mobile comm"] * points[2] + sem6["Big data"]* points[3] + sem6["computer graphics"]* points[4] + sem6["PE1"] * points[5] + sem6["Mobile lab"]* points[6] + sem6["OOAD Lab"] * points[7] + sem6["Mini project"] * points[8] + sem6["eng lab"] * points[9])/24)
if a == 7:
    g = []
    sem7 = {"Principles of management" : 3 , "Cryptography" : 3 , "Cloud computing" : 3 , "OE2" : 3 , "PE2" : 3 , "PE3" : 3 , "FOSS" : 2 , "Security" : 2}
    d = dict.keys(sem7)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem7)
    print((sem7["Principles of management"]*points[0] + sem7["Cryptography"] * points[1] + sem7["Cloud computing"] * points[2] + sem7["OE2"]* points[3] + sem7["PE2"]* points[4] + sem7["PE3"] * points[5] + sem7["FOSS"]* points[6] + sem7["Security"]* points[7])/22)
if a == 8:
    g = []
    sem8 = {"PE4" : 3 , "PE5" : 3 , "Project" : 10}
    d = dict.keys(sem8)
    for i in d:
        g1 = input("Enter grade of "+ i + "\n")
        g.append(g1)
    points = grade_points(g)
    p = dict.values(sem8)
    print((sem8["PE4"]*points[0] + sem8["PE5"] * points[1] + sem8["Project"] * points[2])/16)




