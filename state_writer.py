from turtle import Turtle
import pandas

class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()

        state_data = pandas.read_csv("50_states.csv")
        state_names = state_data["state"].values
        state_x_coordinates = state_data["x"].values
        state_y_coordinates = state_data["y"].valuesstate_array = []

        self.state_array = []
        for index in range(len(state_names)):
            self.state_array.append([state_names[index], int(state_x_coordinates[index]),
                                     int(state_y_coordinates[index])])

