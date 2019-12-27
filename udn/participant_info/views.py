from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseRedirect
from django.views     import generic

from .models import Participant
from .forms  import ParticipantForm

def index(request):
     return HttpResponseRedirect('/participant_info/add_participant')

# This view will return a list of all the participants
# that have been entereed in the UDN database.
def all_participants(request):
    return render(request, 'participant_info/all.html', {'participants': Participant.objects.all()})

# This view is the form where a participant's information is entered.
def add_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)

        #  If the form is valid (no duplicate name or incorrect data)
        #  then save the data and redirect the user to participant list page.
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/participant_info/all')
    else:
        form = ParticipantForm()

    return render(request, 'participant_info/add_participant.html', {'form': form})
