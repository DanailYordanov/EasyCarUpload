from django import forms
from .models import Brand, Model, Car


class CarModelForm(forms.ModelForm):
    brand = forms.ModelChoiceField(
        Brand.objects.all(), label='Марка', empty_label='Избери')

    class Meta:
        model = Car
        fields = ['category', 'brand', 'model', 'modification', 'engine_type', 'price',
                  'transmission_type', 'fuel_type', 'power', 'displacement', 'year',
                  'month', 'run', 'color', 'euro_standart', 'description']
        widgets = {
            'description': forms.Textarea
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['model'].empty_label = 'Избери'

        if not self.is_valid():
            self.fields['model'].queryset = Model.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = Model.objects.filter(
                    brand=brand_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.model_set
