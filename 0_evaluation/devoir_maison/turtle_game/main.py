import turtle
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SALAD_SIZE = 20
MOVE_AMPLITUDE = 20
COLLISION_DISTANCE = 20
SALAD_COLORS = ["red", "blue", "yellow", "purple", "orange"]


# Configuration de l'écran
def setup_screen():
    screen = turtle.Screen()
    screen.title("Jeu de Tortue")
    screen.bgcolor("white")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    return screen


# Création de la tortue
def create_player():
    player = turtle.Turtle()
    player.shape("turtle")
    player.color("green")
    player.speed(0)
    player.penup()
    return player


# Création de la salade
def create_salad():
    salad = turtle.Turtle()
    salad.shape("circle")
    salad.color(random.choice(SALAD_COLORS))
    salad.penup()
    salad.speed(0)
    salad.shapesize(0.5, 0.5)  # Réduire la taille de la salade
    salad.goto(
        random.randint(-SCREEN_WIDTH // 2 + SALAD_SIZE, SCREEN_WIDTH // 2 - SALAD_SIZE),
        random.randint(
            -SCREEN_HEIGHT // 2 + SALAD_SIZE, SCREEN_HEIGHT // 2 - SALAD_SIZE
        ),
    )
    return salad


# Création du compteur de score
def create_score_display():
    score_display = turtle.Turtle()
    score_display.hideturtle()
    score_display.penup()
    score_display.goto(-SCREEN_WIDTH // 2 + 10, SCREEN_HEIGHT // 2 - 30)
    score_display.write(
        f"Score: {salad_count}", align="left", font=("Arial", 16, "normal")
    )
    return score_display


# Mettre à jour le compteur de score
def update_score():
    score_display.clear()
    score_display.write(
        f"Score: {salad_count}", align="left", font=("Arial", 16, "normal")
    )


# Fonctions pour déplacer la tortue
def move_up():
    player.setheading(90)
    player.forward(MOVE_AMPLITUDE)
    check_collision()


def move_down():
    player.setheading(270)
    player.forward(MOVE_AMPLITUDE)
    check_collision()


def move_left():
    player.setheading(180)
    player.forward(MOVE_AMPLITUDE)
    check_collision()


def move_right():
    player.setheading(0)
    player.forward(MOVE_AMPLITUDE)
    check_collision()


# Vérifier si la tortue mange la salade
def check_collision():
    global salad_count
    if (
        player.distance(salad) < COLLISION_DISTANCE
    ):  # Distance pour considérer que la salade est mangée
        salad.goto(
            random.randint(
                -SCREEN_WIDTH // 2 + SALAD_SIZE, SCREEN_WIDTH // 2 - SALAD_SIZE
            ),
            random.randint(
                -SCREEN_HEIGHT // 2 + SALAD_SIZE, SCREEN_HEIGHT // 2 - SALAD_SIZE
            ),
        )
        salad_count += 1
        update_score()
        print(f"Salade mangée ! Total: {salad_count}")


# Configuration des touches
def setup_controls():
    screen.listen()
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")


# Initialisation
screen = setup_screen()
player = create_player()
salad = create_salad()
salad_count = 0
score_display = create_score_display()

setup_controls()

# Boucle principale du jeu
print("Utilisez les touches fléchées pour déplacer la tortue et manger la salade !")
try:
    screen.mainloop()
except KeyboardInterrupt:
    print("Jeu terminé.")
except turtle.Terminator:
    print("Jeu terminé.")
finally:
    print("Merci d'avoir joué !")
