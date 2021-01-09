#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
#list of letters 
letters=["A","B","C","D"]

applelist=[]
appleletters=[]

for i in range(5):
  tempapple=trtl.Turtle()
  applelist.append(tempapple)
  appleletters.append(rand.choice(letters))

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(index):

  global appleletter
  applelist[index].penup()
  applelist[index].shape(apple_image)
  wn.tracer(False)
  applelist[index].color("white")
  applelist[index].sety(rand.randint(-25,100))
  applelist[index].setx(rand.randint(-175,175))
  applelist[index].sety(applelist[index].ycor()-20)
  applelist[index].write(appleletters[index],align="center", font=("Arial", 40, "bold"))
  applelist[index].sety(applelist[index].ycor()+35)
  applelist[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  applelist[index].penup()
  applelist[index].clear()
  applelist[index].sety(-150)
  applelist[index].hideturtle()
  appleletters[index]= rand.choice(letters)
  draw_apple(index)

def typea():
  for i in range(5):
    if appleletters[i]== "A":
      drop_apple(i)

def typeb():
  for i in range(5):
    if appleletters[i]== "B":
      drop_apple(i)

def typec():
  for i in range(5):
    if appleletters[i]== "C":
      drop_apple(i)

def typed():
  for i in range(5):
    if appleletters[i]== "D":
      drop_apple(i)


#-----function calls-----
for i in range(5):
  draw_apple(i)

wn.onkeypress(typea,"a")
wn.onkeypress(typeb,"b")
wn.onkeypress(typec,"c")
wn.onkeypress(typed,"d")

wn.listen()

wn.mainloop()

