from django.db import models
from production.models import (
    Consultation,
    Design,
    Marketing,
    Implementation
)

class Customer(models.Model):
    name = models.CharField(max_length=20, verbose_name='填写人姓名')
    company = models.CharField(max_length=100, verbose_name='公司名称')
    position = models.CharField(max_length=50, verbose_name='填写人职位')
    contact = models.CharField(max_length=20, verbose_name='联系电话')
    address = models.CharField(max_length=200, verbose_name='公司地址')
    consultation = models.ManyToManyField(Consultation, verbose_name='咨询产品', null=True, blank=True)
    design = models.ManyToManyField(Design, verbose_name='设计产品', null=True, blank=True)
    marketing = models.ManyToManyField(Marketing, verbose_name='营销产品', null=True, blank=True)
    implement = models.ManyToManyField(Implementation, verbose_name='落地产品', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')
    cost = models.PositiveIntegerField(default=0, verbose_name='总费用')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '客户选择表'
