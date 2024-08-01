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
        lid = Add_to_cart.objects.filter(user_id=uid).count()
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
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    context ={
        
        'lid' : lid
    }
    return render(request, "myapp/contact.html",context)


def blog_details(request):
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    context ={

        'lid' : lid
    }
    return render(request, "myapp/blog_details.html",context)

def blog(request):   
    uid = User.objects.get(email=request.session['email']) 
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    context ={
        'lid' : lid
    }
    return render(request, "myapp/blog.html",context)


def single_product(request):
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    mid = maincatagory.objects.all()


    pid = Add_product.objects.all()

    context ={
        
        'pid' : pid,
        'lid' : lid,
        'mid' : mid
    }
    return render(request, "myapp/single_product.html",context)




def shop_details(request,id):
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    pid = Add_product.objects.filter(id=id)
    
    context ={
        'pid' : pid,
        'lid' : lid
    }
    return render(request, "myapp/shop_details.html",context)

def add_to_cart(request,id):

    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = Add_product.objects.get(id=id)
        pcid = Add_to_cart.objects.filter(product_id=pid,user_id=uid).exists()

        if pcid:
            pcid = Add_to_cart.objects.get(product_id=pid)
            pcid.quantuty = pcid.quantuty+1
            pcid.total_price = pcid.quantuty * pcid.price
            pcid.save()
            
            return redirect("shoping_cart")
    
        else:
            Add_to_cart.objects.create(user_id=uid,
                                    product_id = pid,
                                    pic = pid.pic,
                                    price=pid.price,
                                    name=pid.name,
                                    total_price=pid.quantuty *pid.price        
            )

            return redirect("shoping_cart")
    else:
        return redirect("shoping_cart")
        
        


def shoping_cart(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Add_to_cart.objects.filter(user_id=uid)
    prod = Add_to_cart.objects.filter(user_id=uid)
    lid = Add_to_cart.objects.filter(user_id=uid).count()
   
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
    uid = User.objects.get(email = request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    ctid = Add_to_cart.objects.filter()
    prod = Add_to_cart.objects.filter(user_id=uid)

    list1 = []
    sub_total = 0
    total = 1
    
    try:
        for i in prod:
            z = i.price * i.quantuty
            list1.append(z)
            a = sum(list1)
        sub_total = sub_total + a 
        total = sub_total + 50
            
        amount = total*100 
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({

                                        'amount':amount,
                                    'currency':'INR',
                                    'payment_capture':1
        
        })
            
        con = {
            'lid' : lid,
            'ctid' : ctid,
            'prod' : prod,
            'response' : response,
            'total' : total,
            'sub_total' : sub_total
        }
        for i in prod:
            print("-----------------------------",i)
            Order.objects.create(user_id = uid,
                                name = i.name,
                                qty = i.quantuty,
                                price = i.price)
        
        return render(request,"myapp/checkout.html",con)

    except:
        amount = total*100 
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({

                                        'amount':amount,
                                    'currency':'INR',
                                    'payment_capture':1
        
        })
        
        con = {
            'lid' : lid,
            'ctid' : ctid,
            'prod' : prod,
            'total' : total,
            'response' : response,
            'sub_total' : sub_total
        }
        
        return render(request,"myapp/checkout.html",con)

def order(request):
    uid = User.objects.get(email = request.session['email'])
    oid = Order.objects.filter(user_id=uid)
    aid = Address.objects.filter(user_id=uid)
    did = Add_to_cart.objects.all().delete()
    
    con = {
        'oid' : oid,
        'aid' : aid,
    }
    return render(request,"myapp/order.html",con)     


def billing_address(request):
    
    try:
        uid = User.objects.get(email = request.session['email'])
        lid = Add_to_cart.objects.filter(user_id=uid).count()
        ctid = Add_to_cart.objects.filter()
        aid = Address.objects.filter(user_id=uid).exists()
        add_list = Address.objects.get(user_id=uid)
        
        print(uid,aid,"---------------------")
        if aid:
            lid = Add_to_cart.objects.all()   
            l1 = []
            for i in lid:
                    
                l1.append(f"product name = {i.name} price = {i.price} quantuty = {i.quantuty} total_price = {i.total_price}......")
                
            add_list.list = l1 
            add_list.save()   
            return redirect('checkout')
    
    except:
    
        if request.POST:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user_name = request.POST['user_name']
            email = request.POST['email']
            address = request.POST['address']
            address_2 = request.POST['address_2']
            country = request.POST['country']
            state = request.POST['state']
            pincode = request.POST['pincode']
            
            uid = Address.objects.create(user_id=uid,
                                        first_name=first_name,
                                        last_name=last_name,
                                        user_name=user_name,
                                        email=email,
                                        address=address,
                                        address_2=address_2,
                                        country=country,
                                        state=state,
                                        pincode=pincode)
            
            lid = Add_to_cart.objects.all()
            
            l1 = []
            for i in lid:
                
                l1.append(f"product name = {i.name} price = {i.price} quantuty = {i.quantuty} total_price = {i.total_price}......")
            
            
            uid.list = l1 
            uid.save()   
            return redirect('checkout')

        else:    
            con = {
                'lid' : lid,
                'ctid' : ctid
            }
        
            return render(request,"myapp/billing_address.html",con)
    
 
def delete_address(request):
    uid = User.objects.get(email = request.session['email'])
    try:
        did = Address.objects.get(user_id=uid).delete()
    
        return redirect('billing_address')    
    except:    
        return render(request,"myapp/billing_address.html")
            

def searchview(request):
    srch = request.GET["srch"]
    if srch:
        pid = Add_product.objects.filter(name__contains=srch)
    contaxt={
        'pid':pid
    }    
    return render(request,"myapp/shop_details.html",contaxt)

def category(request,id):
    
    mid = Add_product.objects.filter(main_id = id)
    
    context = {
        'mid' : mid
    }
    return render(request,"myapp/category.html",context)
