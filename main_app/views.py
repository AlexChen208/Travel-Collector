from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from . models import Travel, Tag
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
    id_list = travel.tags.all().values_list('id')
    travel_tags_doesnt_have = Tag.objects.exclude(id__in=id_list)
    review_form = ReviewsForm()
    return render(request, 'travels/detail.html', {
        'travel': travel, 'review_form': review_form,
        'tags': travel_tags_doesnt_have
    })

def add_review(request, travel_id):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.travel_id = travel_id
        new_review.save()
    return redirect('detail', travel_id=travel_id)

def tags_index(request):
    tags = Tag.objects.all()
    return render(request, 'tags/index.html', { 'tags': tags })

def tags_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'tags/detail.html', { 'tag': tag })

# class TravelList(ListView):
#     model = Travel

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

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'
    success_url = '/tags/'

class TagUpdate(UpdateView):
    model = Tag
    fields = '__all__'

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'