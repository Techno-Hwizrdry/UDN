from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.views     import generic

from .models import Participant
from .forms  import ParticipantForm

def all_participants(request):
    return render(request, 'participant_info/all.html', {'participants': Participant.objects.all()})

def index(request):
     return HttpResponseRedirect('/participant_info/add_participant')

def add_participant(request):
    submitted = False

    if request.method == 'POST':
        form = ParticipantForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/participant_info/all')
    else:
        form = ParticipantForm()

        if 'submitted' in request.GET:
           submitted = True

    return render(request, 'participant_info/add_participant.html', {'form': form, 'submitted': submitted})
