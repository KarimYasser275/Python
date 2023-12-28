import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

data_dict = data.to_dict()

screen = turtle.Screen()
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")
screen.tracer(0)
text = turtle.Turtle()
text.hideturtle()
text.penup()


def get_coordinates(x, y):
    print(x, y)


def write_state(input_state):
    x = data[data.state == input_state].x.item()
    y = data[data.state == input_state].y.item()
    print(input_state, data[data.state == input_state].x.item(), data[data.state == input_state].y.item())
    text.goto(x, y)
    text.write(input_state)
    screen.update()


def generate_csv():
    # missing_states = []
    # for state in states:
    #     if state not in guessed_states:
    #         missing_states.append(state)
    missing_states = [state for state in states if state not in guessed_states]
    missing_states_csv = pandas.DataFrame(missing_states)
    missing_states_csv.to_csv("Missing_States.csv")
    print(missing_states_csv)


screen.onscreenclick(fun=get_coordinates)

game_is_on = True
guessed_states = []
while len(guessed_states) < 50:
    user_input = (screen.textinput(prompt=f"{len(guessed_states)}/50", title="enter a state")).title()
    if user_input == "Exit":
        generate_csv()
        break
    if user_input in states:
        write_state(user_input)
        guessed_states.append(user_input)

    elif user_input in guessed_states:
        print("Already guessed!")
    else:
        print("Wrong Guess!")

screen.mainloop()
