import math
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Box:
    def __init__(self, bottom_left, bottom_right, top_left, top_right):
        self.bl_x = bottom_left.x
        self.bl_y = bottom_left.y
        self.br_x = bottom_right.x
        self.br_y = bottom_right.y
        self.tl_x = top_left.x
        self.tl_y = top_left.y
        self.tr_x = top_right.x
        self.tr_y = top_right.y
    
    def min_x(self):
        return min(self.bl_x, self.br_x, self.tl_x, self.tr_x)

    def max_x(self):
        return max(self.bl_x, self.br_x, self.tl_x, self.tr_x)

    def min_y(self):
        return min(self.bl_y, self.br_y, self.tl_y, self.tr_y)

    def max_y(self):
        return max(self.bl_y, self.br_y, self.tl_y, self.tr_y)
    

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

def collision(ego_axle, targets) -> bool:
    for target in targets:
        if (ego_axle.x >= target.min_x() and ego_axle.x <= target.max_x() and ego_axle.y >= target.min_y() and ego_axle.y <= target.max_y()):
            return True

    return False

if __name__=='__main__':
    i = 0
    heading = 0

    c = Car(Point(-10,-10)) # Starting point
    Boxes = []

    fig, ax = plt.subplots()

    plt.ion()
    plt.axis([-100,100,-100,100])
    plt.xlim([-50,70])
    plt.ylim([-50,70])

    # Box(bl, br, tr, tl)
    #x positive, y positive
    Box1 = Box(Point(10,10), Point(20,10), Point(20,0), Point(10,0))
    Boxes.append(Box1)
    #x negative, y positive
    Box2 = Box(Point(-20,60), Point(-10,60), Point(-10,40), Point(-20,40))
    Boxes.append(Box2)
    #x positive, y negative 
    Box3 = Box(Point(0,-30), Point(20,-30), Point(20,-5), Point(0,-5))
    Boxes.append(Box3)
    #x negative, y negative
    Box4 = Box(Point(-30,-10), Point(-10,-10), Point(-10,0), Point(-30,0))
    Boxes.append(Box4)

    for Box in Boxes:
        ax.plot([Box.tl_x, Box.tr_x, Box.br_x, Box.bl_x], [Box.tl_y, Box.tr_y, Box.br_y, Box.bl_y], 'ko', markersize=2)

    while i <= 1000:
        if i % 1 == 0 and i != 0:
            heading += 2 # Turning over time
        c.step(1,math.radians(heading))

        a1 = ax.plot(c.rear_axle.x, c.rear_axle.y, 'go', markersize=1)
        if (collision(c.front_left, Boxes)):
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'ro', markersize=2)
        else:
            a2 = ax.plot(c.front_left.x, c.front_left.y, 'bo', markersize=2)

        if (collision(c.front_right, Boxes)):
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'ro', markersize=2)
        else:
            a3 = ax.plot(c.front_right.x, c.front_right.y, 'bo', markersize=2)

        if (collision(c.rear_right, Boxes)):
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'ro', markersize=2)
        else:
            a4 = ax.plot(c.rear_right.x, c.rear_right.y, 'bo', markersize=2)

        if (collision(c.rear_left, Boxes)):
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
