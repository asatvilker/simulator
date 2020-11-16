from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import font
import turtle
from math import radians, sin, cos
from functools import partial
from database import createDb
#libraries imported
def velocity_angle(velocity,angle):
    simulators(velocity.get(),angle.get())
    

def simulator(*args):
    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "50 100 50 100")
    subframe = ttk.Frame(mainframe,padding= "50 25 50 25",relief='sunken')
    velocity_frame= ttk.Frame(mainframe,padding= "50 25 50 25",relief='sunken')
    angle_frame= ttk.Frame(mainframe,padding= "50 25 50 25",relief='sunken')
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
    subframe.grid (column=0, row=4, sticky=(N, W, E, S))
    velocity_frame.grid (column=0, row=2, sticky=(N, W, E, S))
    angle_frame.grid (column=0, row=3, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=5)
    mainframe.rowconfigure(0, weight=5)
    subframe.columnconfigure(0, weight=5)
    subframe.rowconfigure(0, weight=5)
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="SIMULATOR/CALCULATOR",font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
    ttk.Label(velocity_frame, text="Slide to change velocity (m/s)", foreground='red').grid (column=3, row=0, sticky=(N))
    ttk.Label(angle_frame, text="Slide to change angle of elevation (degrees)", foreground='red').grid (column=3, row=0, sticky=(N))
    ttk.Button(subframe, text="HOME", command=home).grid(column=0, row=11, sticky=S)
    
    velocity = tk.Scale(velocity_frame, orient=HORIZONTAL, length=200, from_=0.0, to=100.0)
    velocity.grid(column=0, row=0, sticky=N)
    
    angle = tk.Scale(angle_frame, orient=HORIZONTAL, length=200, from_=0.0, to=180.0)
    angle.grid(column=0, row=0, sticky=N)
    ttk.Button(subframe, text="GO", command=partial(velocity_angle,velocity,angle)).grid(column=0, row=11, sticky=S)
    ttk.Button(subframe, text="HOME", command=home).grid(column=1, row=11, sticky=S)

    
    
def simulators(velocity,angle):

    cv = tk.Canvas(width=200,height=200)
    t = turtle.RawTurtle(cv)
    
    angle=radians(angle)

    wn=turtle.Screen()
    
    wn.bgcolor('#FFD700')
    wn.title("projectile")

    ball= turtle.Turtle()
    ball.shape('circle')
    ball.color('#DC143C')
    ball.penup()
    ball.speed(0)
    ball.goto(-330,-10)
    ball.pendown()
    ball.dy=0

    g=0.1
    time=0

                        
    while ball.ycor() >= -10:
        time=time+0.05                    
        changeInX = (velocity*cos(angle)) * time
        changeInY = ((velocity*sin(angle)) * time) + (0.5*-9.81*time*time)
        ball.sety(-10+changeInY)
        ball.setx(-330+changeInX)
def run_Vt(velocity1,acceleration,time1):
    Vt_graph(velocity1.get(),acceleration.get(),time1.get())
def Vt_graph(velocity,acceleration,time):
    import matplotlib.pyplot as plt
    x = []
    for i in range(0,time+1):
        x.append(i)
        i+=1

    # corresponding y axis values
    y = []
    for i in range(0,time+1):
##        print('at',i,'seconds')
        v=velocity+ acceleration*i

        y.append(v)
        i+=1
                  
    # plotting the points 
    plt.plot(x, y)
     
    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('velocity (m/s)')
     
    # giving a title to my graph
    plt.title('V/t graph')
     
    # function to show the plot
    plt.show()
def run_St(velocity1,acceleration,time1):
    St_graph(velocity1.get(),acceleration.get(),time1.get())
def St_graph(velocity,acceleration,time):
    import matplotlib.pyplot as plt
    x = []
    for i in range(0,time+1):
        x.append(i)
        i+=1

    # corresponding y axis values
    y = []
    for i in range(0,time+1):
##        print('at',i,'seconds')
        s=velocity*i + (0.5*acceleration*i*i)

        y.append(s)
        i+=1
                  
    # plotting the points 
    plt.plot(x, y)
     
    # naming the x axis
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('displacement (m)')
     
    # giving a title to my graph
    plt.title('S/t graph')
    plt.show()
def graphs(*args):
    root.geometry("685x600")
