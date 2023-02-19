from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse


def TextSummarize(request):
    return render(request, 'Text_Summarize.html')
