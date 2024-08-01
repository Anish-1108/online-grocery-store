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
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)   
    user_name = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    address_2 = models.TextField()
    country = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    pincode = models.IntegerField()
    list = models.TextField()
 
class Order(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    qty = models.IntegerField()
    price = models.IntegerField()
    
    




 


