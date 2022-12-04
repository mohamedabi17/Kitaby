from django.urls import path
from . import views

urlpatterns = [
    path('getproducts',views.getproducts),
    # path('getproductbycategory',views.GetProductsInCategorie),
    path('getcategories',views.getcategories),
    path('getclients',views.getclients),
    # path('addproduct',views.addData),
    # path('Insertcategorieapi',views.addcategorie,name="addcategorie"),
    # path('Insertproduitapi',views.insertproduct,name="insertproduct"),
    # path('Insertcartapi',views.addcart,name="addcart"),
    # path('Insertachatapi',views.addachat,name="addachat"),
    # path('insertcategorie',views.insertcategorie,name="insertcategorie"),
    # path('',views.insertproduct),
]
