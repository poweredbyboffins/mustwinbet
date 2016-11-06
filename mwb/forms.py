from django import forms

class ProbForm(forms.Form):
    prob = forms.IntegerField(label='Probability',initial=50)
    results = forms.IntegerField(label='Max number of results',initial=24)

