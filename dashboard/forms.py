from django import forms 
from .models import * 
from users.models import Profile


# Create forms here
class IncomeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['income']


class NewExpenditureForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={
                                                            'class':'Input',
                                                            'placeholder':'Description of what you have spent on...', }))

    amount = forms.IntegerField(widget=forms.TextInput(attrs={
                                                            'class':'Input',
                                                            'placeholder':'Cost'}))


    class Meta:
        model = Expenses
        fields = ['description', 'amount', 'category']