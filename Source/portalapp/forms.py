from django import forms
#from django.contrib.admin.widgets import AdminDateTimeWidget
from django.contrib.admin import widgets
from .models import Register
from django.forms import DateTimeField
# from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from datetime import datetime
from django.forms.fields import DateTimeField
from django.forms.extras.widgets import SelectDateWidget
from tinymce.models import HTMLField
from django import forms
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class TalkForm(forms.ModelForm):
          #on_date=forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'],default=datetime.now)
          coordinator = forms.CharField(label='Faculty Coordinator')
          bio = forms.CharField(label='Bio of the speaker', widget=forms.Textarea())
          #on_date = forms.DateTimeField(label='Date And Time')

          #on_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
          class Meta:
              model = Register
              fields = ('topic', 'speaker','date_and_time','venue','abstract','bio','coordinator',)

"""class FlatPageForm(forms.ModelForm):
    #fields
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields="__all__"
"""
'''widgets = {
            'bio': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
              }'''
