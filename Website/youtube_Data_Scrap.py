from googleapiclient.discovery import build
from django.shortcuts import render

def youtube_search(request):
    query = request.GET.get('q', 'django tutorial')
    api_key = 'AIzaSyAfnebY_AdgczXg8Dmd8We5mZCVaWqYoJo'
    youtube = build('youtube', 'v3', developerKey=api_key)

    request_data = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=5,
        type='video'
    )

    response = request_data.execute()

    videos = []
    for item in response['items']:
        video_data = {
            'title': item['snippet']['title'],
            'video_id': item['id']['videoId'],
            'thumbnail': item['snippet']['thumbnails']['high']['url'],
        }
        videos.append(video_data)

    return render(request, 'youtube_results.html', {'videos': videos})
