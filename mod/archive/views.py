from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Contracts, Acts, Companies
from .forms import ContractCreateForm, ContractUpdForm, ActCreateForm, ActUpdForm, CompanyCreateForm, CompanyUpdForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from operator import attrgetter


class ContractHome(ListView):
    model = Contracts
    template_name = 'archive/contract_home.html'
    context_object_name = 'contracts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контракты"
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

def create(request):
    error = ''
    if request.method == 'POST':
        form = ContractCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract-home')
        else:
            error = 'Проверьте корректность заполнения формы!'

    form = ContractCreateForm
    title = 'Форма создания договора:'
    data = {
        'form': form,
        'title':title,
        'error':error
    }
    return render(request, 'archive/create.html', data)

def create_act(request):
    error = ''
    if request.method == 'POST':
        form = ActCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acts')
        else:
            error = 'Проверьте корректность заполнения формы!'

    form = ActCreateForm
    title = 'Форма создания акта:'
    data = {
        'form': form,
        'title':title,
        'error':error
    }
    return render(request, 'archive/create_act.html', data)

def create_company(request):
    error = ''
    if request.method == 'POST':
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-home')
        else:
            error = form.errors

    form = CompanyCreateForm
    title = 'Форма создания контрагента:'
    data = {
        'form': form,
        'title': title,
        'error': error
    }
    return render(request, 'archive/create_company.html', data)

class ContractDetailView(DetailView):
    model = Contracts
    template_name = 'archive/contract_detail.html'
    context_object_name = 'contract'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Акты"
        context['acts'] = Acts.objects.all()
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

class ContractDeleteView(DeleteView):
    model = Contracts
    success_url = reverse_lazy('contract-home')
    template_name = 'archive/contract-delete.html'

class ActDetailView(DetailView):
    model = Acts
    template_name = 'archive/acts_detail.html'
    context_object_name = 'act'

    def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(ActDetailView, self).get_context_data(**kwargs)
        context['contr'] = Contracts.objects.filter(acts=self.get_object())
        return context

class ActUpdateView(UpdateView):
    model = Acts
    template_name = 'archive/update_act.html'
    context_object_name = 'act'

    form_class = ActUpdForm

class ActDeleteView(DeleteView):
    model = Acts
    success_url = reverse_lazy('acts')
    template_name = 'archive/contract-delete.html'

class CompanyDeleteView(DeleteView):
    model = Companies
    success_url = reverse_lazy('company-home')
    template_name = 'archive/contract-delete.html'

class CompanyDetailView(DetailView):
    model = Companies
    template_name = 'archive/companies_detail.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контрагенты"
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

    form_class = CompanyUpdForm



