import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Car:
    def __init__(self, point: Point):
        # Reference
        self.rear_axle = point

        # Constants (bb values)
        self.max_x = 3
        self.min_x = -1
        self.max_y = 1
        self.min_y = -1

        # Initial heading, with x as 0 counter clockwise
        self.heading = 0

        # Starting corners at heading 0
        #
        #       ^ y+
        #       |
        #    rl_|_____fl
        #    |         |
        # ---| ra      |-----> x+
        #    |         |
        #    rr_______fr
        #       |
        #       |
        #       |

        self.front_right = Point(self.rear_axle.x + self.max_x, self.rear_axle.y + self.min_y)
        self.front_left = Point(self.rear_axle.x + self.max_x, self.rear_axle.y + self.max_y)
        self.rear_right = Point(self.rear_axle.x + self.min_x, self.rear_axle.y + self.min_y) 
        self.rear_left = Point(self.rear_axle.x + self.min_x, self.rear_axle.y + self.max_y)

    def __repr__(self):
        rep = f"Rear axle x: {self.rear_axle.x}, y: {self.rear_axle.y}\
                \nTop right x: {self.front_right.x}, y: {self.front_right.y}\
                \nTop left x: {self.front_left.x}, y: {self.front_left.y}\
                \nBottom right x: {self.rear_right.x}, y: {self.rear_right.y}\
                \nBottom left x: {self.rear_left.x}, y: {self.rear_left.y}"

        return rep

    def rotate(self, angle: float):
        self.heading = angle
        c_tr_x = self.front_right.x
        c_tr_y = self.front_right.y
        self.front_right.x = self.rear_axle.x + (c_tr_x - self.rear_axle.x) * math.cos(angle) - \
                        (c_tr_y - self.rear_axle.y) * math.sin(angle)
        self.front_right.y = self.rear_axle.y + (c_tr_x - self.rear_axle.x) * math.sin(angle) + \
                        (c_tr_y - self.rear_axle.y) * math.cos(angle)

        c_tl_x = self.front_left.x
        c_tl_y = self.front_left.y
        self.front_left.x = self.rear_axle.x + (c_tl_x - self.rear_axle.x) * math.cos(angle) - \
                        (c_tl_y - self.rear_axle.y) * math.sin(angle)
        self.front_left.y = self.rear_axle.y + (c_tl_x - self.rear_axle.x) * math.sin(angle) + \
                        (c_tl_y - self.rear_axle.y) * math.cos(angle)

        c_br_x = self.rear_right.x
        c_br_y = self.rear_right.y
        self.rear_right.x = self.rear_axle.x + (c_br_x - self.rear_axle.x) * math.cos(angle) - \
                        (c_br_y - self.rear_axle.y) * math.sin(angle)
        self.rear_right.y = self.rear_axle.y + (c_br_x - self.rear_axle.x) * math.sin(angle) + \
                        (c_br_y - self.rear_axle.y) * math.cos(angle)

        c_bl_x = self.rear_left.x
        c_bl_y = self.rear_left.y
        self.rear_left.x = self.rear_axle.x + (c_bl_x - self.rear_axle.x) * math.cos(angle) - \
                        (c_bl_y - self.rear_axle.y) * math.sin(angle)
        self.rear_left.y = self.rear_axle.y + (c_bl_x - self.rear_axle.x) * math.sin(angle) + \
                        (c_bl_y - self.rear_axle.y) * math.cos(angle)

    def step(self, speed: int, heading: float):
        self.heading = heading

        self.rear_axle.x += speed * math.cos(self.heading)
        self.rear_axle.y += speed * math.sin(self.heading)

        self.front_right = Point(self.rear_axle.x + self.max_x, self.rear_axle.y + self.min_y)
        self.front_left = Point(self.rear_axle.x + self.max_x, self.rear_axle.y + self.max_y)
        self.rear_right = Point(self.rear_axle.x + self.min_x, self.rear_axle.y + self.min_y) 
        self.rear_left = Point(self.rear_axle.x + self.min_x, self.rear_axle.y + self.max_y) 

        self.rotate(self.heading)

