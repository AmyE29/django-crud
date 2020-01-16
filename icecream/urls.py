from django.urls import path
from .views import HomePageView, FlavorDetailView, FlavorCreateView, FlavorUpdateView, FlavorDeleteView


urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('icecream/<int:pk>/', FlavorDetailView.as_view(), name='flavors_details'),
    path('icecream/new/', FlavorCreateView.as_view(), name='flavors_new'),
    path('icecream/<int:pk>/update/', FlavorUpdateView.as_view(), name='flavors_update'),
    path('icecream/<int:pk>/delete/', FlavorDeleteView.as_view(), name='flavors_delete'),
]
