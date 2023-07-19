from products.models import Product, Category

def categories_to_base(request):    
    categories = Category.objects.all()    
    return {'categories': categories}