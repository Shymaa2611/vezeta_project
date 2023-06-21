from django import forms
from .models import comments,posts,appoint,doctor_data

class commentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields='__all__'
class postForm(forms.ModelForm):
    class Meta:
        model=posts
        fields='__all__'
class appointForm(forms.ModelForm):
    class Meta:
        model=appoint
        fields='__all__'
class profileForm(forms.ModelForm):
    class Meta:
        model=doctor_data
        fields='__all__'
