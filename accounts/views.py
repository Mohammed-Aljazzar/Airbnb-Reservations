from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile
from .forms import UserForm , ProfileForm , UserCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from property.models import Property, PropertyBook, PropertyReview
from property.forms import PropertyReviewForm
from django.contrib.auth import logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })



def myreservation(request):
    pass
    property_list = PropertyBook.objects.filter(user=request.user)
    return render(request,'profile/reservation.html' , {'property_list':property_list})


def add_feedback(request , slug):
    property = get_object_or_404(Property , slug=slug)

    try:
        user_feedback = get_object_or_404(PropertyReview , property=property , author=request.user)
        if request.method == 'POST':
            form = PropertyReviewForm(request.POST , instance=user_feedback)
            if form.is_valid():
                form.save()
                
                return redirect('settings:home')

        else:
            form = PropertyReviewForm(instance=user_feedback)
        return render(request,'profile/property_feedback.html' , {'form':form , 'property':property})


    except:
        if request.method == 'POST':
            form = PropertyReviewForm(request.POST)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.property = property
                myform.author = request.user
                myform.save()

        else:
            form = PropertyReviewForm()
        return render(request,'profile/property_feedback.html' , {'form':form , 'property':property})




def mylisting(request):
    
    property_list = Property.objects.filter(owner=request.user)
    return render(request,'profile/my_listing.html' , {'property_list':property_list})

'''
        if request.method == 'POST':
            form = PropertyReviewForm(request.POST , instance=user_feedback)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.property = property
                myform.author = request.user
                myform.save()

        else:
            form = PropertyReviewForm(instance=user_feedback)
        return render(request,'profile/property_feedback.html' , {'form':form , 'property':property})

        '''
        
def custom_logout(request):
    logout(request)
    return redirect('settings:home')