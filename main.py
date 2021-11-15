import turtle
import pandas

screen = turtle.Screen()
screen.title("DANI STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50Guess The State",
                                    prompt="Whats another states name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        main = turtle.Turtle()
        main.hideturtle()
        main.penup()
        S = data[data.state == answer_state]
        main.goto(int(S.x), int(S.y))
        main.write(answer_state)


screen.exitonclick()
