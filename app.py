from flask import Flask, render_template, request
from dictionaries import players

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
  ''' Landing page. Players submit their names '''

  return render_template("add_players.html", title = "Dodaj graczy")

@app.route("/points", methods = ["GET", "POST"])
def points():
  ''' List of players, their points and forms to add new points and end the game '''

  player_one = request.form["player_input_1"]
  if player_one:
    players[player_one] = 0
  player_two = request.form["player_input_2"]
  if player_two:
    players[player_two] = 0
  player_three = request.form["player_input_3"]
  if player_three:
    players[player_three] = 0
  player_four = request.form["player_input_4"]
  if player_four:
    players[player_four] = 0
  return render_template("points.html", title = "Gracze i punkty", player_dict = players, player_one = player_one, player_two = player_two, player_three = player_three, player_four = player_four)

app.run(debug=True)




