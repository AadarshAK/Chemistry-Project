import csv
import turtle

atomic_number = int(input("Enter the Atomic Number of the element : "))

electron_configuration_list = []
i = 1

def get_maximum_electrons(energy_level):
    max_electrons = 2*(energy_level**2)
    return max_electrons

while ((sum(electron_configuration_list)) <= (atomic_number)):
    print(i)
    electron_configuration_list.append(get_maximum_electrons(i))
    i += 1

if(sum(electron_configuration_list) > atomic_number):
    to_append = electron_configuration_list[-1]-(sum(electron_configuration_list)-atomic_number)
    electron_configuration_list.pop()
    electron_configuration_list.append(to_append)

if(electron_configuration_list[-1] > 8):
    to_append1 = electron_configuration_list[-1]-8
    electron_configuration_list.pop()
    electron_configuration_list.append(8)
    electron_configuration_list.append(to_append1)

print(electron_configuration_list)

wn = turtle.Screen()
t = turtle.Turtle()
radii = []


def draw_orbits():
    radii_of_shell = 100
    for i in electron_configuration_list:
        turtle.penup()
        turtle.home()
        radii.append(radii_of_shell)
        turtle.goto(0, -radii_of_shell)
        turtle.pendown()
        turtle.circle(radii_of_shell)
        radii_of_shell +=100
 
electron_radius = 20

def draw_electrons(electron_config_list):
    index_reference = 0
    electrons_filled = 0
    turtle.penup()
    turtle.home()
    print(electron_config_list[index_reference])



    while electrons_filled <= electron_config_list[index_reference]:
        turtle.penup()
        turtle.goto(0, radii[index_reference]+electron_radius)
        turtle.pendown()
        turtle.circle(electron_radius)
        turtle.right(90)
        turtle.penup()
        turtle.home()
        electrons_filled += 1

        if electrons_filled == electron_config_list[index_reference]:
            index_reference += 1
            print(f"index_reference : {index_reference}")
            



""" turtle.penup()
    turtle.home()
    turtle.goto(0, -20)
    turtle.pendown()"""

""" radi = i * 50
    turtle.circle(20)
    turtle.penup()
    turtle.goto(0, (radi-20)*2)
    turtle.pendown() """

""" if electrons_filled % 2 == 0:
    turtle.goto(0, (radii[index_reference]) + electron_radius)
    #turtle.right(90)
    turtle.left(360 / electron_config_list[index_reference])    
else:
    turtle.goto(0, (-(radii[index_reference])) - electron_radius)
    #turtle.right(90)
    turtle.right(360 / electron_config_list[index_reference]) """

"""     while electron_config_list[index_reference] <= 2:
        turtle.penup()
        turtle.goto(0, radii[index_reference]+electron_radius)
        turtle.pendown()
        turtle.circle(electron_radius)
        turtle.penup()
        turtle.home() """

draw_orbits()
draw_electrons(electron_configuration_list)

turtle.done()
