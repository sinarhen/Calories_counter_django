from django import forms

BIG_QUANTITY_VALUE_ERROR = 'Too big value, please enter a value less then 100'

GENDER_CHOICES = {
    '1': 'Male',
    '2': "Female",
}.items()
PHYSICAL_ACTIVITY_CHOICES = {'2': 'Minimum quantity of physical activity',
                             '3': '3 times a week', '4': '5 times a week',
                             '5': 'Every day', '6': 'Every day very intensive or 2 times a day',
                             '7': 'Every day training and physical work'}.items()


class CartEditProductQuantityForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    def clean_quantity(self):
        val = self.cleaned_data['quantity']
        if val >= 100:
            raise forms.ValidationError(BIG_QUANTITY_VALUE_ERROR)
        return val


class CalcForm(forms.Form):
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    physical_activity = forms.ChoiceField(choices=PHYSICAL_ACTIVITY_CHOICES)
