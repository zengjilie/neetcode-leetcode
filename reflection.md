---
layout: post
author: Jilie Zeng 
title: Jilie's First Focused Reflection
---

## Goal:
I want to create a series of tutorials teaching people how to use vim editor, which I think is the best editor in the world. So for this part of the tutorial, I want to introduce the basic cursor movements in vim, Up(k), Down(j), Left(h), Right(l).

## Code Demo:

<iframe src="https://trinket.io/embed/python/2f19bb180c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**To Start With**

I need to capture the key press on the screen. My first instinct was to use the function `input()`. However, after gave it a try, I know that wasn't the right solution.

```python
k = input()

while k != "q" :
    if k == "j":
        # move the turtle...
    if ...

    k = input()
```

**Searching Solution**

I googled on **How to move turtle using keypress** and found the solution. https://www.youtube.com/watch?v=WunZOSRM-vA&ab_channel=pyGuru. 

```python
def f():
    t.fd(10)

def b():
    t.bd(10)

def l():
    t.left(10)

def r():
    t.right(10)
```
**Setbacks**

It uses `fd`, `bd`, `right`, `left` to move the turtle. However, 
what I was hoping for is that the turtle will only move Up, Down, Left and Right. Turning directions is not what I was looking for. 

**lightbule Moment**

I vaguely remember a function that can move the turtle to a specific position. So I was thinking if I can get the current position of the turtle and add certain value to the x or y coordinate, this way I can get exactly what I was expecting, completely ignoring the rotation part.

Here is the revised code

```python
def f():
  x, y = t.pos()
  t.setpos(x, y+10)
def b():
  x, y = t.pos()
  t.setpos(x, y-10)
  
def l():
  x, y = t.pos()
  t.setpos(x-10, y)

def r():
  x, y = t.pos()
  t.setpos(x+10, y)
```

Now it's working as I intended, I also added a new function to clean the screen and let the user do more practice.

```python
 def c():
  t.clear()
```

**Next Move**

My next step would be to make several mazes with different levels of difficulty to help the user practice cursor movement and eventually build their muscle memory.