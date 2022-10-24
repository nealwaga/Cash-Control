from django import forms
from django.contrib.auth.models import User
from .models import Profile


# Create forms here
class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField (required=True)
    names = forms.CharField (required=True, 
                             widget=forms.TextInput(attrs={'class':'input',
                                                          'placeholder':'Name'})
                            )

    class Meta:
        model = Profile
        fields = ['Image', 'Name', 'Bio', 'Income']