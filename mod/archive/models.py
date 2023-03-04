from django.db import models
from django.core.exceptions import ValidationError
def validate_inn(value):
    if len(str(value)) != 10:
        raise ValidationError('ИНН должен содержать 10 символов')
    if type(value) != int:
        raise ValidationError('ИНН должен быть числом')
class Contracts(models.Model):
    title = models.CharField('Название', max_length=120)
    number = models.CharField('Номер', max_length=25, unique=True)
    price = models.FloatField('Цена договора', max_length=25)
    date = models.DateField('Дата договора')
    company = models.ForeignKey('companies', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/archive/{self.id}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
class Companies(models.Model):
    title = models.CharField('Название компании', max_length=120)
    inn = models.IntegerField('ИНН', unique=True, validators=[validate_inn])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/archive/companies/{self.id}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
class Acts(models.Model):
    title = models.CharField('Название акта', max_length=120)
    number = models.CharField('Номер акта', max_length=25, unique=True)
    price = models.FloatField('Цена акта', max_length=25)
    date = models.DateField('Дата акта')
    contract = models.ForeignKey(Contracts, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/archive/acts/{self.id}'

    class Meta:
        verbose_name = 'Акт'
        verbose_name_plural = 'Акты'