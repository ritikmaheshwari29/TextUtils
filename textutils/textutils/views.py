# I have created this file -- RITIK
from django.http import HttpResponse
from django.shortcuts import render

"""
# Code for video 6
def index(request):
    return HttpResponse('''<h1>Hello Everyone! This is my first website</h1> <a href="https://www.linkedin.com/in/ritik-maheshwari-065017166/"> Click on My Profile </a>>''')

def about(request):
    return HttpResponse("Hope you will like it...")
"""
def index(request):
    return render(request,'index.html' )
    #return HttpResponse('''<h1>Home</h1> <a href="http://127.0.0.1:8000/removepunc">Remove Punc  </a>''')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')

    # Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Chech which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>.@~`#$%^&**+='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+ char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps != "on" and newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("Error Not Found! PLEASE SELECT THE OPERATION")

    return render(request, 'analyze.html', params)

"""
def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("New line remover")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")


def charcount(request):
    return HttpResponse("char count")
"""



