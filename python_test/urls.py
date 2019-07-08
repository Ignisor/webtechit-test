from django.urls import path
from django.views.generic import RedirectView

from python_test.views import ClientCreateView, ClientUpdateView, ClientListView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='client-list'), name='index'),
    path('client/create/', ClientCreateView.as_view(), name='client-create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client/list/', ClientListView.as_view(), name='client-list'),
]
