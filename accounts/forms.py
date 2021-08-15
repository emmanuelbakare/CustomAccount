from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms 


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    phone=forms.CharField(max_length=50, required=True)
    class Meta:
        model = get_user_model()
        fields = ['email','phone']