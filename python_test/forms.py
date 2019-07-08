from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    email = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)
    suburb = forms.CharField(max_length=255, required=False)
