# Created by Mohammed Al Mubarak
# Created on 06/01/2019
# version 1

import turtle
turtle.setup(500, 600)
turtle.penup()
turtle.hideturtle()

# Create name for the star coordinates.

BetegeuseX = -70 
BetegeuseY = 200

MeissaX = 80
MeissaY = 180

AlnitakX = -40
AlnitakY = -20

AlnilamX = 0
AlnilamY = 0

MintakaX = 40
MintakaY = 20

SaiphX = -90
SaiphY = -180

RigelX = 120
RigelY = -140

# Draw the stars
turtle.goto(BetegeuseX, BetegeuseY)
turtle.dot()
turtle.goto(MeissaX, MeissaY)
turtle.dot()
turtle.goto(AlnitakX, AlnitakY)
turtle.dot()
turtle.goto(AlnilamX, AlnilamY)
turtle.dot()
turtle.goto(MintakaX, MintakaY)
turtle.dot()
turtle.goto(SaiphX, SaiphY)
turtle.dot()
turtle.goto(RigelX, RigelY)
turtle.dot()

# Write the names of the stars
turtle.goto(BetegeuseX, BetegeuseY)
turtle.write('Betegeuse')
turtle.goto(MeissaX, MeissaY)
turtle.write('Meissa')
turtle.goto(AlnitakX, AlnitakY)
turtle.write('Alnitak')
turtle.goto(AlnilamX, AlnilamY)
turtle.write('Alnilam')
turtle.goto(MintakaX, MintakaY)
turtle.write('Mintaka')
turtle.goto(SaiphX, SaiphY)
turtle.write('Saiph')
turtle.goto(RigelX, RigelY)
turtle.write('Rigel')

# Draw a line from the Betegeue to Alnitak
turtle.goto(BetegeuseX, BetegeuseY)
turtle.pendown()
turtle.goto(AlnitakX, AlnitakY)
turtle.penup()

# Draw a line from Meissa to Mintaka
turtle.goto(MeissaX, MeissaY)
turtle.pendown()
turtle.goto(MintakaX, MintakaY)
turtle.penup()

# Draw a line from Alnitak to Alnilam
turtle.goto(AlnitakX, AlnitakY)
turtle.pendown()
turtle.goto(AlnilamX, AlnilamY)
turtle.penup()

# Draw a line from Alnilam to Mintaka
turtle.goto(AlnilamX, AlnilamY)
turtle.pendown()
turtle.goto(MintakaX, MintakaY)
turtle.penup()

# Draw a line from Alnitak to Saiph
turtle.goto(AlnitakX, AlnitakY)
turtle.pendown()
turtle.goto(SaiphX, SaiphY)
turtle.penup()

# Draw a line from Mintaka to Rigel
turtle.goto(MintakaX, MintakaY)
turtle.pendown()
turtle.goto(RigelX, RigelY)
turtle.penup()

# Keep the window open
turtle.done()