#set the dimensions of the window
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    mainframe = ttk.Frame(root,padding= "100 200 100 200")
    displacement_frame = ttk.Frame(mainframe,padding= "50 50 50 50",relief='sunken')
    velocity_frame = ttk.Frame(mainframe,padding= "50 50 50 50",relief='sunken')
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
    displacement_frame.grid (column=0, row=3, sticky=(N, W, E, S))
    velocity_frame.grid (column=1, row=3, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=5)
    mainframe.rowconfigure(0, weight=5)
    ttk.Label(mainframe, text=" Enter velocity: ",font=font_change, foreground='red').grid (column=0, row=0, sticky=(N))
    ttk.Label(mainframe, text=" Enter time: ",font=font_change, foreground='red').grid (column=0, row=1, sticky=(N))
    ttk.Label(mainframe, text=" Enter acceleration: ",font=font_change, foreground='red').grid (column=0, row=2, sticky=(N))
    #global velocity1
    velocity1=IntVar()
    velocity1_entry = ttk.Entry(mainframe, width=10, textvariable=velocity1).grid(column=1, row=0, sticky=(N))
    #global time1
    time1=IntVar()
    time1_entry = ttk.Entry(mainframe, width=10, textvariable=time1).grid(column=1, row=1, sticky=(N))
    #global acceleration
    acceleration=IntVar()
    acceleration_entry = ttk.Entry(mainframe, width=10, textvariable=acceleration).grid(column=1, row=2, sticky=(N))
    
    ttk.Button(mainframe, text="HOME", command=home).grid(column=1, row=11, sticky=(N))
    ttk.Label(displacement_frame, text=" Select for displacement/time graph ",font=font_change, foreground='red').grid (column=1, row=0, sticky=(N))
    displacement_check= Checkbutton(displacement_frame, state=ACTIVE, command=partial(run_St,velocity1,acceleration,time1)).grid (column=1, row=1, sticky=(N))
    ttk.Label(velocity_frame, text=" Select for velocity/time graph ",font=font_change, foreground='red').grid (column=1, row=0, sticky=(N))
    velocity_check= Checkbutton(velocity_frame, state=ACTIVE, command=partial(run_Vt,velocity1,acceleration,time1)).grid (column=1, row=1, sticky=(N))
def Test_q(*args):
    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "100 200 100 200")
    subframe = ttk.Frame(mainframe,padding= "100 50 100 50",relief='sunken')
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
    subframe.grid (column=2, row=15, sticky=(N, W, E, S))
    
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=5)
    mainframe.rowconfigure(0, weight=5)
    subframe.columnconfigure(0, weight=5)
    subframe.rowconfigure(0, weight=5)

    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text=" TEST ",font=font_change, foreground='red').grid (column=2, row=1, sticky=(N))
    ttk.Label(mainframe, text="Please select a topic").grid (column=2, row=5, sticky=(N))
    ttk.Button(subframe, text="FLAT PLANE", command=Test_q_flat).grid(column=1, row=10, sticky=S)
    ttk.Button(subframe, text="FREE FALL", command=Test_q_free).grid(column=2, row=10, sticky=S)

    ttk.Button(subframe, text="PROJECTILES", command=Test_q_projectile).grid(column=3, row=10, sticky=S)
    ttk.Button(subframe, text="HOME", command=home).grid(column=2, row=11, sticky=S)


########################################################################################################################


def Test_q_flat(*args):
    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "100 200 100 200")
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
##    ttk.Button(mainframe, text="HOME", command=home).grid(column=2, row=11, sticky=S)
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="PARTICLES ON A FLAT PLANE",font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
    import sqlite3
    value= "simulator16.db"
    conn = sqlite3.connect(value)
    c=conn.cursor()
    
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==1'):
        question=row[1]
        a=row[0]
        i=row[0]
        i=ttk.Label(mainframe, text=question,style='Mycolour.TLabel').grid (column=0, row=i*2, sticky=(N))
    
    a_1=StringVar()
    a_1_entry = ttk.Entry(mainframe, width=30, textvariable=a_1)
    a_1_entry.grid(column=0, row=3, sticky=(N))
     
    a_2=StringVar()
    a_2_entry = ttk.Entry(mainframe, width=30, textvariable=a_2)
    a_2_entry.grid(column=0, row=5, sticky=(N))
   
    a_3=StringVar()
    a_3_entry = ttk.Entry(mainframe, width=30, textvariable=a_3)
    a_3_entry.grid(column=0, row=7, sticky=(N))
   
    a_4=StringVar()
    a_4_entry = ttk.Entry(mainframe, width=30, textvariable=a_4)
    a_4_entry.grid(column=0, row=9, sticky=(N))
    
    a_5=StringVar()
    a_5_entry = ttk.Entry(mainframe, width=30, textvariable=a_5)
    a_5_entry.grid(column=0, row=11, sticky=(N))

    ttk.Button(mainframe, text="ENTER", command=partial(results, 1, a_1,a_2,a_3,a_4,a_5)).grid(column=2, row=11, sticky=S)
    conn.close()
################################################################################################################################




