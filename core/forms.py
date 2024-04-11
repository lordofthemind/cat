from django.forms import ModelForm
from .models import UserModel

class CreateUserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'age', 'email', 'dob']