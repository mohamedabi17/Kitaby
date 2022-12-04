from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import  User,Admin,Categorie,Book,LigneCommande,Client,Paiment,Commande
# from .serializers import ClientSerializer,BookSerializer
from rest_framework import status
from api.serializers import ClientSerializer,CategorieSerializer,BookSerializer
# import requests
# from django.shortcuts import render
# from django.db import connection
# from django.http import HttpResponse



@api_view(['GET'])
def getproducts(request):
    if (request.method =='GET'):
        allBooks = Book.objects.all()
        serilize = BookSerializer(allBooks,many=True)
        return Response(serilize.data)
    
@api_view(['GET'])
def getcategories(request):
    if (request.method =='GET'):
        allcotegories = Categorie.objects.all()
        serilize = CategorieSerializer(allcotegories,many=True)
        return Response(serilize.data)
    
@api_view(['GET'])
def getclients(request):
    if (request.method =='GET'):
        allclients = Client.objects.all()
        serilize = ClientSerializer(allclients,many=True)
        return Response(serilize)
        
# @api_view(['GET'])
# def getcategories(request):
#     if (request.method =='GET'):
#         allcategories = Categorie.objects.all().values()
#         return Response(allcategories)
    

# @api_view(['GET'])
# def GetProductsInCategorie(request):
#     if (request.method =='GET'):
#         ID_Cat =3;
#         cursor = connection.cursor()
#         cursor.execute("SELECT titre FROM Produit WHERE id_categorie=%s",ID_Cat)
#         result = cursor.fetchall()
#         print(result)
#         # allproducts = Produit.objects.all().values()
#         return Response(result)
    
# @api_view(['GET'])
# def GetProductsInCategorie(request):
#     if (request.method =='GET'):
#         # allproducts = Produit.objects.raw('SELECT titre FROM Produit WHERE id_categorie=%s",ID_Cat')
#         product = Produit.objects.values().get(id_categorie=1)
#         # allproducts = Produit.objects.all().values().get(id_product=5)
#         return Response(product)
    

# def verify(ob){
#     pass
# }
# @api_view(['GET'])
# def getclients(request):
#     if (request.method =='GET'):
#         allclients = Client.objects.all().values()
#         # clients = map(verify,clients)
#         return HttpResponse(allclients)
    # else:
    #     if(request.method =='POST'):
    #         serializer = ProduitSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response(serializer.data)
        
# @api_view(['POST'])
# def addproduit(request):
#     if request.method=="POST":
#         proserilize =ProduitSerializer(data=request.data)
#         if proserilize.is_valid():
#             proserilize.save()
#             return Response(proserilize.data, status=status.HTTP_201_CREATED);
#         else:
#             return Response(proserilize.data,status=status.HTTP_400_BAD_REQUEST);


# @api_view(['POST'])
# def addData(request):
#     serializer = ProduitSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# def insertcategorie(request):
#     if request.method=="POST":
#         id_categorie=request.POST.get('id_categorie')
#         titre_category=request.POST.get('titre_category')
#         nbr_prodcate=request.POST.get('nbr_prodcate')
#         data ={'id_categorie':id_categorie,'titre_category':titre_category,'nbr_prodcate':nbr_prodcate}
#         headers={'Content-Type': 'application/json'}
#         requests.post('http://127.0.0.1:8000/Insertcategorieapi',json=data,headers=headers)
#         return render(request,'Addproduct.js')
#     else:
#         return render(request,'Addproduct.js ')
        

# def insertproduct(request):
#     if request.method=="POST":
#         id_product=request.POST.get('id_product')
#         titre=request.POST.get('titre')
#         id_categorie=request.POST.get('id_categorie')
#         description=request.POST.get('description')
#         img=request.POST.get('img')
#         price=request.POST.get('price')
#         data ={'id_product':id_product,'titre':titre,'id_categorie':id_categorie,'description':description,'img':img,'price':price}
#         headers={'Content-Type': 'application/json'}
#         requests.post('http://127.0.0.1:8000/Insertproduitapi',json=data,headers=headers)
#         return render(request,'Addproduct.js')
#     else:
#         return render(request,'Addproduct.js')
        
# @api_view(['POST'])
# def addcategorie(request):
#     if request.method =="POST":
#         saveserilize = CategorieSerializer(data=request.data)
#         if saveserilize.is_valid():
#             saveserilize.save()
#             return Response(saveserilize.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(saveserilize.data,status=status.HTTP_400_BAD_REQUEST);

# @api_view(['POST'])
# def addcart(request):
#     if request.method =="POST":
#         saveserilize = CartSerializer(data=request.data)
#         if saveserilize.is_valid():
#             saveserilize.save()
#             return Response(saveserilize.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(saveserilize.data,status=status.HTTP_400_BAD_REQUEST);
        
# @api_view(['POST'])
# def addachat(request):
#     if request.method =="POST":
#         saveserilize = AchatSerializer(data=request.data)
#         if saveserilize.is_valid():
#             saveserilize.save()
#             return Response(saveserilize.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(saveserilize.data,status=status.HTTP_400_BAD_REQUEST);