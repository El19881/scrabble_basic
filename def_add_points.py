from flask import Flask, request
from player_lists import player1, player2, player3, player4, roundssss

def add_points():
  pointsp1 = int(request.form.get("points1", 0))
  pointsp2 = int(request.form.get("points2", 0))
  pointsp3 = int(request.form.get("points3", 0))
  pointsp4 = int(request.form.get("points4", 0))
  

  if pointsp1:
    player1[0] += pointsp1
    roundssss.append(1)
  if pointsp2:
    player2[0] += pointsp2
  if pointsp3:
    player3[0] += pointsp3  
  if pointsp4:
    player4[0] += pointsp4