import csv
from django.http import HttpResponse

#本模块专放置admin共有的自定义actions
def export_as_csv_action(description='导出表格', fields=None, exclude=None, header=True):
    """
    本方法返回一个export_as_csv的方法
    param fields & param exclude 的作用如同ModelForm的开头的设置    
    """
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        if not fields:
            field_names = [field for field in opts]
        else:
            field_names = fields
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Dispositon'] = 'attachment; filename={}.csv'.format(opts.verbose_name.encode('utf-8'))
        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]
            writer.writerow(row)
        return response
    export_as_csv.short_description = description
    return export_as_csv
        