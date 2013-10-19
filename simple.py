# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
counter = 0
# Define "helper" functions
def increment():
    global counter
    counter = counter +1 
def buttonpress():
    global counter 
    counter = 0
# Define event handler functions
def tick():
    increment()
    print counter
# Create a frame
frame = simplegui.create_frame("simple test" ,100,100)
frame.add_button("clickme",buttonpress)
# Register event handlers
timer = simplegui.create_timer(1000,tick)
# Start frame and timers
frame.start()
timer.start()

