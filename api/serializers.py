from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer
from .models import User,Admin,Categorie,Book,LigneCommande,Client,Paiment,Commande


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model =User
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Client
        fields = '__all__'
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Admin
        fields = '__all__'
        
class CategorieSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Categorie
        fields = '__all__'
        
class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Book
        fields ='__all__'
        
class CommandeSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Commande
        fields = '__all__'
        
class LigneCommandeSerializer(serializers.ModelSerializer):
    class Meta: 
        model =LigneCommande
        fields = '__all__'
class PaimentSerializer(serializers.ModelSerializer):
    class Meta: 
        model =Paiment
        fields = '__all__'