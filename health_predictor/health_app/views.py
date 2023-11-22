from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid,random
from django.contrib.auth.decorators import login_required
from datetime import datetime
#from .forms import UserForm,events_create
#from .models import user_details,events
from django.contrib.auth.models import User,auth
from django.contrib import messages
from itertools import chain

# Create your views here.
def index(request):
    return render(request,'index.html')