from tkinter import *
from tkinter.messagebox import *

def gpacalculator(grades):
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
        if((i == 'Other') or (i == 'ra')):
            points.append(0)
    return points
def calgpa():
    def gpa(gpa_page):
        a1 = clicked1.get()

        if a1 == "Sem 1":
            
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                points = gpacalculator(grades)
                gpa = 4*points[0] + 4 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 4 * points[5] + 2* points[6] + 2* points[7]
                gpa = gpa/25
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O" )

            sub1 = Label(gpa_page , text = "English HS8151")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "Maths MA8151")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "Physics PY8151")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "Chemistry CY8151")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "Python GE8151")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "EG GE8152")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "Python lab GE8161")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "Phy Chem lab BS8161")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
            
        if a1 == "Sem 2": 
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                s9 = clickedsub9.get()
                grades.append(s9)
                points = gpacalculator(grades)
                gpa = 4*points[0] + 4 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 3 * points[5] + 2* points[6] + 2* points[7]+ 1* points[8]
                gpa = gpa/25
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")
            clickedsub9 = StringVar()
            clickedsub9.set("O")
            
            sub1 = Label(gpa_page , text = "English HS8251")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "Maths MA8251")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "Physics PH8252")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "BEEE BE8252")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "IT Essentials IT8201")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "C CS8251")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "Engg practices GE8261")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "C lab CS8261")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            sub9 = Label(gpa_page , text = "IT lab IT8211")
            sub9.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s9 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s9.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
        if a1 == "Sem 3":
            
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                s9 = clickedsub9.get()
                grades.append(s9)
                points = gpacalculator(grades)
                gpa = 4*points[0] + 4 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 2 * points[5] + 2* points[6] + 2* points[7]+ 1* points[8]
                gpa = gpa/24
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")
            clickedsub9 = StringVar()
            clickedsub9.set("O")
            
            sub1 = Label(gpa_page , text = "Maths MA8351")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "DPSD CS8351")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "DS CS8391")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "OOPS CS8392")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "ADC EC8394")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "DS lab CS8381")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "OOPS lab CS8383")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "DPSD lab CS8382")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            sub9 = Label(gpa_page , text = "Eng lab HS8381")
            sub9.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s9 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s9.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
        if a1 == "Sem 4":
            
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                s9 = clickedsub9.get()
                grades.append(s9)
                points = gpacalculator(grades)
                gpa = 4*points[0] + 3 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 3 * points[5] + 2* points[6] + 2* points[7]+ 1* points[8]
                gpa = gpa/24
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")
            clickedsub9 = StringVar()
            clickedsub9.set("O")
            
            sub1 = Label(gpa_page , text = "Maths MA8391")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "CA CS8491")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "DBMS CS8492")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "DAA CS8451")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "OS CS8493")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "EVS GE8291")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "DBMS lab CS8481")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "OS lab CS8461")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            sub9 = Label(gpa_page , text = "Eng lab HS8461")
            sub9.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s9 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s9.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
        if a1 == "Sem 5":
            
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                s9 = clickedsub9.get()
                grades.append(s9)
                points = gpacalculator(grades)
                gpa = 4*points[0] + 3 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 3 * points[5] + 2* points[6] + 2* points[7]+ 2* points[8]
                gpa = gpa/25
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")
            clickedsub9 = StringVar()
            clickedsub9.set("O")
            
            sub1 = Label(gpa_page , text = "Maths MA8551")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "CN CS8591")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "MCMS EC8691")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "Web tech IT8501")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "Software engg CS8494")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "Open Elective 1 ")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "MCMS lab EC8681")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "Networks lab CS8581")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            sub9 = Label(gpa_page , text = "Web tech lab IT8511")
            sub9.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s9 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s9.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
        if a1 == "Sem 6":
            
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                s9 = clickedsub9.get()
                grades.append(s9)
                s10 = clickedsub10.get()
                grades.append(s10)
                points = gpacalculator(grades)
                gpa = 3*points[0] + 3 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 3 * points[5] + 2* points[6] + 2* points[7]+ 1* points[8] + 1*points[9]
                gpa = gpa/24
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.8 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.8 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")
            clickedsub9 = StringVar()
            clickedsub9.set("O")
            clickedsub10 = StringVar()
            clickedsub10.set("O")
            
            sub1 = Label(gpa_page , text = "Computational Intelligence IT8601")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "OOAD CS8592")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "Mobile Comm IT8602")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "Big Data CS8091")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "Computer graphics CS8092")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "Professional elective")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "Mobile app lab CS8662")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "OOAD lab CS8582")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            sub9 = Label(gpa_page , text = "Mini project")
            sub9.place(relx = 0.2 , rely = 0.65 , relheight = 0.05 , relwidth = 0.3)

            s9 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s9.place(relx = 0.5 , rely = 0.65, relheight = 0.05 , relwidth = 0.3)
            
            sub10 = Label(gpa_page , text = "Professional comm")
            sub10.place(relx = 0.2 , rely = 0.7 , relheight = 0.05 , relwidth = 0.3)

            s10 = OptionMenu(gpa_page , clickedsub9 , "O","A+","A","B+","B", "Other")
            s10.place(relx = 0.5 , rely = 0.7, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)

        if a1 == "Sem 7":
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                s4 = clickedsub4.get()
                grades.append(s4)
                s5 = clickedsub5.get()
                grades.append(s5)
                s6 = clickedsub6.get()
                grades.append(s6)
                s7 = clickedsub7.get()
                grades.append(s7)
                s8 = clickedsub8.get()
                grades.append(s8)
                points = gpacalculator(grades)
                gpa = 3*points[0] + 3 * points[1] + 3 * points[2] + 3* points[3] + 3* points[4] + 3 * points[5] + 2* points[6] + 2* points[7]
                gpa = gpa/22
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            clickedsub4 = StringVar()
            clickedsub4.set("O")
            clickedsub5 = StringVar()
            clickedsub5.set("O")
            clickedsub6 = StringVar()
            clickedsub6.set("O")
            clickedsub7 = StringVar()
            clickedsub7.set("O")
            clickedsub8 = StringVar()
            clickedsub8.set("O")

            sub1 = Label(gpa_page , text = "Principles of Management MG8591")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "Cryptography CS8792")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "Cloud computing CS8791")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)

            sub4 = Label(gpa_page , text = "Open elective ")
            sub4.place(relx = 0.2 , rely = 0.4 , relheight = 0.05 , relwidth = 0.3)

            s4 = OptionMenu(gpa_page , clickedsub4 , "O","A+","A","B+","B", "Other")
            s4.place(relx = 0.5 , rely = 0.4, relheight = 0.05 , relwidth = 0.3)

            sub5 = Label(gpa_page , text = "Professional elective")
            sub5.place(relx = 0.2 , rely = 0.45 , relheight = 0.05 , relwidth = 0.3)

            s5 = OptionMenu(gpa_page , clickedsub5 , "O","A+","A","B+","B", "Other")
            s5.place(relx = 0.5 , rely = 0.45, relheight = 0.05 , relwidth = 0.3)

            sub6 = Label(gpa_page , text = "Professional elective")
            sub6.place(relx = 0.2 , rely = 0.5 , relheight = 0.05 , relwidth = 0.3)

            s6 = OptionMenu(gpa_page , clickedsub6 , "O","A+","A","B+","B", "Other")
            s6.place(relx = 0.5 , rely = 0.5, relheight = 0.05 , relwidth = 0.3)

            sub7 = Label(gpa_page , text = "Foss lab IT8711")
            sub7.place(relx = 0.2 , rely = 0.55 , relheight = 0.05 , relwidth = 0.3)

            s7 = OptionMenu(gpa_page , clickedsub7 , "O","A+","A","B+","B", "Other")
            s7.place(relx = 0.5 , rely = 0.55, relheight = 0.05 , relwidth = 0.3)

            sub8 = Label(gpa_page , text = "Security lab IT8761")
            sub8.place(relx = 0.2 , rely = 0.6 , relheight = 0.05 , relwidth = 0.3)

            s8 = OptionMenu(gpa_page , clickedsub8 , "O","A+","A","B+","B", "Other")
            s8.place(relx = 0.5 , rely = 0.6, relheight = 0.05 , relwidth = 0.3)

            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)
            
        if a1 == "Sem 8":
            def gpa():
                grades = []
                s1 = clickedsub1.get()
                grades.append(s1)
                s2 = clickedsub2.get()
                grades.append(s2)
                s3 = clickedsub3.get()
                grades.append(s3)
                points = gpacalculator(grades)
                gpa = 3*points[0] + 3 * points[1] + 10 * points[2]
                gpa = gpa/16
                final_label = Label(gpa_page , text = "Your GPA")
                final_label.place(relx = 0.17 , rely = 0.75 , relwidth = 0.3 , relheight = 0.05)
                final_gpa = Entry(gpa_page)
                final_gpa.place(relx = 0.53 , rely = 0.75 , relwidth = 0.4 , relheight = 0.05)
                final_gpa.insert(END , gpa)
            clickedsub1 = StringVar()
            clickedsub1.set("O")
            clickedsub2 = StringVar()
            clickedsub2.set("O")
            clickedsub3 = StringVar()
            clickedsub3.set("O")
            sub1 = Label(gpa_page , text = "Professional elective 4")
            sub1.place(relx = 0.2 , rely = 0.25 , relheight = 0.05 , relwidth = 0.3)

            s1 = OptionMenu(gpa_page , clickedsub1 , "O","A+","A","B+","B", "Other")
            s1.place(relx = 0.5 , rely = 0.25, relheight = 0.05 , relwidth = 0.3)

            sub2 = Label(gpa_page , text = "Professional elective 5")
            sub2.place(relx = 0.2 , rely = 0.3 , relheight = 0.05 , relwidth = 0.3)

            s2 = OptionMenu(gpa_page , clickedsub2 , "O","A+","A","B+","B", "Other")
            s2.place(relx = 0.5 , rely = 0.3, relheight = 0.05 , relwidth = 0.3)

            sub3 = Label(gpa_page , text = "Project work IT8811")
            sub3.place(relx = 0.2 , rely = 0.35 , relheight = 0.05 , relwidth = 0.3)

            s3 = OptionMenu(gpa_page , clickedsub3 , "O","A+","A","B+","B", "Other")
            s3.place(relx = 0.5 , rely = 0.35, relheight = 0.05 , relwidth = 0.3)
            
            submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa())
            submit1.place(relx = 0.4 , rely = 0.66 , relheight = 0.05 , relwidth = 0.2)

            
    clicked1 = StringVar()
    clicked1.set("Sem 1")
    
    gpa_page = Frame(mainpage)
    gpa_page.place(relx = 0 , rely = 0.1 , relheight = 0.9 , relwidth = 1)

    select_label1 = Label(gpa_page , text = "Select semester to check gpa")
    select_label1.place(relx = 0.2 , rely = 0.1 , relheight = 0.05 , relwidth = 0.3)

    sem_number1 = OptionMenu(gpa_page , clicked1 , "Sem 1","Sem 2","Sem 3", "Sem 4","Sem 5","Sem 6", "Sem 7" , "Sem 8")
    sem_number1.place(relx = 0.5 , rely = 0.1 , relheight = 0.05 , relwidth = 0.3)

    sem_submit1 = Button(gpa_page , text = "Submit" , command = lambda: gpa(gpa_page))
    sem_submit1.place(relx = 0.4 , rely = 0.16 , relheight = 0.05 , relwidth = 0.2)


