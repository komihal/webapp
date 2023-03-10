from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from unidecode import unidecode



def validate_inn(value):
    if len(str(value)) != 10:
        raise ValidationError('ИНН должен содержать 10 символов')
    if type(value) != int:
        raise ValidationError('ИНН должен быть числом')


class Contracts(models.Model):
    number = models.CharField('Номер', max_length=25, unique=True)
    title = models.CharField('Название', max_length=120)
    price = models.FloatField('Цена договора', max_length=25)
    date = models.DateField('Дата договора')
    retention_rate = models.FloatField('% гарант. удерж.', max_length=4)
    company = models.ForeignKey('companies', on_delete=models.PROTECT, null=True, verbose_name="Компания")
    work_stage = models.ForeignKey('WorkStage', on_delete=models.PROTECT, null=True, verbose_name="Вид работ")

    def __str__(self):
        return self.company.title + " " + self.title + " " + self.number

    def get_absolute_url(self):
        return f'/archive/{self.id}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def get_fields(self):
        return [(field.name, field.verbose_name, field.value_to_string(self)) for field in Contracts._meta.fields]

class Companies(models.Model):
    title = models.CharField('Название компании', max_length=120)
    inn = models.IntegerField('ИНН', unique=True, validators=[validate_inn])
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title), allow_unicode=True)
        super(Companies, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/archive/companies/{self.slug}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Acts(models.Model):
    title = models.CharField('Название акта', max_length=120)
    number = models.CharField('Номер акта', max_length=25, unique=True)
    price = models.FloatField('Цена акта', max_length=25)
    date = models.DateField('Дата акта')
    warranty_retention = models.FloatField('Гарантийное удержание', max_length=25, null=True)
    warranty_percent = models.FloatField('Процент удержания', max_length=25, null=True)
    contract = models.ForeignKey(Contracts, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return self.title

    def warranty_retention_base(self):
        price = self.cleaned_data.get('price')
        warranty_retention = self.cleaned_data.get('warranty_retention')
        if price and warranty_retention:
            warranty_retention_base = price * warranty_retention
            self.cleaned_data['warranty_retention'] = warranty_retention_base
            return warranty_retention_base

    def get_absolute_url(self):
        return f'/archive/acts/{self.id}'

    class Meta:
        verbose_name = 'Акт'
        verbose_name_plural = 'Акты'


class WorkStage(models.Model):
    title = models.CharField('Название', max_length=120)
    number = models.CharField('Номер', max_length=25, unique=True)
    budget_in = models.FloatField('Цена договора', max_length=25)
    budget_out = models.FloatField('Цена договора', max_length=25)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/archive/{self.id}'

    class Meta:
        verbose_name = 'Этап работ'
        verbose_name_plural = 'Этапы работ'