from http.client import HTTPResponse
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # content = {
    #     "Data": "Youtube is best",
    #     "Roll_Number": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #     "first_name": "Yatharth",
    #     "last_name": "Tripathi"
    # }
    # return HttpResponse("Congrats for your first django web page")
    return render(request, "textUtils-2.html")

def spaceremover(request):
    return HttpResponse("spaceremover")

def removepunctuations(request):
    inputtext = request.POST.get('text', 'default')
    removepunctuations = request.POST.get('removepunctuations', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunctuations == "on": 
        punctuations = '''!@$%^&*()_+-={}[];:><,./'''
        analyzed = ""
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed + char
        user_text = {'Task': 'Removed Punctuations', 'analyzed_text': analyzed}
        inputtext = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in inputtext:
            analyzed = analyzed + char.upper()
        
        user_text = {'Task': 'Capitalized', 'analyzed_text': analyzed}
        inputtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(inputtext):
            if (inputtext[index] == " " and inputtext[index+1]==" "):
                pass
            else:
                analyzed = analyzed + char

        user_text = {'Task': 'Space Removed', 'analyzed_text': analyzed}
        inputtext = analyzed
        
    if(removepunctuations != "on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse("You have not selected any function")



    return render(request, 'analyzed.html', user_text)

    # else:
    #         return HttpResponse('Error')
def capitalize(request):
    return HttpResponse("capitalize")

def about(request):
    return HttpResponse("About this page")
def home(request):
    return HttpResponse("This is home page")
