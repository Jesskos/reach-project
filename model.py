from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	''' A model of users and their scores '''

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	username = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		""" Provide helpful representation of user object when printed"""

		return "<User user_id={}  username={} password={}>".format(self.user_id, 
			self.username, self.password) # pragma: no cover

class Score(db.Model):
	''' keeps track of the score from each game'''
	
	__tablename__ = "scores"

	score_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
	date = db.Column(db.DateTime, nullable=False)
	word = db.Column(db.String(20), nullable=False)
	game_information = db.Column(db.String(400), nullable=False)
	score = db.Column(db.Integer, nullable=False)
	won = db.Column(db.Boolean, nullable=False)
	completed = db.Column(db.Boolean, nullable=False)

	user = db.relationship("User", backref="Score")

	def __repr__(self):
		""" Provide helpful representation of score object when printed"""

		return "<Score score_id={} user_id = {} date={} word={} score={} won={} game_information ={}>".format(self.score_id, 
			self.user_id, self.date, self.word, self.score, self.won, self.game_information) # pragma: no cover


def connect_to_db(app, uri='postgresql:///scoresdb'): # pragma: no cover
	""" Connect the database to our Flask App"""

	# Configure to use our PstgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = uri  
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # pragma: no cover
	app.config['SQLALCHEMY_ECHO'] = True
	db.init_app(app)
	db.app=app
	db.create_all()


if __name__ == "__main__": # pragma: no cover
	from server import app # pragma: no cover

	#from server import app  # pragma: no cover
	connect_to_db(app)  # pragma: no cover
	print("Connected to DB.")  # pragma: no cover
