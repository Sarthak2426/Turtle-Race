import random
import time
from turtle import Screen, Turtle

WIDTH, HEIGHT = 800, 500
MARGIN = 40
START_X = -WIDTH // 2 + MARGIN
FINISH_X = WIDTH // 2 - MARGIN
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_track():
    pen = Turtle(visible=False)
    pen.speed(0)
    pen.penup()
    top = HEIGHT // 2 - 60
    bottom = -HEIGHT // 2 + 60
    step = (top - bottom) // (len(COLORS) - 1)
    ys = [bottom + i * step for i in range(len(COLORS))]
    # finish line
    pen.color("black"); pen.width(2)
    pen.goto(FINISH_X, bottom)
    pen.setheading(90)
    for _ in range(int((top-bottom)/18)):
        pen.pendown(); pen.forward(12); pen.penup(); pen.forward(6)
    return ys

def make_turtles(ys):
    racers = []
    for i, c in enumerate(COLORS):
        t = Turtle("turtle")
        t.penup()
        t.color(c)
        t.goto(START_X, ys[i])
        t.setheading(0)
        racers.append(t)
    return racers

def announce(pen, text, color="black"):
    pen.clear()
    pen.color(color)
    pen.goto(0, HEIGHT // 2 - 35)
    pen.write(text, align="center", font=("Arial", 16, "bold"))

def main():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

    ys = draw_track()
    turtles = make_turtles(ys)

    hud = Turtle(visible=False); hud.penup()

    bet = screen.textinput("Make your bet",
                           f"Which turtle wins? {COLORS} ").strip().lower() if True else None
    if bet not in [c.lower() for c in COLORS]:
        announce(hud, "No valid bet. Race cancelled.", "red")
        screen.exitonclick()
        return

    announce(hud, f"Your bet: {bet.upper()}", bet)
    screen.update()

    # countdown
    for w in ["Ready", "Set", "Go!"]:
        announce(hud, w)
        screen.update()
        time.sleep(0.7)

    winner = None
    while not winner:
        for t in turtles:
            t.forward(random.randint(0, 4))  # slower steps
            if t.xcor() >= FINISH_X:
                winner = t
                break
        screen.update()
        time.sleep(0.02)  # slows down loop

    win_color = winner.pencolor().lower()
    msg = f"You WON! ({win_color.upper()})" if win_color == bet else f"You lost. (Winner: {win_color.upper()})"
    announce(hud, msg, win_color)

    screen.exitonclick()

if __name__ == "__main__":
    main()
