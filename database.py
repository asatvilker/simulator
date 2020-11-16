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

import sqlite3
#library for sql is imported
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

    for row in c.execute('SELECT * FROM Questions'):
        print(row)

    conn.commit()

    conn.close()

