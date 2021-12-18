import math
import matplotlib.pyplot as plt

from resources.Point import Point
from resources.Box import Box
from resources.Car import Car

def collision(ego_axle, targets) -> bool:
    for target in targets:
        if (ego_axle.x >= target.min_x() and ego_axle.x <= target.max_x() and ego_axle.y >= target.min_y() and ego_axle.y <= target.max_y()):
            return True

    return False

if __name__=='__main__':
    i = 0
    heading = 0

    c = Car(Point(-10,-10)) # Starting point

    # Interactive plot, min 50 max 70
    fig, ax = plt.subplots()
    plt.ion()
    plt.xlim([-50,70])
    plt.ylim([-50,70])

    #x positive, y positive
    Box1 = Box(Point(10,10), Point(20,10), Point(20,0), Point(10,0))
    #x negative, y positive
    Box2 = Box(Point(-20,60), Point(-10,60), Point(-10,40), Point(-20,40))
    #x positive, y negative 
    Box3 = Box(Point(0,-30), Point(20,-30), Point(20,-5), Point(0,-5))
    #x negative, y negative
    Box4 = Box(Point(-30,-10), Point(-10,-10), Point(-10,0), Point(-30,0))
    Boxes =  [Box1, Box2, Box3, Box4]

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
