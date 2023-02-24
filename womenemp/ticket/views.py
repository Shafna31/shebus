from django.shortcuts import render
# from ticket.models import Ticket
from django.db import connection, IntegrityError
from django.contrib import messages
from accounts.models import User
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
'''def ticket_book(request,*args):
    if request.method == 'POST':
        context = {}
        women = request.POST['women']
        slot = request.POST['slot']
        date = request.POST['date']
        women_id = User.objects.get(pk=women)
    
    try:
        ticket = Ticket.objects.create(
        women=women_id,
        date = date,
        slot = slot,
        status=False,
        )
    except IntegrityError:
        messages.add_message(request, messages.ERROR, f'Already booked ticket on {date}!')
        return redirect('accounts:index')
        
    context = {'ticket':ticket}
    messages.add_message(request, messages.INFO, f'Booking Successful!')
    return redirect("accounts:home")'''
    