if __name__=='__main__':
    i = 0
    heading = 0

    start_point = Point(-10, -10)
    c = Car(start_point)

    fig, ax = plt.subplots()

    plt.ion()
    plt.axis([-100,100,-100,100])
    plt.xlim([-50,70])
    plt.ylim([-50,70])
    #x positive, y positive
    Box1 = [Point(10,10), Point(20,10), Point(20,0), Point(10,0)]
    #x negative, y positive
    Box2 = [Point(-10,60), Point(-20,60), Point(-20,40), Point(-10,40)]
    #x positive, y negative 
    Box3 = [Point(0,-5), Point(20,-5), Point(20,-30), Point(0,-30)]
    #x negative, y negative
    Box4 = [Point(-10,-10), Point(-30,-10), Point(-30,0), Point(-10,0)]

    ax.plot([Box1[0].x, Box1[1].x, Box1[2].x, Box1[3].x], [Box1[0].y, Box1[1].y, Box1[2].y, Box1[3].y], 'ko', markersize=2)
    ax.plot([Box2[0].x, Box2[1].x, Box2[2].x, Box2[3].x], [Box2[0].y, Box2[1].y, Box2[2].y, Box2[3].y], 'ko', markersize=2)
    ax.plot([Box3[0].x, Box3[1].x, Box3[2].x, Box3[3].x], [Box3[0].y, Box3[1].y, Box3[2].y, Box3[3].y], 'ko', markersize=2)
    ax.plot([Box4[0].x, Box4[1].x, Box4[2].x, Box4[3].x], [Box4[0].y, Box4[1].y, Box4[2].y, Box4[3].y], 'ko', markersize=2)

    while i <= 1000:
        if i % 1 == 0 and i != 0:
            heading += 2
        c.step(1,math.radians(heading))

        a1 = ax.plot(c.rear_axle.x, c.rear_axle.y, 'go', markersize=1)
        if (c.front_left.x >= 0 and c.front_left.y >=0 and c.front_left.x >= 10 and c.front_left.x <= 20 and c.front_left.y >= 0 and c.front_left.y <= 10):
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'ro', markersize=2)
        elif (c.front_left.x < 0 and c.front_left.y < 0 and c.front_left.x >= -30 and c.front_left.x <= -10 and c.front_left.y >= -10 and c.front_left.y <= 0):
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'ro', markersize=2)
        elif (c.front_left.x < 0 and c.front_left.y > 0 and c.front_left.x >= -20 and c.front_left.x <= -10 and c.front_left.y >= 40 and c.front_left.y <= 60):
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'ro', markersize=2)
        elif (c.front_left.x > 0 and c.front_left.y < 0 and c.front_left.x >= 0 and c.front_left.x <= 20 and c.front_left.y >= -30 and c.front_left.y <= -5):
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'ro', markersize=2)
        else:
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'bo', markersize=2)

        if (c.front_right.x >= 0 and c.front_right.y >= 0 and c.front_right.x >= 10 and c.front_right.x <= 20 and c.front_right.y >= 0 and c.front_right.y <= 10):
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'ro', markersize=2)
        elif (c.front_right.x < 0 and c.front_right.y < 0 and c.front_right.x >= -30 and c.front_right.x <= -10 and c.front_right.y >= -10 and c.front_right.y <= 0):
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'ro', markersize=2)
        elif (c.front_right.x < 0 and c.front_right.y > 0 and c.front_right.x >= -20 and c.front_right.x <= -10 and c.front_right.y >= 40 and c.front_right.y <= 60):
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'ro', markersize=2)
        elif (c.front_right.x > 0 and c.front_right.y < 0 and c.front_right.x >= 0 and c.front_right.x <= 20 and c.front_right.y >= -30 and c.front_right.y <= -5):
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'ro', markersize=2)
        else:
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'bo', markersize=2)

        if (c.rear_right.x >= 0 and c.rear_right.y >= 0 and c.rear_right.x >= 10 and c.rear_right.x <= 20 and c.rear_right.y >= 0 and c.rear_right.y <= 10):
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'ro', markersize=2)
        elif (c.rear_right.x < 0 and c.rear_right.y < 0 and c.rear_right.x >= -30 and c.rear_right.x <= -10 and c.rear_right.y >= -10 and c.rear_right.y <= 0):
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'ro', markersize=2)
        elif (c.rear_right.x < 0 and c.rear_right.y > 0 and c.rear_right.x >= -20 and c.rear_right.x <= -10 and c.rear_right.y >= 40 and c.rear_right.y <= 60):
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'ro', markersize=2)
        elif (c.rear_right.x > 0 and c.rear_right.y < 0 and c.rear_right.x >= 0 and c.rear_right.x <= 20 and c.rear_right.y >= -30 and c.rear_right.y <= -5):
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'ro', markersize=2)
        else:
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'bo', markersize=2)

        if (c.rear_left.x >= 0 and c.rear_left.y >= 0 and c.rear_left.x >= 10 and c.rear_left.x <= 20 and c.rear_left.y >= 0 and c.rear_left.y <= 10):
            a5 = ax.plot(c.rear_left.x, c.rear_left.y, 'ro', markersize=2)
        elif (c.rear_left.x < 0 and c.rear_left.y < 0 and c.rear_left.x >= -30 and c.rear_left.x <= -10 and c.rear_left.y >= -10 and c.rear_left.y <= 0):
            a5 = ax.plot(c.rear_left.x, c.rear_left.y, 'ro', markersize=2)
        elif (c.rear_left.x < 0 and c.rear_left.y > 0 and c.rear_left.x >= -20 and c.rear_left.x <= -10 and c.rear_left.y >= 40 and c.rear_left.y <= 60):
            a5 = ax.plot(c.rear_left.x, c.rear_left.y, 'ro', markersize=2)
        elif (c.rear_left.x > 0 and c.rear_left.y < 0 and c.rear_left.x >= 0 and c.rear_left.x <= 20 and c.rear_left.y >= -30 and c.rear_left.y <= -5):
            a5 = ax.plot(c.rear_left.x, c.rear_left.y, 'ro', markersize=2)
        else:
            a5 = ax.plot(c.rear_left.x, c.rear_left.y, 'bo', markersize=2)

        i += 1
        plt.show()
        plt.pause(0.05)
        line = a1.pop(0)
        line.remove()
        line2 = a2.pop(0)
        line2.remove()
        line3 = a3.pop(0)
        line3.remove()
        line4 = a4.pop(0)
        line4.remove()
        line5 = a5.pop(0)
        line5.remove()
