import turtle
import time

turtle.shape("turtle")
def move_forward():
    if "Up" in keys_pressed:
        turtle.forward(speed)
    screen.ontimer(move_forward, 10)

def turn_left():
    turtle.left(20)

def turn_right():
    turtle.right(20)

def decrease_speed():
    global speed
    speed = max(speed - 1, 1)

def increase_speed():
    global speed
    speed += 1

def key_press(key):
    keys_pressed.add(key)

def key_release(key):
    keys_pressed.remove(key)



screen = turtle.Screen()
turtle.speed(0)
speed = 5
keys_pressed = set()


screen.listen()
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(decrease_speed, "Down")
screen.onkeypress(increase_speed, "space")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")


move_forward()


while True:
    screen.update()
    time.sleep(0.01)


screen.exitonclick()
