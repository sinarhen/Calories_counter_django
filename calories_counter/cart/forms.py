from django import forms

# Error message for when the quantity value is too big
BIG_QUANTITY_VALUE_ERROR = 'Too big value, please enter a value less than 100'

# Choices for gender selection
GENDER_CHOICES = {
    '1': 'Male',
    '2': 'Female',
}.items()

# Choices for physical activity selection
PHYSICAL_ACTIVITY_CHOICES = {
    '2': 'Minimum quantity of physical activity',
    '3': '3 times a week',
    '4': '5 times a week',
    '5': 'Every day',
    '6': 'Every day very intensive or 2 times a day',
    '7': 'Every day training and physical work',
}.items()

class CartEditProductQuantityForm(forms.Form):
    """
    Form for editing the quantity of a product in the cart.
    """
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def clean_quantity(self):
        """
        Custom validation for the quantity field.
        Ensures the quantity is less than 100.
        """
        val = self.cleaned_data['quantity']
        if val >= 100:
            raise forms.ValidationError(BIG_QUANTITY_VALUE_ERROR)
        return val

class CalcForm(forms.Form):
    """
    Form for calculating various parameters based on user input.
    """
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    physical_activity = forms.ChoiceField(choices=PHYSICAL_ACTIVITY_CHOICES)

# Usage example in a Django view:
# cart_form = CartEditProductQuantityForm(request.POST)
# calc_form = CalcForm(request.POST)
# ...