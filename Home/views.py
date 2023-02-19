
import shutil
from pathlib import Path
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
# import sys
import sys
from pathlib import Path
sys.path.append('D:\TEXT-SUMMARIZER\texteo_summarizer')
from hackathon.TextSummarizer.text_summarizer_backend import *

def home(request):
    return render(request, 'home.html')


def GenerateSummary(request):

    if request.method == "POST":
        text = request.POST['inputTextArea']
        directory = "./hackathon/TextSummarizer/msft.txt"  # PATH directory
        my_File = open(directory, "w")
        my_File.write(text)
        my_File.close   ()
        
        summarize_text = generate_summary(
            "D:/TEXT-SUMMARIZER/texteo_summarizer/hackathon/TextSummarizer/msft.txt", 7)
    return render(request, 'Text_Summarize.html', {'summarize_text': summarize_text})


def GenerateAudioSummary(request):
    if request.method == "POST":
        file1 = request.POST['audio-file']
        directory = "./hackathon/AudioSummarizer/TestAudio.wav"  # PATH directory

        # filename1 = 'file1.txt'
        # fileA = open(filename1, 'rb')

        # filename2 = 'file5.txt'
        # fileB = open(directory, 'wb')

        # shutil.copyfileobj(file1, fileB)


# generate_summary("AudioSummarizer/msft.txt", 7)
        # summarize_text = main_call()
    return render(request, 'Audio_Summarize.html', {'summarize_text': summarize_text})
