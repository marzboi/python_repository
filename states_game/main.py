import turtle
import pandas
IMAGE_PATH = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(IMAGE_PATH)
turtle.shape(IMAGE_PATH)

us_data = pandas.read_csv("50_states.csv")


def add_state(name, x, y):
    state_draw = turtle.Turtle()
    state_draw.hideturtle()
    state_draw.penup()
    state_draw.goto(x, y)
    state_draw.write(f'{name}')


game_is_on = True
already_guess = []

while len(already_guess) < 50:

    user_input = screen.textinput(f"{len(already_guess)}/50 States Correct", "What's another state's name").title()

    if user_input == "Exit":
        break

    user_answer = us_data[us_data.state == user_input]

    if not user_answer.empty and user_input not in already_guess:
        state_name = user_answer.state.item()
        state_x = user_answer.x.item()
        state_y = user_answer.y.item()
        add_state(state_name, state_x, state_y)
        already_guess.append(user_input)
