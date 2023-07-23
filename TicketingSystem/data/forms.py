from django.forms import Form, CharField
from django import forms
from django.db.models import Q 



class SearchForm(Form):
    keyword = CharField(max_length=20,
    widget=forms.TextInput(attrs={'placeholder': 'Search....'}),required=False)
    FILTER_CHOICES = [
        ('', 'Filter by'),
        ('All', 'All'),
        ('status_open', 'Status Open'),
        ('status_close', 'Status Close'),
        ('ONU down', ' Down'),
        ('ONU up', 'up'),
        ('pon_status_up', 'pon Status Up'),
        ('pon_status_down', 'pon Status Down')
    ]
    #lass SearchForm(forms.Form):
    Filter_by = forms.ChoiceField(choices=FILTER_CHOICES, required=False)

    FILE_FORMAT_CHOICES = [
        ('csv', 'CSV'),
        ('pdf', 'PDF'),
        ('xlsx', 'Excel'),
        
    ]
    file_format = forms.ChoiceField(choices=FILE_FORMAT_CHOICES, required=False)