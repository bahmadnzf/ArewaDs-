from random import randint
class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        self.num_sides=num_sides
    
    def roll(self):
        """Return  a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
   
#Create a Die
die=Die()

#Make some rolls, and store results in a list.
results=[]
for roll_num in range(100):
    result=die.roll()
    results.append(result)

print(results)
