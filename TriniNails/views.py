from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import CartItem

# Create your views here.
def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else: 
        form = UserRegistrationForm()
        
    conext = {"form": form}
    return render(request, "TriniNails/register.html", context)

@login_required
def home(request):
    todos = CartItem.objects.filter(user-request.user, is_completed=false).order_by("-Product")
    
    context = ("todos": todos)
    return render(request, "Trininails/crud.html", context)
    