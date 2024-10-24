from django.urls import path
from . import views

urlpatterns = [
    #path('productos/', views.ProductoListCreate.as_view(), name='producto-list'),
    #path('productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),
    path('reservations/', views.ReservationsListCreate.as_view(), name='reservations-list'),
    path('reservations/<int:pk>/', views.ReservationsDetail.as_view(), name='reservations-detail'),
    path('clients/', views.ClientsListCreate.as_view(), name='clients-list'),
    path('clients/<int:pk>/', views.ClientsDetail.as_view(), name='clients-detail'),
    path('categories/', views.CategoriesListCreate.as_view(), name='categories-list'),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view(), name='categories-detail'),
    path('rooms/', views.RoomsListCreate.as_view(), name='rooms-list'),
    path('rooms/<int:pk>/', views.RoomsDetail.as_view(), name='rooms-detail'),

]