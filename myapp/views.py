from django.shortcuts import render,redirect
from .models import *
import razorpay
from django.conf import settings 
from django.core.mail import send_mail
import random

# Create your views here.

def index(request):
     if "email" in request.session:

        uid = User.objects.get(email=request.session['email'])
        lid = Add_to_cart.objects.all().count()
        mid=maincatagory.objects.all()
        pid = Add_product.objects.all()
        context ={
            'uid' : uid,
            'pid' : pid,
            'mid' : mid,
            'lid' : lid
        }
        return render(request, "myapp/index.html",context)

     else:
    
        return render(request, "myapp/login.html")
        
def login(request):
     if "email" in request.session:
         uid = User.objects.get(email=request.session['email'])                 
         
         context = {
             'uid' : uid
         }
         return render(request, "myapp/index.html",context)

     else:
        try:
            if request.POST:
                email = request.POST['email']
                password = request.POST['password']
                
                uid = User.objects.get(email=email,)
                if uid.password == password:

                    request.session['email'] = uid.email

                    context = {

                        'uid' : uid
                    }

                    # return render(request, "myapp/index.html",context)
                    return redirect("index")
                else:
                    n_msg = "INVALID PASSWORD"
                    context = {

                        "n_msg" : n_msg
                    }
                    return render(request, "myapp/login.html",context)
            else:
                return render(request, "myapp/login.html")
        except:
            context ={
                'e_msg' : "Invalid email....."
            }
            return render(request, "myapp/login.html",context)

def logout(request):
     if "email" in request.session:
         del request.session["email"]
         return render(request, "myapp/login.html")
     else:
         return render(request, "myapp/login.html")


def register(request):
     if request.POST:
         email = request.POST['email']
         password = request.POST['password']
        

         uid = User.objects.create(email=email,
                                   password=password,
                                
                                 )
         context ={

            'uid' : uid

         }

         return render(request, "myapp/register.html",context)
     else:
         return render(request, "myapp/register.html")


def forget_password(request):
    
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1111, 9999)
        try: 
            uid=User.objects.get(email=email) 
            uid.otp=otp                                                                                     
            uid.save()
            send_mail("forgot password","your otp is"+str(otp),"gohiljayb10@gmail.com",[email])
            context={
                
                "email":email, 
            }
            return render(request,'myapp/comefrom_password.html',context) 
        except:
            contaxt={
                'emsg':"invalid email"
            }    
            return render(request,'myapp/forget_password.html',contaxt)        
    return render(request,'myapp/forget_password.html')        


def comefrom_password(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        comefrom_password=request.POST['comefrom_password']
     
        uid=User.objects.get(email=email)
        if str(uid.otp)==otp:
            
            if new_password == comefrom_password:
                uid.password = new_password
                uid.save()
                context={
                    'email':email,
                    'uid':uid,
                    'smsg':'password Successfully Changed'
                }
                return render(request,'myapp/login.html',context)
            else:
                context={
                    'email':email,
                    'emsg':'invalid password'
                }
                return render(request,'myapp/comefrom_password.html',context)
        else:
            context={
                    'email':email,
                    'emsg':'invalid otp'
                }
            return render(request,'myapp/comefrom_password.html',context)
    else:
        return render(request,'myapp/comefrom_password.html')   


def contact(request):
    lid = Add_to_cart.objects.all().count()
    context ={
        'lid' : lid
    }
    return render(request, "myapp/contact.html",context)


def blog_details(request):
    lid = Add_to_cart.objects.all().count()
    context ={

        'lid' : lid

    }
    return render(request, "myapp/blog_details.html",context)

def blog(request):    
    lid = Add_to_cart.objects.all().count()
    context ={
        'lid' : lid
    }
    return render(request, "myapp/blog.html",context)


def single_product(request):
    lid = Add_to_cart.objects.all().count()


    pid = Add_product.objects.all()

    context ={
        
        'pid' : pid,
        'lid' : lid,
    }
    return render(request, "myapp/single_product.html",context)




def shoping_cart(request):

    cid = Add_to_cart.objects.all()
    prod = Add_to_cart.objects.all()
    lid = Add_to_cart.objects.all().count()
   
    list1=[]
    sub_total=0
    total = 1
    for x in prod:
        z=x.price * x.quantuty
        list1.append(z)
        sub_total = sum(list1)
        total = sub_total + 50

    context ={

        'cid' : cid,
        'lid' : lid,
        'sub_total' : sub_total,
        'total' : total
 
    }
    return render(request, "myapp/shoping_cart.html",context)



def add_to_cart(request,id):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
    

        pid = Add_product.objects.get(id=id)
        Add_to_cart.objects.create(user_id=uid,
                                   product_id = pid,
                                   pic = pid.pic,
                                   price=pid.price,
                                   name=pid.name,
                                   total_price=pid.quantuty *pid.price        
        )

        return redirect("shoping_cart")


def puls(request,id):

    pid = Add_to_cart.objects.get(id=id)

    if pid:
        pid.quantuty = pid.quantuty+1
        pid.total_price = pid.quantuty * pid.price
        pid.save()
        
        return redirect("shoping_cart")

def manus(request,id):

    pid = Add_to_cart.objects.get(id=id)
    if pid.quantuty == 1:
        pid.delete()
        return redirect("shoping_cart") 

    else:
        if pid:
            pid.quantuty = pid.quantuty-1
            pid.total_price = pid.quantuty * pid.price
            pid.save()
            
            return redirect("shoping_cart")

def remov(request,id):
    rid = Add_to_cart.objects.get(id=id)
    rid.delete()
    return redirect("shoping_cart")


def checkout(request):
    prod = Add_to_cart.objects.all()
    lid = Add_to_cart.objects.all().count()
   
   
    list1=[]
    sub_total=0
    total = 1
    for x in prod:
        z=x.price * x.quantuty
        list1.append(z)
        sub_total = sum(list1)
        total = sub_total + 50
       
    amount = total*100 
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({

                                    'amount':amount,
                                   'currency':'INR',
                                   'payment_capture':1

    
    })
    print(response,"****************************************")
   
    con = {
            'prod':prod,
            'sub_total':sub_total,
            'total':total,
            'response':response,
            "lid" : lid
            
    }
   
    
    return render(request, "myapp/checkout.html",con)


def shop_details(request,id):
    
    
    pid = Add_product.objects.filter(id=id)
    


    context ={
        'pid' : pid
    }
    return render(request, "myapp/shop_details.html",context)

    
def address(request):
    uid = User.objects.get(email=request.session['email'])
    
    if request.POST:
        fist_name = request.POST['fist_name']
        last_name =request.POST['last_name']
        country = request.POST['country']
        Saddress = request.POST['Saddress']
        Aaddress = request.POST['Aaddress']
        town_city = request.POST['town_city']
        Country_State = request.POST['Country_State']
        phon = request.POST['phon']
        email = request.POST['email']


        aid = Address.objects.create(user_id=uid,
                                     fist_name=fist_name,
                                     last_name= last_name,
                                     country=country,
                                     Saddress=Saddress,
                                     Aaddress= Aaddress,
                                     town_city=town_city,
                                     Country_State=Country_State,
                                     phon=phon,
                                     email=email 
        
        )

        # context ={

        #     'uid' : uid,
        #     'sid' : "Address add sussesfull........."

        # }

        return redirect("checkout")

    else:

        return redirect("checkout")

def searchview(request):
    srch = request.GET["srch"]
    if srch:
        pid = Add_product.objects.filter(name__contains=srch)
    contaxt={
        'pid':pid
    }    
    return render(request,"myapp/shop_details.html",contaxt)



