from django.shortcuts import render
from customer.admin import CustomerAdmin
from . models import Customer

# Create your views here.
def result(request):
    #product_list = CustomerAdmin.product_list(CustomerAdmin,Customer)
    context = {
        'result': '注册成功',
    }
    return render(request, 'customer/result.html', context)