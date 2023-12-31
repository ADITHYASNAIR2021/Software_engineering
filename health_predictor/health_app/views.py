from django.shortcuts import render,redirect
import numpy as np
import requests
from django.http import HttpResponse
import uuid,random
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User,auth
from django.contrib import messages
from PIL import Image
from itertools import chain
from gradio_client import Client
import joblib
from tempfile import NamedTemporaryFile
from health_app.forms import AlzheimerPredictionForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def alzheimers(request):
    if request.method == 'POST':
        image = request.FILES['image']

        with NamedTemporaryFile(delete=True) as tmp:
            for chunk in image.chunks():
                tmp.write(chunk)
            tmp.flush()

            img = Image.open(tmp)
            processed_img = img.resize((128, 128))  

            with open('D:/College-works/Sem 5/Software/Software_engineering/health_predictor/ml_models/alzheimers/alzheimers_model.sav', 'rb') as f:
                model = joblib.load(f)

            img_array = np.array(processed_img)
            img_array = img_array.reshape(1, 128, 128, 3)  # Assuming grayscale

            prediction = model.predict(img_array)
            prediction_class = np.argmax(prediction)

            labels = ['Non Demented', 'Mild Dementia', 'Moderate Dementia', 'Very Mild Dementia']

            # Pass both image URL and prediction to the template
            return render(request, 'alzheimers.html', {'image': image, 'prediction': labels[prediction_class]})
    else:
        return render(request, 'alzheimers.html')


