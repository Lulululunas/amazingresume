from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Resume
from .forms import CvForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.conf import settings


def form(request):
    return render(request, 'funny/resume.html')

def final(request):

    data = Resume.objects.filter(user=request.user).last()
    return render(request, 'funny/forma.html', {'data': data})


def hello(request):
    return HttpResponse("Hello on our service")
    
@login_required
def results(request):
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES or None)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            # messages.success(request, f'YooOoo-Hooo...')
            return redirect('final')

    else:
        form = CvForm()
        # messages.success(request, f'Fill the form')
    return render(request, 'funny/resume.html', {'form': form})


import pdfkit
from django.http import HttpResponse
from django.template import loader

def create_pdf(request):
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    data = Resume.objects.filter(user=request.user).last()
    html = loader.render_to_string('funny/result.html', {'data': data})
    output= pdfkit.from_string(html, output_path=False, configuration=config, options={"enable-local-file-access": ""})
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response