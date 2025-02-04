from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Game, Point, Shot


#Home Page
def home(request):
    users = User.objects.all()  # Fetch all users from the database
    return render(request, 'games/home.html', {'users': users})  # Pass 'users' to template

#Add User
def add_user(request):
    games = Game.objects.all()
    if request.method == "POST":
        game_name = request.POST.get['game_name']
        game_id= request.POST.get['game']

    if game_name:
        Game.objects.create(game_name=game_name)
        messages.success(request, "Game added successfully!")
        return redirect('home')
    else:
        messages.error(request, "Game name is required.")

    return render(request, 'user/add_user.html', {'games': games})

#Game Record

def game_records(request):
    game_records = Game.objects.all()
    return render(request, 'games/games.html', {'games_records': game_records})

#Point Record
def points_records(request):
    points_records = Point.objects.all()
    return render(request, 'games/points.html', {'points_records': points_records})

#Shot Record
def shot_records(request):
    shot_records=Shot.objects.all()
    return render(request, 'games/shots.html', {'shot_records': shot_records})

