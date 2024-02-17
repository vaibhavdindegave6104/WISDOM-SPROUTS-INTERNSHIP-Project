import datetime
from django.contrib.auth.models import User
from django  import forms
from django.utils.html import format_html

from .models import Task
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class DateTimeWidget(forms.widgets.MultiWidget):
    def __init__(self, date_format=None, time_format=None, attrs=None):
        widgets = [
            forms.DateInput(format=date_format, attrs={'type': 'date'}),
            forms.TimeInput(format=time_format, attrs={'type': 'time'}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time()]
        return [None, None]

class DateTimeField(forms.fields.MultiValueField):
    widget = DateTimeWidget

    def __init__(self, date_format=None, time_format=None, *args, **kwargs):
        fields = [
            forms.DateField(input_formats=[date_format]),
            forms.TimeField(input_formats=[time_format]),
        ]
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            date, time = data_list
            return datetime.datetime.combine(date, time)
        return None

class DateTimeLocalInput(forms.widgets.Input):
    input_type = 'datetime-local'


class TaskForm(forms.ModelForm):
    due_datetime = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=DateTimeLocalInput(),)
    class Meta:
        model=Task
        fields=['title','description','priority','completed','due_datetime',]
        widgets = {

            'created': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class UserLoginForm(AuthenticationForm):
    # Customize fields if needed
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):
    # Customize fields if needed
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']