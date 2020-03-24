from app import db
from datetime import datetime
import json
from time import mktime

class Video(db.Model):
	id = db.Column(db.String(11), primary_key=True)
	likes = db.Column(db.Integer)
	dislikes = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		epoch_time = int(mktime(self.timestamp.timetuple()))
		output = f'''
			{{
			<p>&emsp;"video_id": "{self.id}",</p>
			<p>&emsp;"likes": "{self.likes}",</p>
			<p>&emsp;"dislikes": "{self.dislikes}",</p>
			<p>&emsp;"time": "{epoch_time}"</p>
			}}
		'''
		return output
