from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse




from .forms import MyForm

import json
import requests


# Create your views here.


def home(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']

            

            return redirect(reverse("detail", kwargs={"slug":word}))

    

    else:form = MyForm()
    
    
    return render (request, "dictionary/home.html", {"form":form})
    

def dictionaryView(request,slug):

    word = slug
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = json.loads(response.text)
    if type(data) == list:
    
        data = json.loads(response.text)[0]
        meanings = data.get("meanings")
        
        if  meanings:
            
            phonetics = data.get("phonetics")
            if phonetics:
                audio = phonetics[0].get("audio")
            
            return render(request, "dictionary/detail.html",{"audio":audio
                                                    ,"data":data,
                                                    "meanings":meanings})
    else: 
        title = data["title"]
        message = data["message"]
        resolution = data["resolution"]
        return render( request ,"dictionary/notFound.html", {"title":title,
                                                            "message":message,
                                                            "resolution":resolution})

    
    
    
    
    
    
    
    
    
   