def Test_q_free(*args):

    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "100 200 100 200")
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=5)
    mainframe.rowconfigure(0, weight=5)
    ttk.Button(mainframe, text="HOME", command=home).grid(column=2, row=11, sticky=S)
    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "100 200 100 200")
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="PARTICLES IN FREE FALL",font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
    import sqlite3
    value= "simulator16.db"
    conn = sqlite3.connect(value)
    c=conn.cursor()
    
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==2'):
        question=row[1]
        a=row[0]
        i=row[0]
        i=ttk.Label(mainframe, text=question,style='Mycolour.TLabel').grid (column=0, row=i*2, sticky=(N))
    
    a_1=StringVar()
    a_1_entry = ttk.Entry(mainframe, width=30, textvariable=a_1)
    a_1_entry.grid(column=0, row=3, sticky=(N))
     
    a_2=StringVar()
    a_2_entry = ttk.Entry(mainframe, width=30, textvariable=a_2)
    a_2_entry.grid(column=0, row=5, sticky=(N))
    
    a_3=StringVar()
    a_3_entry = ttk.Entry(mainframe, width=30, textvariable=a_3)
    a_3_entry.grid(column=0, row=7, sticky=(N))
    
    a_4=StringVar()
    a_4_entry = ttk.Entry(mainframe, width=30, textvariable=a_4)
    a_4_entry.grid(column=0, row=9, sticky=(N))
   
    a_5=StringVar()
    a_5_entry = ttk.Entry(mainframe, width=30, textvariable=a_5)
    a_5_entry.grid(column=0, row=11, sticky=(N))

    ttk.Button(mainframe, text="ENTER", command=partial(results, 2,a_1,a_2,a_3,a_4,a_5)).grid(column=2, row=11, sticky=S)
    conn.close()
######################################################################################################################################




def results(x,a_1,a_2,a_3,a_4,a_5):
    value= "simulator16.db"
    conn = sqlite3.connect(value)
    c=conn.cursor()

    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "100 200 100 200")
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
##    ttk.Button(mainframe, text="HOME", command=home).grid(column=2, row=11, sticky=S)
    count=0
##set count variable to 0
    name_upper=name.get().upper()
