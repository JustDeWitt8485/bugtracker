from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render, reverse

from tracker_app.forms import LoginForm, AddTicket, EditTicket, ActionForm
from tracker_app.models import CustUser, Tickets

# Create your views here.


@login_required(login_url='loginpage')
def index(request):
    user = CustUser.objects.all()
    ticket = Tickets.objects.all()
    new_ticket = Tickets.objects.filter(status="NEW")
    in_pro = Tickets.objects.filter(status="IN_PROGRESS")
    done = Tickets.objects.filter(status="DONE")
    invalid = Tickets.objects.filter(status="INVALID"),

    return render(request, 'index.html', {
        'user': user,
        'ticket': ticket,
        'new': new_ticket,
        'ip': in_pro,
        'done': done,
        'invalid': invalid
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
                return HttpResponseRedirect(request.GET.get('next',
                                                            reverse('homepage')))
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
            ticket = Tickets.objects.create(
                title=data['title'],
                description=data['description'],
            )
            print(ticket.id)
            return HttpResponseRedirect(reverse('homepage'))

    form = AddTicket()
    return render(request, html, {'form': form})


def status_view(request, ticket_id):

    my_ticket = Tickets.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_ticket.user_assigned = data['pick_user']
            my_ticket.status = 'IN_PROGRESS'
            my_ticket.save()
        return HttpResponseRedirect(reverse('homepage'))


def ticket_detail(request, user_filed_id):
    ticket_det = Tickets.objects.get(id=user_filed_id)
    choose_person = ActionForm()
    return render(
        request, 'ticket_detail.html', {
            'ticket_d': ticket_det, 'choose_person': choose_person}
    )


def user_detail(request, user_id):
    user = CustUser.objects.filter(id=user_id).first()
    user_ticket = Tickets.objects.filter(user_filed=user)
    return render(
        request, 'user_detail.html', {
            'user': user, 'user_ticket': user_ticket}
    )


def edit_ticket(request, ticket_id):
    html = 'generic_form.html'
    edit = Tickets.objects.get(id=ticket_id)

    if request.method == 'POST':
        form = EditTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit.title = data['title'],
            edit.description = data['description'],
            edit.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = EditTicket()
    return render(request, html, {'form': form})


def assign_ticket(request, ticket_id):
    ass_ticket = Tickets.objects.filter(id=ticket_id).first()
    if ass_ticket.status == "IN_PROGRESS":
        ass_ticket.user_assigned = request.user
        ass_ticket.user_completed = None
        ass_ticket.save()
    return HttpResponseRedirect(reverse('homepage'))


def completed_ticket(request, ticket_id):
    user = CustUser.objects.get(username=request.user.username)
    ass_ticket = Tickets.objects.filter(id=ticket_id).first()
    if ass_ticket.status == "INVALID" or ass_ticket.user_assigned is None:
        ass_ticket.user_assigned = user
        ass_ticket.user_completed = None
    ass_ticket.status = "DONE"
    ass_ticket.user_completed = ass_ticket.user_assigned
    ass_ticket.user_assigned = None
    ass_ticket.save()
    return HttpResponseRedirect(reverse('homepage'))


def return_ticket(request, ticket_id):
    return_tick = Tickets.objects.filter(id=ticket_id).first()
    return_tick.status = "NEW"
    return_tick.user_assigned = None
    return_tick.user_completed = None
    return_tick.save()
    return HttpResponseRedirect(reverse('homepage'))
