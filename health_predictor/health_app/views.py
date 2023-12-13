from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid,random
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User,auth
from django.contrib import messages
from itertools import chain
from gradio_client import Client

# Create your views here.
def index(request):
    client = Client("https://adithyasnair-alzheimers-prediction-using-cnn.hf.space/")
    result = client.predict(
				"D:/Sem 5/Software/Software_engineering/health_predictor/ml_models/alzheimers/Non(1).jpg",	# str (filepath or URL to image) in 'image' Image component
				api_name="/predict")
    print(result)
    return render(request,'index.html',{'result':result})
