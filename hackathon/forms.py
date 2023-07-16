from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class UserBaseForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

#회원가입폼
class UserCreateForm(UserBaseForm):
    #유효성 검사 비밀번호 확인용
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta(UserBaseForm.Meta):
        fields = ['username', 'password']



class SingUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username',]