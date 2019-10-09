
import turtle
wn = turtle.Screen()
Arb = turtle.Turtle()

for i in range(200):
    wn.bgcolor("light blue")
    wn.title("Turtle")
    Arb.pencolor("blue")
    Arb.forward(100+1*i)
    Arb.right(140)
    wn.title("TURTLE")
    Arb.pencolor("orange")
    Arb.forward(100+1*i)
    
wn.bgcolor("orange")  
for i in range(20000000):
    wn.title("Turtle")
    wn.title(i)
   
wn.bgcolor("blue")
