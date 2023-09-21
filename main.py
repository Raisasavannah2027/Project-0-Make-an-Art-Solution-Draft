import turtle
import random
# The higher ↓this integer is, the faster the drawing.



# # First Test (Testing the radomiser)
# for i in range(50):
#   x = random.randint(1 ,360)
#   y = random.randint(1 ,80)
#   turtle.forward(y)
#   turtle.right(x)

# # Second Test (Genorating a radom shape)
# x = random.randint(90 ,360)
# y = random.randint(30 ,90)
# z = random.randint(50 ,300)
# for i in range(z):
#   turtle.forward(y)
#   turtle.right(x)
# # p = turtle.pos()
# # if p == (0 ,0):
# #   break

# Second Test (Genorating a radom shape)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(7)
t1.color('Black')
t1.fillcolor('Black')
t1.begin_fill()
t1.hideturtle()

t2 = turtle.Turtle()
t2.shape("turtle")
t2.speed(7)
t2.color('black')
t2.fillcolor('red')
t2.hideturtle()

t3 = turtle.Turtle()
t3.shape("turtle")
t3.speed(7)
t3.color('black')
t3.fillcolor('blue')
t3.hideturtle()

t4 = turtle.Turtle()
t4.shape("turtle")
t4.speed(7)
t4.color('black')
t4.fillcolor('green')
t4.hideturtle()

t5 = turtle.Turtle()
t5.shape("turtle")
t5.speed(7)
t5.color('black')
t5.fillcolor('purple')
t5.hideturtle()

t6 = turtle.Turtle()
t6.shape("turtle")
t6.speed(7)
t6.color('black')
t6.fillcolor('brown')
t6.hideturtle()

t7 = turtle.Turtle()
t7.shape("turtle")
t7.speed(7)
t7.color('black')
t7.fillcolor('yellow')
t7.hideturtle()


# A Star of Daved created by Accident that allways works no matter what number is put in (I finally got the second turtle working)
# org = turtle.position()
# while True:
#   t1.forward(90)
#   t1.right(60)
#   p = t1.position()
#   for i in range(100):
#     t2.setpos(p)
#     t2.forward(90)
#     t2.right(60)
#   p = t1.position()
#   print(p)
#   d = t1.distance((org)) 
#   if d < 0.1:
#     break

num = [1, 2, 3, 4, 5, 6]
state = []
state1 = []
state2 = []
state3 = []
state4 = []
state5 = []
state6 = []
rand_state_list = [state1, state2, state3, state4, state5, state6]
rand_state_list2 = [state1, state2, state3, state4, state5, state6]
rand_state_list3 = [state1, state2, state3, state4, state5, state6]
tlist = [t2, t3, t4, t5, t6, t7]
tlist2 = [t2, t3, t4, t5, t6, t7]
tlist3 = [t2, t3, t4, t5, t6, t7]
tlist4 = [t2, t3, t4, t5, t6, t7]
tlist5 = [t2, t3, t4, t5, t6, t7]
tlist6 = [t2, t3, t4, t5, t6, t7]

org = t1.position()
while True:
  t1.forward(50)
  t1.right(60)
  p = t1.position()
  h = t1.heading()
  state_pair = [p, h]
  state.append(state_pair)
  d = t1.distance((org))
  if d < 0.1:
    t1.end_fill()
    break

while True:
  t = random.choice(tlist)
  s = random.choice(state)
  c = s[0]
  h = s[1]
  t.penup()
  # vertex of original shape
  t.goto(c)
  t.setheading(h)
  t.pendown()
  tlist.remove(t)
  state.remove(s)
  if len(state) == 0:
    break


while True:
  tt = random.choice(tlist2)
  tt.begin_fill()
  tlist2.remove(tt)
  if len(tlist2) == 0:
    break


# while True:
#   if len(tlist3) == 0:
#         break
#   ttt = random.choice(tlist3)
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     # pp = ttt.position()
#     # state.append(pp)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       tlist3.remove(ttt)
#       break

# First Layer
# while True:
#   if len(tlist3) == 0:
#         break
#   rand_list = random.choice(rand_state_list)
#   ttt = random.choice(tlist3)
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     p2 = ttt.position()
#     h2 = ttt.heading()
#     state_pair = [p2, h2]
#     rand_list.append(state_pair)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       rand_state_list.remove(rand_list)
#       tlist3.remove(ttt)
#       break

while True:
  if len(tlist3) == 0:
        break
  rand_list = random.choice(rand_state_list)
  ttt = random.choice(tlist3)
  orgorg = ttt.position()
  while True:
    ttt.forward(50)
    ttt.left(60)
    p2 = ttt.position()
    h2 = ttt.heading()
    state_pair = [p2, h2]
    rand_list.append(state_pair)
    dd = ttt.distance((orgorg))
    if dd < 0.1:
      ttt.end_fill()
      rand_state_list.remove(rand_list)
      tlist3.remove(ttt)
      break

for i in range(len(state1)):
  print(state1[i])

while True:
  rand_list = random.choice(rand_state_list2)
  rand_list.pop(0)
  rand_list.pop(1)
  rand_list.pop(3)
  rand_state_list2.remove(rand_list)
  if len(rand_state_list2) == 4:
    break


while True:
  if len(tlist4) == 0:
        break
  while True:
    tr = random.choice(tlist4)
    s = random.choice(state1)
    c = s[0]
    h = s[1]
    tr.penup()
    tr.goto(c)
    tr.setheading(h)
    tr.pendown()
    tlist4.remove(tr) 
    state1.remove(s)
    if len(state1) == 0:
      break

while True:
  tt = random.choice(tlist5)
  tt.begin_fill()
  tlist5.remove(tt)
  if len(tlist5) == 0:
    break

while True:
  if len(tlist6) == 0:
        break
  ttt = random.choice(tlist6)
  orgorg = ttt.position()
  while True:
    ttt.forward(50)
    ttt.left(60)
    dd = ttt.distance((orgorg))
    if dd < 0.1:
      ttt.end_fill()
      tlist6.remove(ttt)
      break