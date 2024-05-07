from graphics import*
class Toothpick:
    global pixel_length
    pixel_length = 63

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def add_toothpick_A(self, tlist):
        global pixel_length
        if self.direction == "horizontal":
            new_pick_A = Toothpick(self.x - (pixel_length // 2), self.y, "vertical")
        else:
            new_pick_A = Toothpick(self.x, self.y - (pixel_length // 2), "horizontal")

        for tpick in tlist:
            if self.is_equal(tpick, new_pick_A):
                return None
            else:
                if new_pick_A.direction == "horizontal":
                    temp_A = Toothpick(new_pick_A.x, new_pick_A.y + pixel_length // 2, "vertical")
                    temp_B = Toothpick(new_pick_A.x, new_pick_A.y - (pixel_length // 2), "vertical")
                elif new_pick_A.direction == "vertical":
                    temp_A = Toothpick(new_pick_A.x + (pixel_length // 2), new_pick_A.y, "horizontal")
                    temp_B = Toothpick(new_pick_A.x - (pixel_length // 2), new_pick_A.y, "horizontal")
                if self.is_present(temp_A, tlist) and self.is_present(temp_B, tlist):
                    return None
        return new_pick_A

    def add_toothpick_B(self, tlist):
        global pixel_length
        if self.direction == "horizontal":
            new_pick_B = Toothpick(self.x + (pixel_length // 2), self.y, "vertical")
        else:
            new_pick_B = Toothpick(self.x, self.y + (pixel_length // 2), "horizontal")

        for tpick in tlist:
            if self.is_equal(tpick, new_pick_B):
                return None
            else:
                if new_pick_B.direction == "horizontal":
                    temp_A = Toothpick(new_pick_B.x, new_pick_B.y + pixel_length // 2, "vertical")
                    temp_B = Toothpick(new_pick_B.x, new_pick_B.y - (pixel_length // 2), "vertical")
                elif new_pick_B.direction == "vertical":
                    temp_A = Toothpick(new_pick_B.x + (pixel_length // 2), new_pick_B.y, "horizontal")
                    temp_B = Toothpick(new_pick_B.x - (pixel_length // 2), new_pick_B.y, "horizontal")
                if self.is_present(temp_A, tlist) and self.is_present(temp_B, tlist):
                    return None
        return new_pick_B

    def show(self, win):
        global pixel_length
        if self.direction == "horizontal":
            p1 = Point(self.x - (pixel_length // 2), self.y)
            p2 = Point(self.x + (pixel_length // 2), self.y)
            line = Line(p1, p2)
            line.draw(win)
        else:
            p1 = Point(self.x, self.y - (pixel_length // 2))
            p2 = Point(self.x, self.y + (pixel_length // 2))
            line = Line(p1, p2)
            line.draw(win)

    def __str__(self):
        return str(f"{self.x},{self.y},{self.direction}")

    @staticmethod
    def is_equal(tpick1, tpick2):
        return tpick1.x == tpick2.x and tpick1.y == tpick2.y and tpick1.direction == tpick2.direction

    @staticmethod
    def is_present(tpick, tlist):
        return any(tpick.x == t.x and tpick.y == t.y and tpick.direction == t.direction for t in tlist)
