"""
Author: Gabi Costa
Assignment / Part: HW4 - Q4
Date due: 2023-03-02, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
import turtle
Zellij = turtle.Turtle()

value = int(input('Enter the number of polygons you would like to be displayed: '))
for i in range(0, 20):
    for j in range(0, value):
        Zellij.forward(100)
        Zellij.left(360/value)
    Zellij.left(360/20)
turtle.done()