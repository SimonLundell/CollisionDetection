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
