import math
from resources.Point import Point

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
