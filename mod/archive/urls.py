from django.urls import path
from . import views
from .views import pageNotFound

urlpatterns = [
    path("", views.CompanyHome.as_view(), name="company-home"),
    path("contracts_home/", views.ContractHome.as_view(), name="contract-home"),
    path("companies_home/", views.CompanyHome.as_view(), name="company-home"),
    path('create/', views.ContractCreateView.as_view(), name="create"),
    path('<int:pk>', views.ContractDetailView.as_view(), name="contract-detail"),
    path('<int:pk>/update', views.ContractUpdateView.as_view(), name="contract-update"),
    path('<int:pk>/delete', views.ContractDeleteView.as_view(), name="contract-delete"),
    path("acts_home/", views.ActHome.as_view(), name="acts"),
    path('create_act/', views.ActCreateView.as_view(), name="create_act"),
    path('create_act/<int:pk>', views.ActCreateView.as_view(), name="create_act1"),
    path('create_company/', views.CompanyCreateView.as_view(), name="create-company"),
    path('acts/<int:pk>', views.ActDetailView.as_view(), name="acts-detail"),
    path('acts/<int:pk>/update', views.ActUpdateView.as_view(), name="acts-update"),
    path('acts/<int:pk>/delete', views.ActDeleteView.as_view(), name="acts-delete"),
    path('companies/<slug:comp_slug>', views.CompanyDetailView.as_view(), name="companies-detail"),
    path('companies/<slug:comp_slug>/update', views.CompanyUpdateView.as_view(), name="company-update"),
    path('companies/<slug:comp_slug>/delete', views.CompanyDeleteView.as_view(), name="company-delete"),
]

handler404 = pageNotFound
# handler500
# handler403
# handler400