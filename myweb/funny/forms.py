from django import forms
from .models import Resume 

class CvForm(forms.ModelForm):
    first_name = forms.CharField(max_length=40, help_text="First name", label = 'First name', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    last_name = forms.CharField(max_length=40, help_text="Last name", label = 'Last name', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    user_email = forms.EmailField(max_length=40, help_text="Email", label = 'Email', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    education = forms.CharField(max_length=150, help_text="University", label = 'Education', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    experience = forms.CharField(max_length=150, help_text="Professional experience", label = 'Experience', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    skills = forms.CharField(max_length=150, help_text="Skills", label = 'Skills', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    languages = forms.CharField(max_length=150, help_text="Foreign languages", label = 'Languages', widget=(forms.TextInput(attrs={'class': 'form-control'})))
    image = forms.ImageField(label = 'image', widget=(forms.FileInput(attrs={'class': 'form-control'})))
    class Meta:
        model = Resume 
        fields = ('first_name', 'last_name', 'user_email', 'education', 'experience', 'skills', 'languages', 'image',)
