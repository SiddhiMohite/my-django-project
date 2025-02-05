from django import forms
from .models import Details

 
class detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"

# class EmpForm(forms.Form):
#     no=forms.IntegerField(label="Enter Sr. no.")
#     id=forms.IntegerField(label="Enter Id")  
#     firstname = forms.CharField(label="Enter first name",max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length = 10)  
#     email     = forms.EmailField(label="Enter Email")  
#     file      = forms.FileField() # for creating file input  
 