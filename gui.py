from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt
from tkinter import font
import turtle
from math import radians, sin, cos
from functools import partial

#libraries imported


Questions=[(1,1,'A cliff diver jumps from a point 28m above the surface of the water. Modelling the diver as a particle moving freely under gravity with initial speed 0, \n find the speed of the diver when he hits the water','23.4'),
           (1,2,'A particle P is projected vertically downwards from a point 80m above the ground with speed 4m/s. Find, the speed which P hits the ground','39.8'),
           (1,3,'A pebble is catapulted vertically upwards with speed 24m/s. Find the greatest height aboive point of projection reached by pebble','29.4'),
           (1,4,'A particle is projected vertically upwards from a point O with speed U m/s, the greatest height reached is 62.5m. Find U','35'),
           (1,5,'A ball is released from rest at a point which is 10m above a wooden floor. Each time the ball strikes the floor, it rebounds with the three quarters of the speed \n with which it strikes the floor. Find the greatest height above the floor reached by the ball after the first time it rebounds from the floor ','5.6'),
           (2,1,'A particle moves in a straight line from a point A to B with a constant deceleration of 4m/s^2. At A the particle has speed 32m/s and the particle comes to rest at B. \n Find the time taken for the particle to travel from A to B','8'),
           (2,2,'A cyclist is moving along a straight road from A to B with constant acceleration 0.5m/s^2. Her velocity at A is 3m/s and it takes 12s to cycle from A to B. \n Find velocity at B','9'),
           (2,3,'A particle moves along a straight line with constant acceleration 3m/s^2. The particle moves 38m in 4s. Find initial speed','3.5'),
           (2,4,'A particle P is moving on the x-axis with constant deceleration 4m/s^2. At time t=0, P passes through the origin O with velocity 14m/s in the positive direction. \n The point A lies on the x-axis and OA=22.5m. Find the difference in times when P passes through A.','2'),
           (2,5,'A car is travelling along a straight horizontal road with constant acceleration. The car passes over three consecutive points A, B and C where AB=100m and BC=300m. \n The speed of the car at B is 14m/s and the speed of the car at C is 20m/s. Find acceleration of the car.','0.34'),
           (3,1,'A particle is projected with speed 35m/s at an angle of elevation of 60 degrees. Find the time the particle takes to reach its greatest height','3.1'),
           (3,2,'A particle is projected with speed 21m/s ata an angle of elevation X. Given that the greatest height reached above the point of projection is 15m, \n find the value of X, to the nearest degree.','55'),
           (3,3,'A ball i sprojected from a point A on level ground with speed 24m/s. The ball is projected at an angle X where sinX= 4/5. The ball moves freely under gravity \n until it strikes the ground at B. Find the time of flight.','3.9'),
           (3,4,'A particle is projected horizontally from a point A which is 16m above horizontal ground. The projectile strikes the gound at a point B \n which is at a horizontal distance of 140m from A. Find the speed of projection of particle','77.5'),
           (3,5,'A stone is thrown with speed 30m/s from a window which is 20m above the horizontal ground. The stone hits the ground 3.5s later. Find the angle of projection of the stone','22.4')]


#create database if it doesnt exist
def createDb():
    conn = sqlite3.connect('simulator16.db')
    ##creating and connecting database
    c = conn.cursor()
    ##creates a cursor for searching database

    c.execute('''CREATE TABLE IF NOT EXISTS results
                (resultID int,username text,Q1 int,Q2 int,Q3 int,Q4 int,Q5 int,total int)''')
    #creates an empty table with fields above and there data type

    #when adding the data the '?,?...' represents 8 fields are present


    a=c.execute('''CREATE TABLE IF NOT EXISTS Questions
                (question_type int, question_num int, question text, answer text)''')
    b=c.execute("SELECT COUNT(*) FROM Questions")
    for row in b:
        count=(row[0])
    if count == 0:
        c.executemany('INSERT INTO Questions VALUES (?,?,?,?)',Questions)
    
    conn.commit()
    conn.close()




def velocity_angle(velocity,angle):
    run_sim(velocity.get(),angle.get())
    
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

    
    
def run_sim(velocity,angle):

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
    time=0
           
    while ball.ycor() >= -10:
        time=time+0.05                    
        changeInX = (velocity*cos(angle)) * time
        changeInY = ((velocity*sin(angle)) * time) + (0.5*-9.81*time*time) #suvat equations
        ball.sety(-10+changeInY)
        ball.setx(-330+changeInX)

def run_Vt(velocity1,acceleration,time1):
    Vt_graph(velocity1.get(),acceleration.get(),time1.get())

def Vt_graph(velocity,acceleration,time): #creates velocity time graph
    
    x = []
    for i in range(0,time+1):
        x.append(i)
        i+=1

    # corresponding y axis values
    y = []
    for i in range(0,time+1):
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
    
    x = []
    for i in range(0,time+1):
        x.append(i)
        i+=1

    # corresponding y axis values
    y = []
    for i in range(0,time+1):

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

def graphs(*args): #function for displaying graphing option, set values and select type of graph
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
   
    velocity1=IntVar()
    velocity1_entry = ttk.Entry(mainframe, width=10, textvariable=velocity1).grid(column=1, row=0, sticky=(N))
   
    time1=IntVar()
    time1_entry = ttk.Entry(mainframe, width=10, textvariable=time1).grid(column=1, row=1, sticky=(N))
   
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
    font_change = font.Font(family='Helvetica', size=20, weight='bold')
    ttk.Label(mainframe, text="PARTICLES ON A FLAT PLANE",font=font_change,foreground='red').grid (column=0, row=0, sticky=(N))
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
    #   padding adds extra space around the widget
    #create the frame for the window
    mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
    #sticky means how the widget would line up within the grid cell
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
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
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==(?)',[(x)]): ## sql statement to query database
        if answers[i] == row[2]:
            finalResults[i]=1  ##retrieves value in variable and compares if equal to value in the above position in the row
            ttk.Label(mainframe, text='correct',style='Mycolour.TLabel').grid (column=2, row=i+1, sticky=(N))
            count+=1        
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
    value= "simulator16.db"
    conn = sqlite3.connect(value)
    ##connects to database
    c=conn.cursor()
    ##creates cursor   
    for row in c.execute('SELECT question_num, question, answer FROM Questions WHERE question_type==3'):
        question=row[1]
        a=row[0]
        i=row[0]
        i=ttk.Label(mainframe, text=question,style='Mycolour.TLabel').grid (column=0, row=i*2, sticky=(N))

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

root = tk.Tk() 
root.title("Mechanics simulator")

root.geometry("685x600")


createDb()
home()