def calcgpa():
    def cgpa(cgpa_page):
        a = clicked.get()

        if a == "Sem 1":
            def upto1():
                s1 = sem1.get() 
                final_cgpa.insert(END , s1)
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page)
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA")
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Text(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto1())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)
            
        if a == "Sem 2":
            def upto2():
                s1 = sem1.get()
                s2 = sem2.get()
                cgpa = (float(s1)+float(s2))/2
                final_cgpa.insert(END , cgpa)
                
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page)
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA")
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page)
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA")
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Text(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto2())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)

        if a == "Sem 3":
            def upto3():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                cgpa = (float(s1)+float(s2)+float(s3))/3
                final_cgpa.insert(END , cgpa)
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page )
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA" )
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page )
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page)
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA" )
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page )
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto3())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)

        if a == "Sem 4":
            def upto4():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                s4 = sem4.get()
                cgpa = (float(s1)+float(s2)+float(s3)+float(s4))/4
                final_cgpa.insert(END , cgpa)
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA" )
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page )
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA")
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page)
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page)
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            sem4_label = Label(cgpa_page , text = "Sem 4 GPA")
            sem4_label.place(relx = 0.17 , rely = 0.37 , relwidth = 0.3 , relheight = 0.05)
            sem4 = Entry(cgpa_page)
            sem4.place(relx = 0.53 , rely = 0.37 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA" )
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto4())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)            

        if a == "Sem 5":
            def upto5():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                s4 = sem4.get()
                s5 = sem5.get()
                cgpa = (float(s1)+float(s2)+float(s3)+float(s4)+float(s5))/5
                final_cgpa.insert(END , cgpa)
                
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page)
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA")
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page)
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page)
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            sem4_label = Label(cgpa_page , text = "Sem 4 GPA")
            sem4_label.place(relx = 0.17 , rely = 0.37 , relwidth = 0.3 , relheight = 0.05)
            sem4 = Entry(cgpa_page )
            sem4.place(relx = 0.53 , rely = 0.37 , relwidth = 0.4 , relheight = 0.05)

            sem5_label = Label(cgpa_page , text = "Sem 5 GPA" )
            sem5_label.place(relx = 0.17 , rely = 0.44 , relwidth = 0.3 , relheight = 0.05)
            sem5 = Entry(cgpa_page)
            sem5.place(relx = 0.53 , rely = 0.44 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA")
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto5())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)
            
        if a == "Sem 6":
            def upto6():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                s4 = sem4.get()
                s5 = sem5.get()
                s6 = sem6.get()
                cgpa = (float(s1)+float(s2)+float(s3)+float(s4)+float(s5)+float(s6))/6
                final_cgpa.insert(END , cgpa)
                
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page )
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA")
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page)
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page )
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            sem4_label = Label(cgpa_page , text = "Sem 4 GPA")
            sem4_label.place(relx = 0.17 , rely = 0.37 , relwidth = 0.3 , relheight = 0.05)
            sem4 = Entry(cgpa_page)
            sem4.place(relx = 0.53 , rely = 0.37 , relwidth = 0.4 , relheight = 0.05)

            sem5_label = Label(cgpa_page , text = "Sem 5 GPA")
            sem5_label.place(relx = 0.17 , rely = 0.44 , relwidth = 0.3 , relheight = 0.05)
            sem5 = Entry(cgpa_page)
            sem5.place(relx = 0.53 , rely = 0.44 , relwidth = 0.4 , relheight = 0.05)

            sem6_label = Label(cgpa_page , text = "Sem 6 GPA")
            sem6_label.place(relx = 0.17 , rely = 0.5 , relwidth = 0.3 , relheight = 0.05)
            sem6 = Entry(cgpa_page)
            sem6.place(relx = 0.53 , rely = 0.5 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA")
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page )
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto6())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)
            
        if a == "Sem 7":
            def upto7():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                s4 = sem4.get()
                s5 = sem5.get()
                s6 = sem6.get()
                s7 = sem7.get()
                cgpa = (float(s1)+float(s2)+float(s3)+float(s4)+float(s5)+float(s6)+float(s7))/7
                final_cgpa.insert(END , cgpa)
                                
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page )
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA")
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page )
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page)
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            sem4_label = Label(cgpa_page , text = "Sem 4 GPA")
            sem4_label.place(relx = 0.17 , rely = 0.37 , relwidth = 0.3 , relheight = 0.05)
            sem4 = Entry(cgpa_page)
            sem4.place(relx = 0.53 , rely = 0.37 , relwidth = 0.4 , relheight = 0.05)

            sem5_label = Label(cgpa_page , text = "Sem 5 GPA" )
            sem5_label.place(relx = 0.17 , rely = 0.44 , relwidth = 0.3 , relheight = 0.05)
            sem5 = Entry(cgpa_page)
            sem5.place(relx = 0.53 , rely = 0.44 , relwidth = 0.4 , relheight = 0.05)

            sem6_label = Label(cgpa_page , text = "Sem 6 GPA" )
            sem6_label.place(relx = 0.17 , rely = 0.5 , relwidth = 0.3 , relheight = 0.05)
            sem6 = Entry(cgpa_page )
            sem6.place(relx = 0.53 , rely = 0.5 , relwidth = 0.4 , relheight = 0.05)
            
            sem7_label = Label(cgpa_page , text = "Sem 7 GPA" )
            sem7_label.place(relx = 0.17 , rely = 0.57 , relwidth = 0.3 , relheight = 0.05)
            sem7 = Entry(cgpa_page )
            sem7.place(relx = 0.53 , rely = 0.57 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA" )
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto7())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)

        if a == "Sem 8":
            def upto8():
                s1 = sem1.get()
                s2 = sem2.get()
                s3 = sem3.get()
                s4 = sem4.get()
                s5 = sem5.get()
                s6 = sem6.get()
                s7 = sem7.get()
                s8 = sem8.get()
                cgpa = (float(s1)+float(s2)+float(s3)+float(s4)+float(s5)+float(s6)+float(s7)+float(s8))/8
                final_cgpa.insert(END , cgpa)
            sem1_label = Label(cgpa_page , text = "Sem 1 GPA")
            sem1_label.place(relx = 0.17 , rely = 0.16 , relwidth = 0.3 , relheight = 0.05)
            sem1 = Entry(cgpa_page)
            sem1.place(relx = 0.53 , rely = 0.16 , relwidth = 0.4 , relheight = 0.05)

            sem2_label = Label(cgpa_page , text = "Sem 2 GPA" )
            sem2_label.place(relx = 0.17 , rely = 0.23 , relwidth = 0.3 , relheight = 0.05)
            sem2 = Entry(cgpa_page)
            sem2.place(relx = 0.53 , rely = 0.23 , relwidth = 0.4 , relheight = 0.05)
            
            sem3_label = Label(cgpa_page , text = "Sem 3 GPA")
            sem3_label.place(relx = 0.17 , rely = 0.3 , relwidth = 0.3 , relheight = 0.05)
            sem3 = Entry(cgpa_page )
            sem3.place(relx = 0.53 , rely = 0.3 , relwidth = 0.4 , relheight = 0.05)

            sem4_label = Label(cgpa_page , text = "Sem 4 GPA" )
            sem4_label.place(relx = 0.17 , rely = 0.37 , relwidth = 0.3 , relheight = 0.05)
            sem4 = Entry(cgpa_page )
            sem4.place(relx = 0.53 , rely = 0.37 , relwidth = 0.4 , relheight = 0.05)

            sem5_label = Label(cgpa_page , text = "Sem 5 GPA" )
            sem5_label.place(relx = 0.17 , rely = 0.44 , relwidth = 0.3 , relheight = 0.05)
            sem5 = Entry(cgpa_page)
            sem5.place(relx = 0.53 , rely = 0.44 , relwidth = 0.4 , relheight = 0.05)

            sem6_label = Label(cgpa_page , text = "Sem 6 GPA" )
            sem6_label.place(relx = 0.17 , rely = 0.5 , relwidth = 0.3 , relheight = 0.05)
            sem6 = Entry(cgpa_page)
            sem6.place(relx = 0.53 , rely = 0.5 , relwidth = 0.4 , relheight = 0.05)
            
            sem7_label = Label(cgpa_page , text = "Sem 7 GPA" )
            sem7_label.place(relx = 0.17 , rely = 0.57 , relwidth = 0.3 , relheight = 0.05)
            sem7 = Entry(cgpa_page )
            sem7.place(relx = 0.53 , rely = 0.57 , relwidth = 0.4 , relheight = 0.05)

            sem8_label = Label(cgpa_page , text = "Sem 8 GPA")
            sem8_label.place(relx = 0.17 , rely = 0.64 , relwidth = 0.3 , relheight = 0.05)
            sem8 = Entry(cgpa_page)
            sem8.place(relx = 0.53 , rely = 0.64 , relwidth = 0.4 , relheight = 0.05)

            final_label = Label(cgpa_page , text = "Your CGPA")
            final_label.place(relx = 0.17 , rely = 0.83 , relwidth = 0.3 , relheight = 0.05)
            final_cgpa = Entry(cgpa_page)
            final_cgpa.place(relx = 0.53 , rely = 0.83 , relwidth = 0.4 , relheight = 0.05)
            final_submit = Button(mainpage , text = "Submit" , command = lambda: upto8())
            final_submit.place(relx = 0.4 , rely = 0.75 , relheight = 0.05 , relwidth = 0.2)
            
    clicked = StringVar()
    clicked.set("Sem 8")
    
    cgpa_page = Frame(mainpage)
    cgpa_page.place(relx = 0 , rely = 0.1 , relheight = 0.9 , relwidth = 1)

    select_label = Label(mainpage , text = "Number of semesters completed")
    select_label.place(relx = 0.2 , rely = 0.1 , relheight = 0.05 , relwidth = 0.3)

    sem_number = OptionMenu(mainpage , clicked , "Sem 1","Sem 2","Sem 3", "Sem 4","Sem 5","Sem 6", "Sem 7" , "Sem 8")
    sem_number.place(relx = 0.5 , rely = 0.1 , relheight = 0.05 , relwidth = 0.3)

    sem_submit = Button(mainpage , text = "Submit" , command = lambda: cgpa(cgpa_page))
    sem_submit.place(relx = 0.4 , rely = 0.16 , relheight = 0.05 , relwidth = 0.2)
    
root = Tk()
root.title("Cgpa")

mainpage = Canvas(root , height = 700 , width = 700)
mainpage.pack()

gpa_button = Button(mainpage , text = "GPA" ,  command = lambda: calgpa())
gpa_button.place(relx = 0 , rely = 0 , relheight = 0.081 , relwidth = 0.5)

cgpa_button = Button(mainpage , text = "CGPA" , command = lambda: calcgpa())
cgpa_button.place(relx = 0.5 , rely = 0 , relheight = 0.081 , relwidth = 0.5)

root.resizable(0,0)
root.mainloop()

