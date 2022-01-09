from flask import Flask, request
from player_lists import player1, player2, player3, player4, roundssss, list_scores

def final_results():
  list_scores.append(player1)
  list_scores.append(player2)
  list_scores.append(player3)
  list_scores.append(player4)
  list_scores.sort(reverse=True)
