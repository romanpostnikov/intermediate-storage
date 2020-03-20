from app import app, db
from app.models import Video
from flask import request
import os
import googleapiclient.discovery
import json


@app.route('/')
def index():
    return "Required input in format '<URL>/video/<id>'"

# id - is the video id contained in the youtube link
@app.route('/video/<id>')
def videoinfo(id):
    video = Video.query.filter_by(id=id).first()
    if video is None:
        response = youtube_request(id)
        statistics = parse_statistics(response)
        dislikeCount = statistics.get('dislikeCount')
        likeCount = statistics.get('likeCount')

        video = Video(id=id, likes=likeCount, dislikes=dislikeCount)
        db.session.add(video)
        db.session.commit()
    return f"{video}"


def parse_statistics(response):
    items_value = response.get("items") # this one creates value list returned by items key
    statistics_value = items_value[0].get("statistics") # this one returns by 
    # the first item (the only one as well) value by statistics, whic is a dict

    return statistics_value

def youtube_request(id):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCwmkITeKUu3UkehGolUZnT_lHvPShOeYI"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=id
    )

    return request.execute()