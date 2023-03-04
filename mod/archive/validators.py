from django.core.exceptions import ValidationError
def validate_inn(value):
    if len(value) != 10:
        raise ValidationError('ИНН должен содержать 10 символов')
    if type(value) != int:
        raise ValidationError('ИНН должен быть числом')


