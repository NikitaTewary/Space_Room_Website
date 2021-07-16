from django.shortcuts import render

# Create your views here.
#group auth_views

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember
class CreateGroup(LoginRequiredMixin,generic:CreateView):
    fields=('name','description')
    model=Group

class SigleGroup(generic.DetailView):
    model=Group

class ListGroups(generic.ListView):
    model=Group
