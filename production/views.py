from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import (
    CateForDesign, Design,
    CateForCon, Consultation,
    Marketing,
    Implementation
)

from customer.models import Customer
from .cost import total_cost

def home(request):
    """
    偷个懒，访问首页的view写在了这里
    """
    return render(request, 'index.html')

#处理产品服务挑选的request
def order(request):
    if request.method == "GET":
        """ 把所有的产品信息渲染到前端，产品被分成了4个model来实现的，所以有4个tontext对象，
            其中design和marketing两个产品有分类，所以这两个queryset放在了各自的分类model中实现
        """
        context = {
            'all_cons': CateForCon.get_all_cons(),
            'all_designs': CateForDesign.get_all_designs(),
            'all_markets': Marketing.get_all_markets(),
            'all_imps': Implementation.get_all_imps(),
        }
        return render(request, 'production/order.html', context)

    if request.method == "POST":
        """前端获取checkbox的所有信息，写入Customer中 """
        #获取填写人信息，get返回的是str，适合处理单个值
        post_name = request.POST.get('name', '')
        post_company = request.POST.get('company', '')
        post_position = request.POST.get('position', '')
        post_address = request.POST.get('address', '')
        post_contact = request.POST.get('contact', '')

        #从post中获取勾选的信息，getlist返回的是list，checkbox中带回的参数为各个产品的id-->用来获取产品queryset和计算总价格
        con_list = request.POST.getlist('con_list', '')        
        design_list = request.POST.getlist('design_list', '')
        markets_list = request.POST.getlist('markets_list', '')
        imps_list = request.POST.getlist('imps_list', '')

        #上面的list传入下方的方法中，用id获取所有产品，返回的是queryset-->用来写入到customer中
        all_cons = Consultation.get_by_post(con_list)
        all_designs = Design.get_by_post(design_list)
        all_markes = Marketing.get_by_post(markets_list)
        all_imps = Implementation.get_by_post(imps_list)

        #再用上方的ist计算产品总价格-->用来写入到customer中
        costs = total_cost(con_list, design_list, markets_list, imps_list)

        dic = {
            'name': post_name,
            'company': post_company,
            'position': post_position,
            'contact': post_company,
            'address': post_address,
            'cost': costs,
        }
        
        #ManyToManyField只能通过field_name.set()方法进行保存，且必须在创建实例之后
        save_all = Customer.objects.create(**dic)
        save_all.consultation.set(all_cons)
        save_all.design.set(all_designs)
        save_all.marketing.set(all_markes)
        save_all.implement.set(all_imps)

        return HttpResponseRedirect('done')


