import json
import requests

from videos.models import Video, KeyWord


def get_video_list(key):
    """
    Grabs the latest image from the flick public image feed
    """
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={}&type=video".format(key)
    r = requests.get(url)
    page_content = r.text
    probably_json = page_content.replace("\\'", "'")
    feed = json.loads(probably_json)
    videos = feed['items']
    return videos


def save_videos():
    """
    We get video list and save it in database
    """
    key_list = KeyWord.objects.all()
    for key in key_list:
        video_list = get_video_list(key)
        # lets make sure we don't save the same image more than once
        # we are assuming each Flickr image has a unique Link
        for item in video_list:
            if not Video.objects.filter(link=item['link']).exists():
                video = Video(
                    title=item['snippet']['title'],
                    link="https://www.youtube.com/watch?v={}".format(item['id']['videoId']),
                    key=key,
                    description=item['snippet']['description']
                )
                video.save()
