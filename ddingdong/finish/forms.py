from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Search name", max_length=7)
