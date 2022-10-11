layout: post
author: zengjilie
title: "Jilie's Clicky Turtlehack Reflection"
---

## Goal
I want to make an old-school board game. When the player touches a target, this target will disappear, and the player will get 1 point. 
In this program, I want to achieve the basic functionality of this game. When the player reaches the boundary of the board, it will turn to the opposite direction.

## Demo
<iframe src="https://trinket.io/embed/python/8f27440b3c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Setbacks
At first, I just used `player.right(180)` to turn around the player, but when the player goes out of bounds, it's not going back inside the boundary, instead, it will keep rotating in that position. I tried another approach to rotate the player first, then set the x/y coordinate to `179` which is inside the boundary, and it workes.


```python
#boundary checking
while True:
  player.forward(1)
  if player.xcor() >= 180 or player.xcor() <= -180:
    player.right(180)
    
  if player.ycor() >= 180 or player.ycor() <= -180:
    player.speed(100)
```

```python
#boundary checking
while True:
  player.forward(1)
  if player.xcor() >= 180 or player.xcor() <= -180:
    player.speed(100)
    player.right(180)
    if player.xcor() >= 180:
      player.goto(179, player.ycor())
    if player.xcor() <= -180:
      player.goto(-179, player.ycor())
    player.speed(move_amount)
    
  if player.ycor() >= 180 or player.ycor() <= -180:
    player.speed(100)
    player.right(180)
    if player.ycor() >= 180:
      player.goto(player.xcor(), 179)
    if player.ycor() <= -180:
      player.goto(player.xcor(), -179)
```
Another setback is when I want to achieve the a function which the player rotate to the pointed direction, instead goto that position. I tried `player.towards(x,y)`, and it didn't work. So I searched on google and found out I should use setheading instead.

```python
#click function
def clicky(x, y):
  player.goto(x,y)
```

```python
#click function
def clicky(x, y):
  player.setheading(player.towards(x,y))
```

## What I learned from this assignment
It was a fun project. I learned using `while` loop to constantly check the position of the player and the right position to put that `while` loop, yes, I didn't put it in the right place at first, and it prevents the code below it to execute. The process of debugging is painful but also fun. 