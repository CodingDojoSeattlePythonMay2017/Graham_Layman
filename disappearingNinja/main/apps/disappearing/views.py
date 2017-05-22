#from __future__ import unicode_literals
from django.shortcuts import render, redirect


def index(request):
    data = { 'pic':""}
    if 'url' in request.session:
        data = {
        'pic':request.session['url']
        }
        print data['pic']
        return render(request, "disappearing/index.html", data)
        """
        Doing it this way you can render the images on the html with either
          <img src="{%static pic %}" alt=""> which pulls from the data dict being passed in the render request
        or you can do it through   <img src="{%static  request.session.url %}" alt="">
        also need the img tag and static which you can see on the html page.
        """
    return render(request, "disappearing/index.html", data)

def display(request, ninja):
    if not ninja:
        request.session['url']="images/ninjaturtles.jpg"
    elif ninja.lower() == 'blue':
        request.session['url']='images/leonardo.jpg'
    elif ninja.lower() == 'purple':
        request.session['url']='images/donatelo.jpg'
    elif ninja.lower() == 'red':
        request.session['url']='images/raphael.jpg'
    elif ninja.lower() == 'yellow':
        request.session['url']='images/michaelangelo.jpg'
    else:
        request.session['url']='images/april.jpg'
    return redirect("/")
