import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from psycopg2.extensions import JSON
from chu2pa.forms import EmailUserCreationForm
from chu2pa.models import Calendar
from pa2chu import settings


def home(request):
    data = {'current_user': request.user}
    return render(request, 'home.html', data)

def faq(request):
    return render(request, 'faq.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):

    return render(request, 'student.html')

@csrf_exempt
def student_check(request):
    check_in = Calendar.objects.create(person=request.user, status=True)
    person = check_in.person.username
    date = check_in.date
    status = check_in.status
    result = {'person': person,
              'date': date,
              'status': status
               }
    return HttpResponse(json.dumps(result),
                        content_type='application/json')

@login_required
def profile(request):
    return render(request, 'profile.html', {})

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website at {}, {} {}'.format(user.date_joined, user.first_name, user.last_name)
            html_content = '<h2>Thanks {} {} for signing up at {}!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
      })

# def check_status(request):
#     if request.user.title == "Student"