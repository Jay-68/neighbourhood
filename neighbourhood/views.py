from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)

    except:
        profile = Profile.objects.create(user=user, name=user.username)
        profile.save()
        return redirect('edit_profile', username=user.username)

    posts = Post.objects.filter(neighbourhood=profile.neighbourhood)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)
    neighbourhood = profile.neighbourhood

    return render(request, 'index.html', {"posts": posts, "profile": profile, "businesses": businesses, "neighbourhood": neighbourhood})


@login_required(login_url='/accounts/login')
def business(request):
    profile = Profile.objects.get(user=request.user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request, 'business.html', {"businesses": businesses})


@login_required(login_url='/accounts/login')
def new_business(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = profile
            business.neighbourhood = profile.neighbourhood
            business.save()

        return redirect('business')

    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {'form': form})
