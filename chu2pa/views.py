import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.mail import EmailMultiAlternatives
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from psycopg2.extensions import JSON
from chu2pa.forms import EmailUserCreationForm
from chu2pa.models import Calendar
from pa2chu import settings
import datetime


def home(request):
    data = {'current_user': request.user}
    return render(request, 'home.html', data)


def faq(request):
    return render(request, 'faq.html')


def teacher(request):
    return render(request, 'teacher.html')


def student(request):
    logs = Calendar.objects.filter(person=request.user)
    return render(request, 'student.html', {'logs': logs})


@csrf_exempt
def student_check(request):

    current_datetime = datetime.datetime.now()
    year = str(current_datetime)[:4]
    month = str(current_datetime)[5:7]
    day = str(current_datetime)[8:10]
    hour = str(current_datetime)[11:13]
    min = str(current_datetime)[14:16]

    fulldate = month + "/" + day + "/" + year
    fullhour = hour + ":" + min
    print fullhour
    data = json.loads(request.body)
    check_in = Calendar.objects.create(person=request.user, date=fulldate, hour=fullhour, status=data )
    person = check_in.person.username
    status = check_in.status

    result = {'person': person,
              'date': fulldate,
              'hour': fullhour,
              'status': status
               }
    return HttpResponse(json.dumps(result),
                        content_type='application/json')

@csrf_exempt
def teacher_overview(request):
    collection = []
    data = json.loads(request.body)
    students_of_day = Calendar.objects.filter(date=data)
    for student in students_of_day:
        person = model_to_dict(student.person)
        person_name = person['username']
        collection.append({
            'person': person_name,
            'date': student.date,
            'hour': student.hour,
            'status': student.status
            })
    return HttpResponse(json.dumps(collection),
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