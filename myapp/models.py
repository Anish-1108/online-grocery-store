from django.db import models

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField(default=1234)

    def __str__(self):
        return self.email
    

class maincatagory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Add_product(models.Model):
    main_id = models.ForeignKey(maincatagory,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to = "img")
    name = models.CharField(max_length=30)
    quantuty = models.IntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    

class Add_to_cart(models.Model):
    product_id = models.ForeignKey(Add_product, on_delete=models.CASCADE)
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to = "img")
    name = models.CharField(max_length=30)
    quantuty = models.IntegerField(default=1)
    price = models.IntegerField()
    total_price = models.IntegerField()



class Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    Saddress = models.CharField(max_length=500)
    Aaddress = models.CharField(max_length=500)
    town_city = models.CharField(max_length=500)
    Country_State = models.CharField(max_length=200)
    phon = models.IntegerField()
    email = models.EmailField(max_length=50)




 


