from django.shortcuts import render
from blog.models import Post
from property.models import Property, Place, Category
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.db.models.query_utils import Q
from django.db.models import Count

# Create your views here.
def home(request):
    places = Place.objects.all().annotate(property_count= Count('property_place'))
    category = Category.objects.all()
    
    resturant_list = Property.objects.filter(category__name = 'Restaurant')[:5]
    hotels_list = Property.objects.filter(category__name = 'Hotel')[:4]
    places_list = Property.objects.filter(category__name = 'Places')[:4]
    
    recent_posts = Post.objects.all()[:4]
    
    users_count =User.objects.all().count()
    places_count = Property.objects.filter(category__name = 'Places').count
    restaurant_counts =Property.objects.filter(category__name = 'Restaurant').count()
    hotels_count=Property.objects.filter(category__name = 'Hotel').count()
    
    return render(request, 'settings/home.html', {'places': places,
                   'category': category,
                   'resturant_list':resturant_list,
                   'hotels_list':hotels_list,
                   'places_list':places_list,
                   'recent_posts':recent_posts,
                   'users_count':users_count,
                   'places_count':places_count,
                   'restaurant_counts':restaurant_counts,
                   'hotels_count':hotels_count,
                   
                   })

def home_search(request):
        name = request.GET.get('name')
        place = request.GET.get('place')
        
        property_list = Property.objects.filter(
            Q(name__icontains=name)&
            Q(place__name__icontains=place)
        )
        return render(request, 'settings/home_search.html', {'property_list': property_list})


def category_filter(request,category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request, 'settings/home_search.html', {'property_list': property_list,'category':category})


def place_filter(request,place):
    place = Place.objects.get(name = place)
    category =  Place.objects.get(name = place)
    property_list = Property.objects.filter(place=place)
    
    return render(request, 'settings/home_search.html', {'property_list': property_list,'category':category})



def contact_us(request):
    return render(request, 'settings/contact_us.html')






