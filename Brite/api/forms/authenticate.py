from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from ..models import Employee, Company



class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    # Employee fields
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    role = forms.ChoiceField(choices=Employee.ROLE_CHOICES)
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Employee.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords do not match.")
        validate_password(password1)
        return password2

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )
        Employee.objects.create(
            user_name=user,
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            company=self.cleaned_data['company'],
            role=self.cleaned_data['role'],
            joining_date=self.cleaned_data.get('joining_date')
        )
        return user

class LoginForm(forms.Form):
    username = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput)