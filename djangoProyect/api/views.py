# Create your views here.
#from .models import Producto
#from .serializers import ProductoSerializer
from rest_framework import generics
from .models import Reservations
from .models import Clients
from .models import Rooms
from .models import Categories

from .serializers import ReservationsSerializer
from .serializers import RoomsSerializer
from .serializers import ClientsSerializer
from .serializers import CategoriesSerializer




# metodos productos
"""class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer"""




## Reservaciones
class ReservationsListCreate(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer


class ReservationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer




#Clientes
class ClientsListCreate(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer




#Habitacion
class RoomsListCreate(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class RoomsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


#Categoria
class CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer