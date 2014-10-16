from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
<<<<<<< HEAD
from chu2pa.models import UserStatus
=======
from chu2pa.models import UserStatus, Calendar
>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    TITLE_CHOICES = (
                        ('T', 'Teacher'),
                        ('S', 'Student'),
                     )
    title = forms.ChoiceField(choices=TITLE_CHOICES)
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
<<<<<<< HEAD
=======

>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68
    class Meta(UserCreationForm.Meta):
        model = UserStatus
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "title")

class MyUserAdmin(UserAdmin):
    add_form = EmailUserCreationForm
<<<<<<< HEAD
# class CalendarForm()
=======




>>>>>>> 7d5ca9f58d7e301285c97cb0f360632a4f0e1c68
