from .models import Customer
from production.models import CateForCon, CateForDesign, Consultation, Design

def get_con_detail(current_customer):
    """
    通过实例ID获取一个自定义的数据模型[{咨询分类: [该分类的所有产品]}]，列表中嵌套了字典，字典的value值为列表
    这个自定义数据模型只有cousulation和design才会有，marketing & implement两个产品model是没有分类外键的
    """
    #获取当前的实例
    consultations = current_customer.consultation.all()

    #获取实例中所有分类的id并去重处理
    cate_for_con = []
    for con in consultations:
        cate_for_con.append(con.category.id)
        cate_for_con = list(set(cate_for_con))
    #使用实例分类的id，组成自定义数据模型[{咨询分类: [该分类的所有产品]}]，列表中嵌套了字典，字典的value值为列表
    all_cons = []    
    for cate in cate_for_con:
        con_final = []
        cons_filter = Consultation.objects.filter(category__id=cate)        
        for cons in cons_filter:
            if cons in consultations:
                con_final.append(cons)
        all_cons.append({CateForCon.objects.get(id=cate): con_final})
          
    return all_cons

def get_des_detail(current_customer):
    """函数的目的及处理的逻辑与get_con_detail一致"""
    designs = current_customer.design.all()

    #获取实例中所有分类id并去重处理
    cate_for_des = []    
    for des in designs:
        cate_for_des.append(des.category.id)
        cate_for_des = list(set(cate_for_des))

    #使用实例分类的id，组成自定义数据模型[{设计分类: [该分类的所有产品]}]，列表中嵌套了字典，字典的value值为列表 
    all_designs = []
    for cate in cate_for_des:
        des_final = []
        des_filter = Design.objects.filter(category__id=cate)
        for des in des_filter:
            if des in designs:
                des_final.append(des)
        all_designs.append({CateForDesign.objects.get(id=cate): des_final})
    
    return all_designs


def get_market_detail(current_customer):
    markets = current_customer.marketing.all()
    return markets

def get_implement_detail(current_customer):
    imps = current_customer.implement.all()
    return imps




