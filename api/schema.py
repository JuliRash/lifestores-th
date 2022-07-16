import graphene

from graphene_django import DjangoObjectType

from api.models import Product


# class BookType(DjangoObjectType):
#     class Meta:
#         model= Book
#         fields = ('id', 'name', 'excerpt')
  
        
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'sku', 'image')
  
        
class Query(graphene.ObjectType):
    # all_books = graphene.List(BookType)
    all_products = graphene.List(ProductType)
    
    def resolve_all_books(root, info):
        return Book.objects.filter(id=1)
    
    def resolve_all_products(root, info):
        return Product.objects.all();
    

schema = graphene.Schema(query=Query)