from django.shortcuts import render
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Travel
from .forms import ReviewsForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def travels_index(request):
    travels = Travel.objects.all()
    return render(request, 'travels/index.html', { 'travels': travels })

def travels_detail(request, travel_id):
    travel = Travel.objects.get(id=travel_id)
    review_form = ReviewsForm()
    return render(request, 'travels/detail.html', {
        'travel': travel, 'review_form': review_form
    })

# class TravelList(ListView):
#     model = Travel
#     template_name = 'travels/index.html'

class TravelCreate(CreateView):
    model = Travel
    fields = '__all__'
    success_url = '/travels/'

class TravelUpdate(UpdateView):
    model = Travel
    fields = '__all__'

class TravelDelete(DeleteView):
    model = Travel
    success_url = '/travels/'