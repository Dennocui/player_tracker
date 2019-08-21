from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse , HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from django.views import generic
from django.http import  HttpResponse

from django.urls import reverse


from .models import Player, Medical
from .forms import MedicalReport

@login_required
def home(request):
    return render(request, 'medical/home.html')

@login_required
def players(request):
    players = Player.Player.objects.select_related().order_by('first_name')
    context = {'players' : players }

    return render(request, 'medical/players.html', context)

@login_required
def injured(request):
    players = Medical.objects.all().order_by('recovery_date')
    context = {'players' : players }
  
    return render(request, 'medical/injured_players.html', context)

@login_required
def NewMedicalReport(request):
    if request.method == 'POST':
        #print(request.POST)
        form = MedicalReport(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            messages.success(request, ' Report Sucessfully Entered')
            return HttpResponseRedirect(reverse('medical:injured'))
    else:
        messages.error(request, 'Report Not Successfuly Entered')
        form = MedicalReport()
        

    return render(request, 'medical/form.html', {'form' : form})


@login_required
def PlayerDetails(request, id):
    report = Medical.objects.select_related().filter(player_id=id).order_by('created_at')
    context = {'report' : report}

    return render(request, 'medical/report.html', context)

@login_required
def EditReport(request, id):
    report = Medical.objects.get(id=id)
    form = MedicalReport(request.POST or None, instance=report)
    context = {'report' : report, 'form' : form}

    if form.is_valid():
        form.save()
        return redirect('medical:players')

    return render(request, 'medical/form.html', context)

def get_data(request):
    data = {
        "sales" : 100,
        "customers": 10,
    }
    return JsonResponse(data)