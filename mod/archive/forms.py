from .models import Contracts, Acts, Companies
from django.forms import ModelForm, TextInput, NumberInput, DateInput, Select, IntegerField


class CompanyUpdForm(ModelForm):
    class Meta:
        model = Companies
        fields = ['title', 'inn']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название подрядчика'
            }),
            'inn': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер ИНН'
        })
        }


class ContractUpdForm(ModelForm):
    class Meta:
        model = Contracts
        fields = ['title', 'number', 'price', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название договора'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер договора'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена договора'
            }),
            'date': DateInput(attrs={
                'input_type':"date",
                'class': 'form-control datetimepicker-input'
        })
        }

class ActUpdForm(ModelForm):
    class Meta:
        model = Acts
        fields = ['contract', 'title', 'number', 'price', 'date']

        widgets = {
            'contract': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Договор'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название акта'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер акта'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена акта'
            }),
            'date': DateInput(attrs={
                'input_type':"date",
                'class': 'form-control datetimepicker-input'
        })
        }

class DateInput(DateInput):
    input_type = 'date'

class ContractCreateForm(ModelForm):
    class Meta:
        model = Contracts
        fields = ['title', 'number', 'price', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название договора'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер договора'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена договора'
            }),
            'date': DateInput(attrs={
                'input_type':"date",
                'class': 'form-control datetimepicker-input'
        })
        }


class ActCreateForm(ModelForm):
    class Meta:
        model = Acts
        fields = ['contract', 'title', 'number', 'price', 'date']

        widgets = {
            'contract': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Договор'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название акта'
            }),
            'number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер акта'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена акта'
            }),
            'date': DateInput(attrs={
                'input_type':"date",
                'class': 'form-control datetimepicker-input'
        })
        }

class CompanyCreateForm(ModelForm):
    class Meta:
        model = Companies
        fields = ['inn', 'title']

        widgets = {
            'inn': NumberInput(attrs={
                'maxlength': 10,
                'minlength': 10,
                'class': 'form-control',
                'placeholder': 'ИНН компании (10 символов)'
            }),
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Контрагента'
        })
        }

