from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_names = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        if self.middle_names:
            return self.first_name + ' ' + self.middle_names + ' ' + self.last_name

        else:
            return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=1500, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return self.title

    
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Książka')
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100, verbose_name='Nazwa ulicy', 
                                    validators=[RegexValidator(regex="[a-zA-ZŻŹĆĄŚĘŃŁÓżźćąśęńłó]", message="Zły format nazwy ulicy: tylko litery")])
    num_building = models.CharField(max_length=4, verbose_name='Numer mieszkania', 
                                    validators=[RegexValidator(regex="[0-9]", message="Zły format numeru mieszkania: XXXX(cyfry)")])
    num_door = models.CharField(max_length=4, null=True, blank=True, verbose_name='Numer lokalu', 
                                    validators=[RegexValidator(regex="[0-9]", message="Zły format numeru lokalu: XXXX(cyfry)")])
    post_code = models.CharField(max_length=6, verbose_name='Kod pocztowy', 
                                    validators=[RegexValidator(regex="\d{2}-\d{3}", message="Zły format kodu pocztowego: XX-XXX (cyfry)")] )
    city = models.CharField(max_length=100, verbose_name='Miejscowość', 
                                    validators=[RegexValidator(regex="[a-zA-ZŻŹĆĄŚĘŃŁÓżźćąśęńłó]", message="Zły format miejscowości: tylko litery")])
    country = CountryField(verbose_name='Kraj', default="PL")
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(blank=True)

    def save(self):
        days = timedelta(days=30)

        if not self.id:
            self.date_end = datetime.now() + days
        
        super().save()

    def __str__(self):
       return str(self.book)

    def get_absolute_url(self):
        return reverse("orders-list")
    