from production import models

def total_cost(con_list, design_list, markets_list, imps_list):
    """
    本模块功能：
    1、客户端提交选择表单时，调用该方法计算总费用；
    2、后台add、change客户选择表时，调用该方法计算、重新计算总费用。
    """
    cost_list = []
    con_total = 0
    des_total = 0
    mar_total = 0
    imp_total = 0
    total = 0

    if con_list:
        for con in con_list:
            con_price = models.Consultation.objects.get(id=con).price
            con_total += int(con_price)
    
    cost_list.append(con_total)

    if design_list:
        for des in design_list:
            des_price = models.Design.objects.get(id=des).price
            des_total += int(des_price)

    cost_list.append(des_total)

    if markets_list:
        for markets in markets_list:
            mar_price = models.Marketing.objects.get(id=markets).price
            mar_total += int(mar_price)
    
    cost_list.append(mar_total)

    if imps_list:
        for imps in imps_list:
            imp_price = models.Implementation.objects.get(id=imps).price
            imp_total += int(imp_price)
    
    cost_list.append(imp_total)

    for cost in cost_list:
        total += cost
    
    return total