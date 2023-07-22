from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
# Create your views here.


def members(request):
    template = loader.get_template('members.html')
    return HttpResponse(template.render())


def members_list(request):
    members = Member.objects.all().values()
    context = {
        'members': members
    }
    template = loader.get_template('all_members.html')

    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    context = {
        'member': member
    }
    template = loader.get_template('details.html')
    return HttpResponse(template.render(context, request))


def create_member(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render())


def testing(request):
    members = Member.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('tests.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))
