from django.contrib import admin
from ecommerceapp.models  import Contact,Product,Orders,OrderUpdate

# Register your models 
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)