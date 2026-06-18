import turtle
import pandas

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)
screen.update()
t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f'{len(guessed_states)}/50 States Correct', 'What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        # states_to_learn = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        states_to_learn = [state for state in all_states if state not in guessed_states]

        pandas.DataFrame(states_to_learn).to_csv('states_to_learn.csv')

        t.color('red')
        for state in states_to_learn:
            state_data = data[data.state == state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(state_data.state.item(), font=('Arial', 10, 'bold'))
        screen.update()
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item(), font=('Arial', 10, 'bold'))
        screen.update()

screen.exitonclick()