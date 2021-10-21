from random import choice

class RandomWalk():
    """a class that generates the random walking"""
    def __init__(self, num_points=5000):
        self.num_points = num_points

        #The start point
        self.x_v = [0]
        self.y_v = [0]

    def fill_walk(self):
        while len(self.x_v) < self.num_points:
            # x_direction = choice([1, -1])
            # y_direction = choice([1,-1])
            # x_distance = choice([0,1,2,3,4])
            # y_distance = choice([0,1,2,3,4])
            # x_step = x_direction * x_distance
            # y_step = y_direction * y_distance

            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_v[-1] + x_step
            next_y = self.y_v[-1] + y_step

            self.x_v.append(next_x)
            self.y_v.append(next_y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        return direction * distance
            