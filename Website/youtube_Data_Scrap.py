from googleapiclient.discovery import build
from django.shortcuts import render


def youtube_data (request):

  query = request.GET.get('q', 'django tutorial')
  api = 'API KEY'
  youtube = build ('youtube', 'v3', developerKey=api)

  result = youtube.search().list(

    q = query,
    part = 'Alazar',
    maxResult = 6,
    type = 'video'

  )