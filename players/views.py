from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Player, Club, Role, High_school, Position
from .forms import NewPlayer, NewClub, NewSchool
import json
from medical.models import Medical
from conditioning.models import Condition

from django.urls import reverse
from django.contrib import messages
from django.db.models import Count, Q


@login_required
def home(request):

    total_players = Player.objects.count()
    injuries = Medical.objects.count()
    club_count = Club.objects.count()
    schools = High_school.objects.count()

    
    dataset = Position.objects.values('name').annotate(player_count=Count('player')).order_by('id')
    # .order_by('position')


    positions = list()
    player_series_data = list()
    

    for entry in dataset:
        positions.append(entry['name'])
        player_series_data.append(entry['player_count'])



    club_dataset = Club.objects.values('name').annotate(player_count=Count('player')).order_by('id')
    # .order_by('position')


    clubs = list()
    player_data = list()
    

    for entry in club_dataset:
        clubs.append(entry['name'])
        player_data.append(entry['player_count'])

        

    return render(request, 'players/home.html', {
        'positions': json.dumps(positions),
        'player_series_data': json.dumps(player_series_data),
        'clubs': json.dumps(clubs),
        'player_data': json.dumps(player_data),
        'total_players': total_players,
        'injuries': injuries,
        'club_count': club_count,
        'schools': schools ,
        
    })

     





@login_required
def players(request):
    """
    Renders current_players.html template which lists all the currently available players
    """
    
    players = Player.objects.select_related().order_by('first_name')
    context = {'players' : players}
    return render(request, 'players/current_players.html', context)

@login_required
def past_players(request):
    """
    Renders current_players.html template which lists all the currently available players
    """
    players = Player.objects.select_related().filter()
    context = {'players' : players}
    return render(request, 'players/past_players.html', context)

#@login_required
class DetailView(generic.DetailView):
    model = Player
    template_name = 'players/details.html'


@login_required
def new_player(request):
    club = Club.objects.all()
    role = Role.objects.all()
    position = Position.objects.all()
    high_school = High_school.objects.all()


    if request.method == 'POST':
        #print(request.POST)
        form = NewPlayer(request.POST,request.FILES)
        if form.is_valid():
            #print(form)
            form.save()
            messages.success(request, 'High School Sucessfully Entered')
            return HttpResponseRedirect(reverse('players:settings'))
    else:
        #messages.error(request, 'Club Not Successfuly Entered')
        form = NewPlayer()
        
    context = {'form' : form, 'club' : club , 'role' : role , 'position' : position  , 'high_school': high_school }

    return render(request, 'players/player_form.html', {'context' : context})


@login_required
def edit_player(request, id):
    player = Player.objects.get(id=id)
    form = NewPlayer(request.POST or None, request.FILES or None, instance=player)

    if form.is_valid():
        form.save()
        return redirect('players:players')

    return render(request, 'players/player_form.html', {'form': form, 'player': player})

@login_required
def delete(request, id):
    player = Player.objects.get(id=id)

    #if request.method == 'POST':
    player.delete()
        #return redirect('players:players')

    return redirect('players:players')
@login_required
def Settings(request):
    clubs = Club.objects.all().order_by('id')
    schools = High_school.objects.all().order_by('name')

    context = {'clubs': clubs, 'schools': schools}

    return render(request, 'players/settings.html', context)


@login_required
def new_club(request):
    if request.method == 'POST':
        #print(request.POST)
        form = NewClub(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            messages.success(request, 'Club Sucessfully Entered')
            return HttpResponseRedirect(reverse('players:settings'))
    else:
        messages.error(request, 'Club Not Successfuly Entered')
        form = NewClub()
        

    return render(request, 'players/form.html', {'form' : form})

def edit_club(request, id):
    club = Club.objects.get(id=id)
    form = NewClub(request.POST or None, instance=club)
    context = {'club' : club, 'form' : form}

    if form.is_valid():
        form.save()
        return redirect('players:settings')

    return render(request, 'players/form.html', context)


@login_required
def new_school(request):
    if request.method == 'POST':
        #print(request.POST)
        form = NewSchool(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            messages.success(request, 'High School Sucessfully Entered')
            return HttpResponseRedirect(reverse('players:settings'))
    else:
        #messages.error(request, 'Club Not Successfuly Entered')
        form = NewSchool()
        

    return render(request, 'players/form.html', {'form' : form})

def edit_school(request, id):
    school = High_school.objects.get(id=id)
    form = NewSchool(request.POST or None, instance=school)
    context = {'school' : school, 'form' : form}

    if form.is_valid():
        form.save()
        return redirect('players:settings')

    return render(request, 'players/form.html', context)
