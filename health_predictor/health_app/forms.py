from django import forms
class AlzheimerPredictionForm(forms.Form):
    image = forms.ImageField(label='Upload an MRI scan image', required=True)
