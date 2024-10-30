from django import forms

class PuzzleForm(forms.Form):
    selected_word = forms.ChoiceField(widget=forms.RadioSelect)
