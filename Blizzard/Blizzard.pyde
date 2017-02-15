from random import random, randint

class Snowflake():
    """Represents one single snowflake"""
    def __init__(self, x, y_speed, y=0):
        self.x = x
        self.y = 0
        self.x_speed = 0
        self.y_speed = y_speed
        self.y = y
        #self.r = 8 / self.y_speed
        self.r = self.y_speed * 0.65
        
    def change_speed(self):
        """Changes the horizontal speed of the snowflake 
        based on the user's mouse position"""
        self.x_speed = (mouseX - 500) / 80
    
    def move_snowflake(self):
        """Moves the snowflake based on x and y speeds"""
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
    
    def show_snowflake(self):
        """Draws the snowflake on the canvas"""
        ellipse(self.x, self.y, self.r, self.r)
        
        
def create_snowflake():
        snowflake_x = randint(0, width)
        snowflake_y_speed = (random() * 5) + 2
        return Snowflake(snowflake_x, snowflake_y_speed) 
            
        
        
snowflakes = []
w = 1280
h = 800

def setup():
    background(0)
    stroke(255)
    fill(255)
    size(w, h)
    frameRate(30)
    
    for n in range(1300):
        snowflake_x = randint(0, w)
        snowflake_y = randint(0, h + 1)
        snowflake_y_speed = (random() * 5) + 2
        snowflakes.append(Snowflake(snowflake_x, snowflake_y_speed, snowflake_y))


def draw():
    background(0)
    pending_snowflakes = []
    global snowflakes
    
    while snowflakes:
        snowflake = snowflakes.pop()
        
        if snowflake.y > h:
            snowflake = create_snowflake()
        elif snowflake.x < 0 or snowflake.x > w:
            snowflake.x = snowflake.x % w
            
        pending_snowflakes.append(snowflake)
    
    snowflakes = pending_snowflakes[:]
    for snowflake in snowflakes:
        snowflake.show_snowflake()
        snowflake.move_snowflake()
        snowflake.change_speed()
    