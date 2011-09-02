from django.db import models
from django import forms 
from django.forms import ModelForm

# Create your models here.

class Text(models.Model):
    wash = models.CharField(max_length=12, blank=False)
    locked = models.BooleanField(default=False)
    text = models.TextField(blank=False)

class TextForm(forms.ModelForm):
    class Meta:
        model = Text

    def save(self):
        if not self.instance:
           self.bound_object = Text()

        self.bound_object.text = self.cleaned_data['text']
        self.bound_object.wash = self.cleaned_data['wash']
        self.bound_object.save()

