from django.contrib import admin
from .models import (
    Order, 
    Book, 
    Author
)


admin.site.register(Order)
admin.site.register(Book)
admin.site.register(Author)
# Register your models here.
