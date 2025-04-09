from django.shortcuts import render, redirect
from .forms import AssignmentForm, WellnessCheckForm, UserRegisterForm
from .models import Assignment, WellnessCheck
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def home(request):
    assignments = Assignment.objects.all()
    return render(request, 'core/home.html', {'assignments': assignments})

@login_required
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssignmentForm()
    return render(request, 'core/add_assignment.html', {'form': form})

@login_required
def wellness_check_in(request):
    if request.method == 'POST':
        form = WellnessCheckForm(request.POST)
        if form.is_valid():
            check = form.save(commit=False)
            check.user = request.user
            check.save()
            return redirect('home')
    else:
        form = WellnessCheckForm()
    return render(request, 'core/check_in.html', {'form': form})

def calendar_view(request):
    return render(request, 'core/calendar.html')

def mood_analytics(request):
    return render(request, 'core/mood_analytics.html')
