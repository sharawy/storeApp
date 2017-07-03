from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from product_manager.models import Product


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = { 'username', 'password1', 'password2', 'email'}

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        if commit:
            user.save()

        return user


class AddRemoveProductToCartForm(forms.ModelForm):
    id = forms.IntegerField(required=True)
    action = forms.CharField(max_length=10,required=True,min_length=1)

    class Meta:
        model = Product
        fields = ['id','action']