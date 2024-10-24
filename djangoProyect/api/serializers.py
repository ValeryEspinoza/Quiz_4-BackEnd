from rest_framework import serializers
#from .models import Producto
from .models import Reservations
from .models import Clients
from .models import Rooms
from .models import Categories


#class ProductoSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Producto
        #fields = '__all__'

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'
    
    def validate_reservation_description(self, values):
        if any(char in values for char in ['<', '>', '&', '*',  '¿', '?', '|']):
            raise serializers.ValidationError("Invalid characters in input.")
        return values
    
    def validate_reservation_status(self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values 

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
        
    def validate_name (self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values   
        
    def validate_last_name (self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values  
    
    def validate_emai (self, values):
        if len(values) <= 10:
           raise serializers.ValidationError(
               "Error: The name must contain at least 10 characters"
           )
        return values
        

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

    def validate_room_name (self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values
    
    def validate_room_price (self, values):
        if values <= 10.00:
           raise serializers.ValidationError(
               "Error:  The price must be at least $10.0"
           )
        return values

    def validate_room_name (self, values):
        if any(char in values for char in ['<', '>', '&', '/', '.', '¿', '?', '|']):
            raise serializers.ValidationError("Invalid characters in input.")
        return values
    


"""Validaciones para Categorias"""
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
    def validate_category_name (self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: no less than 5 letters allowed"
           )
        return values
    
    def validate_category_name (self, values):
        if any(char in values for char in ['<', '>', '&', '/', '.', '¿', '?', '|']):
            raise serializers.ValidationError("Invalid characters in input.")
        return values
    
    def validate_description (self, values):
        if any(char in values for char in ['<', '>', '&', '*',  '¿', '?', '|']):
            raise serializers.ValidationError("Invalid characters in input.")
        return values
        
    