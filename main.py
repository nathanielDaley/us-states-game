import turtle
import pandas

TEXT_ALIGN = "center"
TEXT_FONT = ("Arial", 10, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=493)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_writer = turtle.Turtle()
state_writer.speed("fastest")
state_writer.hideturtle()
state_writer.penup()

state_data = pandas.read_csv("50_states.csv")
state_names = state_data["state"].values
state_x_coordinates = state_data["x"].values
state_y_coordinates = state_data["y"].values

state_dict = {}

for index in range(len(state_names)):
    state_dict[state_names[index]] = (state_x_coordinates[index], state_y_coordinates[index])

guessed_states = []
states_correct = 0
while states_correct < 50:
    state_guess = screen.textinput(title=f"{states_correct}/50 States Correct",
                                   prompt="What's another state's name?").title()

    if state_guess == "Exit":
        missing_states = [state for state in state_names if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if state_guess in state_dict:
        state_writer.goto(state_dict[state_guess][0], state_dict[state_guess][1])
        state_writer.write(state_guess, align=TEXT_ALIGN, font=TEXT_FONT)
        guessed_states.append(state_guess)
        states_correct += 1