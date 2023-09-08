from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.utils import timezone
# Create your views here.

@api_view(['GET'])
def stageone(reqeust, *args, **kwargs):
   
    #extracting value of the query parameters from the url 
    slack_name = reqeust.query_params.get('slack_name')
    track = reqeust.query_params.get('track') 
    current_day = getCurrentDay()
    utc_time = getUtc()
    context ={
        'slack_name': slack_name,
        'track': track,
        'current_day': current_day,
        'utc_time': utc_time,
        'status_code': status.HTTP_200_OK
    }
    return Response(context, status=status.HTTP_200_OK)


"""
this function uses the built in datetime class to get the current day
"""
def getCurrentDay():
    now = datetime.now()

    #the format code %A is used to get the full weekday name from the strftime function
    day = now.strftime('%A')
    return day

"""
this function uses the built in timezone class to get the utc time 
"""
def getUtc():
   return timezone.now() 
