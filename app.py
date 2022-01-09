#create a new py file with routes and a file for just the flask app and then import it to the route files

from flask import Flask, render_template, request
from player_lists import player1, player2, player3, player4, roundssss, list_scores
from def_add_new_players import add_new_players
from def_add_points import add_points
from def_final_results import final_results

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
  ''' Landing page. Players submit their names '''
  return render_template("add_players.html", title = "Add players")


@app.route("/points", methods = ["GET", "POST"])
def points():
  ''' List of players, their points and forms to add new points and end the game '''
  add_new_players()
  add_points()
  
  return render_template("points.html", title = "Players and points", player1=player1, player2=player2, player3=player3, player4=player4)


@app.route("/end_game", methods = ["POST", "GET"])
def end_game():
  ''' Final page of the app, shows the results of the game '''
  final_results()
  rounds = len(roundssss)

  return render_template ("end_game.html", title = "Final results", player1=player1, player2=player2, player3=player3, player4=player4, list_scores=list_scores, rounds = rounds)


app.run(debug=True)




