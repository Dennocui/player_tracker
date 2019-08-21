from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views import generic
from django.urls import reverse
from django.contrib import messages

from .models import  Player, Condition
from .forms import ConditioningReport




@login_required
def home(request):
    return render(request, 'conditioning/home.html')

#@login_required
class PlayersView(generic.ListView):
    template_name = 'conditioning/players.html'
    context_object_name = 'player_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.Player.objects.order_by('first_name')

@login_required
def players(request):
	player_list = Player.Player.objects.order_by('first_name')
	context = {'player_list' : player_list}

	return render(request, 'conditioning/players.html', context)

@login_required
def NewReport(request):
    if request.method == 'POST':
        #print(request.POST)
        form = ConditioningReport(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            messages.success(request, ' Report Sucessfully Entered')
            return HttpResponseRedirect(reverse('conditioning:players'))
    else:
        messages.error(request, 'Report Not Successfuly Entered')
        form = ConditioningReport()
        

    return render(request, 'conditioning/form.html', {'form' : form})

@login_required
def EditReport(request, id):
    report = Condition.objects.get(id=id)
    form = ConditioningReport(request.POST or None, instance=report)
    context = {'report' : report, 'form' : form}

    if form.is_valid():
        form.save()
        return redirect('medical:players')

    return render(request, 'conditioning/form.html', context)



@login_required
def PlayerDetails(request, id):
    report = Condition.objects.select_related().filter(player_id=id).order_by('created_at')
    context = {'report' : report}

    return render(request, 'conditioning/report.html', context)


@login_required
def reharb(request):
    #players = Medical.objects.all()
    context = {'players' : players }

    return render(request, 'conditioning/reharb.html', context)

