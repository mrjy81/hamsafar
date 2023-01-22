from django import forms
from django.utils.translation import gettext_lazy as _

class ChargeForm(forms.Form):
    value = forms.IntegerField(label=_('مبلغ'))

    def clean_value(self):
        money = self.cleaned_data['value']
        if money > 0:
            return money
        raise forms.ValidationError('مقدار ناصحیح')
