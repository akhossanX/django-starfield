from django import forms
from django_starfield import Stars

class RatingForm(forms.Form):
    rating_1 = forms.IntegerField(label='Default rating', widget=Stars)
    rating_2 = forms.IntegerField(label='Big rating', widget=Stars(stars=17))
    rating_3 = forms.IntegerField(label='Pink rating', widget=Stars(colour='#ff1493'))
    rating_4 = forms.IntegerField(label='Dolphin rating', widget=Stars(codepoint='1f42c'))
