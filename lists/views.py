from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item
# Create your views here.
def home_page(request):
    if request.method =='POST':
        new_item_text= request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text=''
    # item =Item()
    # item.text = request.POST.get('id_new_item','')
    # item.save()
    #return render(request,'home.html',{'new_item_text':request.POST.get('id_new_item','')})
    return render(request,'home.html',{'new_item_text':new_item_text})




user_list=[]
def index(request):
    if request.method =="POST":
        username= request.POST.get("username",None)
        password =request.POST.get("password",None)
        temp= {"user": username,"pwd":password}
        user_list.append(
            temp
        )

    return render(request,'index.html',{"data":user_list})