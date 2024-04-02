from django import forms


class usersForm(forms.Form):
    
    num1=forms.CharField(label="Value 1 ",widget=forms.TextInput(attrs={'class': "form-control"}))
    num2=forms.CharField(label="Value 2 ",widget=forms.TextInput(attrs={'class': "form-control"}))
    num3=forms.CharField(label="Value 3 ",required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    email=forms.EmailField(label="Email ",widget=forms.TextInput(attrs={'class': "form-control"}))
    Gender=forms.BooleanField(required=False, label="Gender")
    