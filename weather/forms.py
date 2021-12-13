from django import forms

class CityForm(forms.Form):
    name = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(CityForm, self).clean()
        name = cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('You have to write something!')