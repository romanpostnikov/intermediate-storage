from app import db
from datetime import datetime

class Video(db.Model):
	id = db.Column(db.String(11), primary_key=True)
	likes = db.Column(db.Integer)
	dislikes = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return f"""Video id = {self.id}, likes = {self.likes}, 
				dislikes = {self.dislikes}, UTC time: {self.timestamp}"""
