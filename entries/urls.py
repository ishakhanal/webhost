from django.urls import path
from .views import HomeView, ContractView, CreateContractView, UserDetailView, HomeView1
from . import views
from django.views.generic import TemplateView


urlpatterns = [

    path('', HomeView.as_view(), name = 'letsbid-home'),
    path('contract/<int:pk>/', ContractView.as_view(), name = 'contract-detail'),
   	path('create_contract/', CreateContractView.as_view(success_url='/'), name = "create_contract"),
   	path('contract/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
   	path('about/', TemplateView.as_view(template_name='entries/about.html'), name = 'about'),
   	path('details/<int:pk>/',UserDetailView.as_view(), name = 'user-details'),
   	path('home/', HomeView1.as_view(), name='home'),




]
