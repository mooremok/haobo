from django.db import models

# Create your models here.
class CateForDesign(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '设计产品分类设置'
    
    @classmethod
    def get_all_designs(cls):
        """获取设计分类及分类下所有产品
            这个数据被组合成了字典，格式：{catefordesign：[分类下所有产品]}
            为了前端更好地展示产品
        """
        catefordesign = cls.objects.all()
        all_designs = []
        for cate in catefordesign:
            designs = cls.objects.get(id=cate.id).des_category.filter(status=1)
            cate_name = cls.name
            cate_des_dict = {cate.name: designs}
            all_designs.append(cate_des_dict)        
        return all_designs


class CateForCon(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '咨询产品分类设置'
            
    @classmethod
    def get_all_cons(cls):
        """#获取咨询分类及分类下所有产品"""
        cateforcon = cls.objects.all()
        all_cons = []
        for cate in cateforcon:
            cons = cls.objects.get(id=cate.id).con_category.filter(status=1)
            cate_name = cls.name
            cate_con_dict = {cate.name: cons}
            all_cons.append(cate_con_dict)        
        return all_cons

    
#把产品类型的model共有的字段抽象基类
class CommenInfo(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDDEN = 0
    STATUS_CODE = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDDEN, '隐藏'),
    )

    name = models.CharField(max_length=100, verbose_name='产品名称')    
    status = models.BooleanField(default=STATUS_SHOW, choices=STATUS_CODE, verbose_name="产品状态")
    price = models.IntegerField(default=0, verbose_name='产品价格')
    desc = models.TextField(null=True ,blank=True, verbose_name='产品说明')

    def __str__(self):
        return self.name
    
    class Meta:
        abstract=True


#咨询类产品有分类，所以继承基类时加个category的foreignkey
class Consultation(CommenInfo):
    category = models.ForeignKey(CateForCon, on_delete=models.DO_NOTHING, verbose_name='所属分类', related_name='con_category')
    
    class Meta:
        verbose_name = verbose_name_plural = '1_咨询类产品'
    
    @staticmethod
    def get_by_post(con_list):
        return Consultation.objects.filter(id__in=con_list)


#设计类产品有分类，所以继承基类时加个category的foreignkey
class Design(CommenInfo):
    category = models.ForeignKey(CateForDesign, on_delete=models.DO_NOTHING, verbose_name='所属分类', related_name='des_category')
    
    class Meta:
        verbose_name = verbose_name_plural = '2_设计类产品'
    
    @staticmethod
    def get_by_post(design_list):
        return Design.objects.filter(id__in=design_list)

    

#营销类产品
class Marketing(CommenInfo):    
    class Meta:
        verbose_name = verbose_name_plural = '3_营销类产品'

    @classmethod
    def get_all_markets(cls):
        return cls.objects.filter(status=1)
    
    @staticmethod
    def get_by_post(markets_list):
        return Marketing.objects.filter(id__in=markets_list)

#落地类产品
class Implementation(CommenInfo):
    class Meta:
        verbose_name = verbose_name_plural = '4_落地类产品'

    @classmethod
    def get_all_imps(cls):
        return cls.objects.filter(status=1)
    
    @staticmethod
    def get_by_post(imps_list):
        return Implementation.objects.filter(id__in=imps_list)
        #return Implementation.objects.filter(id__in=[1,2,3])