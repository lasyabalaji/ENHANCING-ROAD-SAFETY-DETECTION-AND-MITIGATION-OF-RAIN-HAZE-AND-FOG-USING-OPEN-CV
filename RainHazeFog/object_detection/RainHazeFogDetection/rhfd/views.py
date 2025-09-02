from django.shortcuts import render

from rhfd.models import ImageModel
from rhfd.forms import ImageForm
from rhfd.haze_removal import enhance
import os

import cv2
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

def predict(request):

    imageForm = ImageForm(request.POST, request.FILES)

    if imageForm.is_valid():

        imageModel = ImageModel()
        imageModel.photo = imageForm.cleaned_data["photo"]
        imageModel.save()

        try:
            last=ImageModel.objects.last()
            imgpath =str(last.photo)

            enhance(imgpath)
            return render(request, 'result.html',{"result":"output.jpg"})

        except Exception as e:
            print("Exception:",e)
            return render(request, 'index.html', {"message": "Prediction Failed"})

    return render(request, 'index.html', {"message": "Invalid Form"})