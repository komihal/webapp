from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Contracts, Acts, Companies
from .forms import ContractCreateForm, ContractUpdForm, ActCreateForm, ActUpdForm, CompanyCreateForm, CompanyUpdForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from operator import attrgetter


class ContractHome(ListView):
    model = Contracts
    template_name = 'archive/contract_home.html'
    context_object_name = 'contracts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Договоры"
        context['navbar'] = 'contract'
        return context


class ActHome(ListView):
    model = Acts
    template_name = 'archive/acts_home.html'
    context_object_name = 'acts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Акты"
        context['navbar'] = 'act'
        context['contracts'] = Contracts.objects.all()
        return context


class CompanyHome(ListView):
    model = Companies
    template_name = 'archive/company_home.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контрагенты"
        context['navbar'] = 'company'
        return context


class ContractCreateView(CreateView):
    form_class = ContractCreateForm
    template_name = 'archive/create.html'
    success_url = reverse_lazy("contract-home")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Новый контракт"
        context['navbar'] = 'contract'
        return context


class ActCreateView(CreateView):
    form_class = ActCreateForm
    template_name = 'archive/create_act.html'
    success_url = reverse_lazy("acts")

    def __init__(self):
        self.pk = ""

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Новый акт"
        context['navbar'] = 'act'
        if self.pk != "":
            context['contract'] = Contracts.objects.all()
        elif self.kwargs['pk']:
            context['pk'] = self.kwargs['pk']
            context['contract'] = Contracts.objects.get(id=self.kwargs['pk'])
        return context

    def get_initial(self):
        if self.pk != "":
            contract = Contracts.objects.all()
            return ()
        elif self.kwargs['pk']:
            contract = get_object_or_404(Contracts, id=self.kwargs.get('pk'))
            retention_rate = contract.retention_rate
            company = contract.company
            return {
                'contract': contract,
                'warranty_percent': retention_rate,
            }



class CompanyCreateView(CreateView):
    form_class = CompanyCreateForm
    template_name = 'archive/create_company.html'
    success_url = reverse_lazy("company-home")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Новый контрагент"
        context['navbar'] = 'company'
        return context


class ContractDetailView(DetailView):
    model = Contracts
    template_name = 'archive/contract_detail.html'
    context_object_name = 'contract'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Детали контракта"
        context['acts'] = Acts.objects.all()
        context['pk'] = self.kwargs['pk']
        context['navbar'] = 'contract'
        context['company'] = Companies.objects.all()
        context['fields_act'] = [field.verbose_name for field in Acts._meta.get_fields()]
        context['fields_contr'] = Contracts._meta.get_fields()
        return context

    def get_fields(self):
        return [(field.name, getattr(self, field.name)) for field in Acts._meta.fields]
        return [(field.name, getattr(self, field.name)) for field in Contracts._meta.fields]


class ContractUpdateView(UpdateView):
    model = Contracts
    template_name = 'archive/update.html'
    context_object_name = 'contract'

    form_class = ContractUpdForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактировать контракт"
        context['navbar'] = 'contract'
        return context


class ContractDeleteView(DeleteView):
    model = Contracts
    success_url = reverse_lazy('contract-home')
    template_name = 'archive/contract-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Удалить контракт"
        context['navbar'] = 'contract'
        return context


class ActDetailView(DetailView):
    model = Acts
    template_name = 'archive/acts_detail.html'
    context_object_name = 'act'

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(ActDetailView, self).get_context_data(**kwargs)
        context['contr'] = Contracts.objects.filter(acts=self.get_object())
        context['title'] = "Детали акта"
        context['navbar'] = 'act'
        return context


class ActUpdateView(UpdateView):
    model = Acts
    template_name = 'archive/update_act.html'
    context_object_name = 'act'
    form_class = ActUpdForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактировать акт"
        context['navbar'] = 'act'
        return context


class ActDeleteView(DeleteView):
    model = Acts
    success_url = reverse_lazy('acts')
    template_name = 'archive/contract-delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Удалить акт"
        context['navbar'] = 'act'
        return context


class CompanyDeleteView(DeleteView):
    model = Companies
    success_url = reverse_lazy('company-home')
    template_name = 'archive/contract-delete.html'
    slug_url_kwarg = 'comp_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Детали контрагента"
        context['navbar'] = 'company'
        return context


class CompanyDetailView(DetailView):
    model = Companies
    template_name = 'archive/companies_detail.html'
    context_object_name = 'company'
    slug_url_kwarg = 'comp_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Детали контрагента"
        context['navbar'] = 'company'
        context['contracts'] = Contracts.objects.all()
        context['fields_contr'] = [field for field in Contracts._meta.get_fields()]
        context['fields_companie'] = Companies._meta.get_fields()
        return context

    def get_fields(self):
        return [(field.name, getattr(self, field.name)) for field in Companies._meta.fields]


class CompanyUpdateView(UpdateView):
    model = Companies
    template_name = 'archive/update_company.html'
    context_object_name = 'company'
    slug_url_kwarg = 'comp_slug'

    form_class = CompanyUpdForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Детали контрагента"
        context['navbar'] = 'company'
        return context


def pageNotFound(request, exception):
                 return HttpResponseNotFound('<h1>Страница не найдена</h1>')



