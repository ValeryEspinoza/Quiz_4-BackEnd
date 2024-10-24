from django.db import models


"""class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return str(self.nombre)
"""
class Clients(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emai = models.EmailField(unique=True, max_length=100)
    phone_number = models.IntegerField()

    def _str_(self):
        return str(self.name)

class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    description = models.TextField(null=False)

    def _str_(self):
        return str(self.category_name)


class Rooms(models.Model):
    id_room = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)
    room_number = models.IntegerField(null=False)
    room_price = models.DecimalField(max_digits=5, decimal_places= 2)
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.room_name)
    

class Reservations(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    Reservations_date = models.DateField(auto_now_add=True)
    checkin = models.DateTimeField(null=False)
    checkout = models.DateTimeField(null=False)
    reservation_status = models.CharField(max_length=20, null=False)
    reservation_description = models.TextField(null=False)
    id_client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.id_reservation)
    