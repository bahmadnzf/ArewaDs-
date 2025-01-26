from random import choice  

class RandomWalk:  
    """A Class to generate random walk."""  

    def __init__(self, num_points=5000):  
        """Initialize attributes of a walk."""  
        self.num_points = num_points  

        # All walks start at (0, 0).  
        self.x_values = [0]  
        self.y_values = [0]  

    def fill_walk(self):  
        """Calculate all the points in the walk."""  
        # Keep taking steps until the walk reaches the desired length.  
        while len(self.x_values) < self.num_points:  
            # Decide which direction to go and how far to go in that direction.  
            x_direction = choice([1, -1])  # Use a list here  
            x_distance = choice([0, 1, 2, 3, 4])  
            x_step = x_distance * x_direction  
            
            y_direction = choice([1, -1])  # Use a list here  
            y_distance = choice([0, 1, 2, 3, 4])  
            y_step = y_distance * y_direction  

            # Reject moves that go nowhere  
            if x_step == 0 and y_step == 0:  
                continue  

            # Calculate the next x and y values.  
            next_x = self.x_values[-1] + x_step  
            next_y = self.y_values[-1] + y_step  

            self.x_values.append(next_x)  
            self.y_values.append(next_y)  

# Example Usage  
if __name__ == "__main__":  
    rw = RandomWalk()  
    rw.fill_walk()  
    
    # Output the results  
    print("X Values:", rw.x_values)  
    print("Y Values:", rw.y_values)

