from Particle import Particle


class Sand(Particle):
    def is_move_ok(self, x, y):
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            return False
        if x == self.x and y == self.y + 1 and self.get(x, y) == None:
            return True
        elif x == self.x + 1 and y == self.y + 1 and self.get(x, y) == None and self.get(x, y - 1) == None:
            return True
        elif x == self.x - 1 and y == self.y + 1 and self.get(x, y) == None and self.get(x, y - 1) == None:
            return True
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, self.y + 1):
            return ((self.x, self.y + 1))
        elif self.is_move_ok(self.x - 1, self.y + 1):
            return ((self.x - 1, self.y + 1))
        elif self.is_move_ok(self.x + 1, self.y + 1):
            return ((self.x + 1, self.y + 1))
        else:
            return None


class Rock(Particle):
    def physics(self):
        return None


class Bubble(Particle):
    def is_move_ok(self, x, y):
        if x >= self.width or y >= self.height or x < 0 or y < 0:
            return False
        if x == self.x and y == self.y - 1 and self.get(x, y) == None:
            return True
        elif x == self.x + 1 and y == self.y - 1 and self.get(x, y) == None and self.get(x, y + 1) == None:
            return True
        elif x == self.x - 1 and y == self.y - 1 and self.get(x, y) == None and self.get(x, y + 1) == None:
            return True
        else:
            return False

    def physics(self):
        if self.is_move_ok(self.x, self.y - 1):
            return ((self.x, self.y - 1))
        elif self.is_move_ok(self.x + 1, self.y - 1):
            return ((self.x + 1, self.y - 1))
        elif self.is_move_ok(self.x - 1, self.y - 1):
            return ((self.x - 1, self.y - 1))
        else:
            return None




