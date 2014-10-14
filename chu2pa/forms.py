from django import forms
from django.contrib.auth.forms import UserCreationForm
from chu2pa.models import UserStatus


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    TITLE_CHOICES = (
                        ('T', 'Teacher'),
                        ('S', 'Student'),
                     )
    title = forms.ChoiceField(choices=TITLE_CHOICES)

    class Meta:
        model = UserStatus
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "title")

# class CalendarForm()



