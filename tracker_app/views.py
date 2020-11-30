from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render, reverse

from tracker_app.forms import LoginForm, AddTicket
from tracker_app.models import CustUser, Tickets

# Create your views here.


@login_required(login_url='loginpage')
def index(request):
    return render(request, 'index.html', {
        'user': CustUser.objects.all(),
        'tickets': Tickets.objects.all(),
        }
    )


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('loginpage')))


def create_ticket(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tickets.objects.create(
                title=data['title'],
                status=data['status'],
                user_assigned=data['user_assign'],
                user_filed=data['user_filed'],
                user_complete=data['user_complete'],


            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddTicket()
    return render(request, html, {'form': form})


def ticket_detail(request, user_filed_id):
    ticket_det = Tickets.objects.get(id=user_filed_id)
    return render(
        request, 'ticket_detail.html', {'ticket_d': ticket_det}
    )



