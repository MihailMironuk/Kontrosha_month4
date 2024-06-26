from .models import Review
from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = "__all__"
