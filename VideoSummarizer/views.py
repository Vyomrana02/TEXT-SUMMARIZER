from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse


def VideoSummarize(request):
    return render(request, 'Video_Summarize.html')
