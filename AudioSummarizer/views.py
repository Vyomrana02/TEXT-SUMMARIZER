from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse


def AudioSummarize(request):
    return render(request, 'Audio_Summarize.html')