##retrieve the value of name and make it upper case
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
##formatting for font change
    ttk.Label(mainframe, text="HERE ARE YOUR RESULTS "+name_upper,font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
    ttk.Label(mainframe, text="LEADERBOARD",font=font_change,foreground='red').grid (column=5, row=0, sticky=(N))
    ttk.Label(mainframe, text="username",font=font_change,foreground='red').grid (column=4, row=1, sticky=(N))
    ttk.Label(mainframe, text="score",font=font_change,foreground='red').grid (column=6, row=1, sticky=(N))
    ttk.Label(mainframe, text="QUESTION 1:",font=font_change,foreground='red').grid (column=0, row=1, sticky=(N))
    ttk.Label(mainframe, text="QUESTION 2:",font=font_change,foreground='red').grid (column=0, row=2, sticky=(N))
    ttk.Label(mainframe, text="QUESTION 3:",font=font_change,foreground='red').grid (column=0, row=3, sticky=(N))
    ttk.Label(mainframe, text="QUESTION 4:",font=font_change,foreground='red').grid (column=0, row=4, sticky=(N))
    ttk.Label(mainframe, text="QUESTION 5:",font=font_change,foreground='red').grid (column=0, row=5, sticky=(N))
    ttk.Button(mainframe, text="Back", command=Test_q_projectile).grid(column=2, row=7, sticky=S)
    ttk.Button(mainframe, text="Home", command=home).grid(column=1, row=7, sticky=S)
    answers=[a_1.get(),a_2.get(),a_3.get(),a_4.get(),a_5.get()]
    finalResults=[0,0,0,0,0]
    i=0
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==(?)',[(x)]):
        
## sql statement to query database
        if answers[i] == row[2]:
            finalResults[i]=1
##retrieves value in variable and compares if equal to value in the above position in the row
            
##changes value in database
            ttk.Label(mainframe, text='correct',style='Mycolour.TLabel').grid (column=2, row=i+1, sticky=(N))
            count+=1
##adds 1 to count variable           
        i+=1
    ttk.Label(mainframe, text=count,font=font_change,foreground='green').grid (column=2, row=6, sticky=(N))

    user=name.get()
    for row in c.execute('SELECT COUNT(*) FROM results'):
        ID= row[0]+1
    record = [(ID,str(user),finalResults[0],finalResults[1],finalResults[2],finalResults[3],finalResults[4],count)]
    c.executemany('INSERT INTO results VALUES (?,?,?,?,?,?,?,?)', record)
    for row in c.execute('SELECT * FROM results'):
        print(row)
    m=1
    for row in c.execute('SELECT username, total FROM results ORDER BY total DESC'):
        ttk.Label(mainframe, text=row[0],style='Mycolour.TLabel').grid (column=4, row=m+1, sticky=(N))
        ttk.Label(mainframe, text=row[1],style='Mycolour.TLabel').grid (column=6, row=m+1, sticky=(N))
        m+=1
        
##displays value currently in count
    
    conn.commit()
##saves changes to database
    conn.close()

def Test_q_projectile(*args):
    root.geometry("685x600")
#set the dimensions of the window

    mainframe = ttk.Frame(root,padding= "10 200 10 200")
#padding adds extra space around the widget
#create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
#sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=5)
    mainframe.rowconfigure(0, weight=5)
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="PARTICLES PROJECTED AT AN ANGLE",font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
    import sqlite3
##imports library for using sql
    value= "simulator16.db"
    conn = sqlite3.connect(value)
##connects to database
    c=conn.cursor()
##creates cursor   
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==3'):
##sql statement for querying database with a condition
        question=row[1]
        a=row[0]
        i=row[0]
##stores the contents of the item in the given position of the row in the above variables
        i=ttk.Label(mainframe, text=question,style='Mycolour.TLabel').grid (column=0, row=i*2, sticky=(N))
##code for creating label is stored in variable above
    
##declares variable as global to later access outside function
    a_1=StringVar()
##sets the data type for the variable
    a_1_entry = ttk.Entry(mainframe, textvariable=a_1)
    a_1_entry.grid(column=0, row=3, sticky=(N))
##creates a widget to enter answer and stores it in variable
      
    a_2=StringVar()
    a_2_entry = ttk.Entry(mainframe, textvariable=a_2)
    a_2_entry.grid(column=0, row=5, sticky=(N))
    
    a_3=StringVar()
    a_3_entry = ttk.Entry(mainframe, textvariable=a_3)
    a_3_entry.grid(column=0, row=7, sticky=(N))
    
    a_4=StringVar()
    a_4_entry = ttk.Entry(mainframe, textvariable=a_4)
    a_4_entry.grid(column=0, row=9, sticky=(N))
    
    a_5=StringVar()
    a_5_entry = ttk.Entry(mainframe, textvariable=a_5)
    a_5_entry.grid(column=0, row=11, sticky=(N))
    ttk.Button(mainframe, text="ENTER", command=partial(results, 3,a_1,a_2,a_3,a_4,a_5)).grid(column=2, row=11, sticky=S)
    conn.close()





############################################################################################################################################

def connect(*args):
    value= "simulator16.db"
    conn = sqlite3.connect(value)
    c=conn.cursor()
    
##    additional_window = tk.Toplevel()   #***********HERE******* 
##    additional_window.title("welcome")
#function to connect databse to the programme    
    
    conn.commit()
    conn.close()
    




def home(*args):
   

    #set the dimensions of the window
    s = ttk.Style()
    s.configure('Mycolour.TFrame',background='red')
    s.configure('Mycolour.TButton',background='red',foreground='red')
    s.configure('Mycolour.TLabel',background='red',foreground='red')

    mainframe = ttk.Frame(root,padding= "100 200 100 200",relief='sunken',style='Mycolour.TFrame')
    subframe = ttk.Frame(mainframe,padding= "100 50 100 50",relief='sunken',style='Mycolour.TFrame')
    ##mainframe.configure(background='red')
    #padding adds extra space around the widget
    #create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
    subframe.grid (column=2, row=15, sticky=(N, W, E, S))
    #sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    subframe.columnconfigure(0, weight=5)
    subframe.rowconfigure(0, weight=5)

    #column and row configure tells Tk that if the main window is resized, the frame should expand to take up extra space
    global name
    name=StringVar()
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="MECHANICS IN MATHS",font=font_change,foreground='red').grid (column=2, row=0, sticky=(N))
    ttk.Label(mainframe, text="Please enter a username",style='Mycolour.TLabel').grid (column=2, row=5, sticky=(N))
    name_entry = ttk.Entry(mainframe, width=30, textvariable=name)
    name_entry.grid(column=2, row=10, sticky=(N))
    ttk.Button(mainframe, text="ENTER", command=connect, style='Mycolour.TButton').grid(column=2, row=10, sticky=E)
    ttk.Button(subframe, text="TEST", command=partial(Test_q), style='Mycolour.TButton').grid(column=1, row=10, sticky=S)
    ttk.Button(subframe, text="GRAPHS", command=graphs,style='Mycolour.TButton').grid(column=2, row=10, sticky=S)

    ttk.Button(subframe, text="SIMULATOR", command=simulator,style='Mycolour.TButton').grid(column=3, row=10, sticky=S)

    ##frame = ttk.Frame(subframe,borderwidth=10, relief='sunken').grid(column=2,row=15, sticky=(S))
root = tk.Tk()
root.title("Mechanics simulator")

root.geometry("685x600")



home()

createDb()

