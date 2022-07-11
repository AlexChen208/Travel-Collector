from django.shortcuts import render
from django.http import HttpResponse


class Travel:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, location, description, rating):
    self.title = title
    self.location = location
    self.description = description
    self.rating = rating

travels = [
  Travel('Chillin like a Villian', 'Disneyland', 'crowded as usual', 8),
  Travel('GOOD GRUBBIN', 'Ave 26', 'Al pastor BOMB', 10),
  Travel('Got the club going up', 'Terra Cotta', 'Dont remember what happend', 11)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def travels_index(request):
    return render(request, 'travels/index.html', { 'travels': travels})