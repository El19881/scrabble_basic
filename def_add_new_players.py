from flask import Flask, request
from player_lists import player1, player2, player3, player4

def add_new_players():
  
  player_one = request.form.get("player_input_1")
  if player_one:
    player1[1] = player_one
  player_two = request.form.get("player_input_2")
  if player_two:
    player2[1] = player_two
  player_three = request.form.get("player_input_3")
  if player_three:
    player3[1] = player_three
  player_four = request.form.get("player_input_4")
  if player_four:
    player4[1] = player_four