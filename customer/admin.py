from django.contrib import admin
from . models import Customer

from django.utils.html import format_html, html_safe
from django.template.response import TemplateResponse
from django.urls import path

from . admin_get_detail import (
    get_con_detail, get_des_detail, get_market_detail, get_implement_detail
)

from production.cost import total_cost

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'position', 'address', 'contact','cost', 'created_time', 'detail']
    filter_horizontal = ['consultation', 'design', 'marketing', 'implement']
    
    def get_urls(self):
        """
        1、get_urls()方法专处理admin中的request且需新增自定义功能；
        2、本质上是处理request及response，在admin中需要重写get_urls()后，需自定义views，并且必须以TemplateResponse方式返回数据；
        3、需用self.admin_site.admin_view来校验url的权限(传入自定义的view即可)，以防止不登录或权限以外的账号查看。
        """
        urls = super().get_urls()
        show_products_detail = [
            path('<cus_id>/show_detail', self.admin_site.admin_view(self.customer_products), name="show_detail"),
        ]
        return show_products_detail + urls

    def customer_products(self, request, cus_id):
        """
        自定义view，查看的是客户提交产品服务的详情，admin中无友好的查看方式
        """
        current_customer = Customer.objects.get(id=cus_id)

        #consultation的所有产品(返回一个自定义的数据类型，请阅读get_con_detail方法)
        consultations = get_con_detail(current_customer)
        #design的所有产品(返回一个自定义的数据类型，请阅读get_des_detail方法)
        designs = get_des_detail(current_customer)
        #marketing的所有产品，返回常规queryset
        markets = get_market_detail(current_customer)
        #implement的所有产品，返回常规queryset
        imps = get_implement_detail(current_customer)

        context = dict(
            self.admin_site.each_context(request),
            consultations = consultations,
            designs = designs,
            markets = markets,
            imps = imps,
            company = current_customer.company,
        )
        return TemplateResponse(request, 'customer/modal.html', context)
 
    def detail(self, obj):
        obj_id = obj.id        
        return format_html('<a href="{}/{}">查看</a>',
            obj_id,
            'show_detail',
        )
    detail.short_description = "产品详情"

    #重写save_model，实现后台自建实例、修改实例（包含客户端提交的实例）时，自动计算总费用并写入cost字段；
    #此处调用的费用计算模块total_cost()与客户端提交时调用的为同一模块
    def save_model(self, request, obj, form, change):
        con_list = request.POST.getlist('consultation')
        design_list = request.POST.getlist('design')
        markets_list = request.POST.getlist('marketing')
        imps_list = request.POST.getlist('implement')
        obj.cost = total_cost(con_list, design_list, markets_list, imps_list)

        super().save_model(request, obj, form, change)
    """
    class Media:
        js = ('/static/js/demo.js', '/static/js/bootstrap.js', '/static/js/jquery3.4.1.js')
        #css = {"all": ('/static/css/bootstrap.css',)}
    """ 
        