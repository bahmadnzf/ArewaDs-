from random import choice
class RandomWalk2:  
    """A Class to generate random walk."""  

    def __init__(self, num_points=5000):  
        """Initialize attributes of a walk."""  
        self.num_points = num_points  

        # All walks start at (0, 0) 
        self.x_values = [0]  
        self.y_values = [0]  
    def get_step(self):  
        """Calculate all the points in the walk."""  
        # Keep taking steps until the walk reaches the desired length.  
        direction =choice([1,-1])
        distance=choice([0, 1, 2, 3,4,9,16,25,30,34,36,40,45,47,51,60,67,72,76,80,81]) 
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:  
            x_step  = self.get_step()
            y_step=self.get_step()
           
            # Reject moves that go nowhere  
            if x_step == 0 and y_step == 0:  
                continue  

            # Calculate the next x and y values.  
            next_x = self.x_values[-1] + x_step  
            next_y = self.y_values[-1] + y_step  

            self.x_values.append(next_x)  
            self.y_values.append(next_y)  