from django import forms

class MenuFormulario(forms.Form):
    menu = forms.CharField()
    precio = forms.IntegerField()

class BuscaMenuForm(forms.Form):
    menu = forms.TextInput()
    