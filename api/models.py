from django.db import models
import datetime

        
class User(models.Model):
    id_user= models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone =  models.CharField(max_length=14)
    username = models.CharField(max_length=30)
    password = models.TextField(max_length=30)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_user'
        
class Admin(models.Model):
    
    id_admin = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    surname = models.CharField(max_length=30)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_admin'
        
class Client(models.Model):
    
    id_client = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    niv_fidélité = models.IntegerField(default=1)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_client'
    

class Categorie(models.Model):
    
    id_categorie = models.AutoField(primary_key=True)
    titre_category = models.CharField(max_length=400)
    nbr_book = models.IntegerField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_categorie'
    
class Paiment(models.Model):
    
    id_paiment = models.AutoField(primary_key=True)
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_paiment'


class Commande(models.Model):
    
    id_commande = models.AutoField(primary_key=True)
    Commande_price = models.FloatField()
    id_paiment =  models.ForeignKey(Paiment,on_delete=models.PROTECT)
    id_client =  models.ForeignKey(Client,on_delete=models.CASCADE)
    id_user =  models.ForeignKey(User,on_delete=models.CASCADE)
    nbr_produit =models.IntegerField()
    price_commande = models.FloatField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_commande'


    
class Book(models.Model):
    
    id_book = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    author =  models.CharField(max_length=200)
    id_categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=200)
    price=models.FloatField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_book'
    

class LigneCommande(models.Model):
    
    id_ligne=models.AutoField(primary_key=True)
    id_user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client,on_delete=models.CASCADE)
    id_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    id_categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    price_discount = models.FloatField()
    created_at = models.DateField(("Date"), default=datetime.date.today)
    updated_at = models.DateTimeField(auto_now_add=datetime.date.today)
    class Meta:
        db_table='app_lignecommande'

