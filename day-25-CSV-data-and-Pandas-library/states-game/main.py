import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=730, height=500)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
states_correct = []
while len(states_correct) < 50:
    answer_state = screen.textinput(title=f"{len(states_correct)}/50 States Correct",
                                    prompt="What's another state name?")

    if answer_state.title() == "Exit":
        missing_states = [state for state in states if state not in states_correct]
        # for state in states:
        #     if state not in states_correct:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    if answer_state.title() not in states_correct:
        if answer_state.title() in states:
            x = int(data.x[data.state == answer_state.title()])
            y = int(data.y[data.state == answer_state.title()])

            new_turtle.goto(x, y)
            new_turtle.write(answer_state.title(), False, "center", ("Arial", 7, "bold"))
            states_correct.append(answer_state.title())

screen.exitonclick()
