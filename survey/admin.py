from django.contrib import admin
from . models import (
    Question,
    Answer,
    Record,
)
from . models import Record
from django.urls import path
from django.template.response import TemplateResponse
from django.utils.html import format_html

class Question_Answer(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'status_choice', 'status_source', 'display_set', 'status_extra']
    inlines = [Question_Answer]
    fields = ('question', 'status_choice', 'display_set', 'status_extra', 'status_source')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'show_record_btn', 'created_time']

    def get_urls(self):
        """重写get_urls方法实现查看调研表详情"""
        urls = super().get_urls()
        show_record_detail = [
            path('<record_id>/show_detail', self.admin_site.admin_view(self.show_record), name="show_record"),
        ]
        return show_record_detail + urls
    
    def show_record(self, request, record_id):
        from . admin_show_detail import get_detail

        records = Record.objects.get(id=record_id)
        all_datas = get_detail(records)
        context = {
            'all_datas': all_datas,
        }
        return TemplateResponse(request, 'survey/record.html', context)
    
    def show_record_btn(self, obj):
        obj_id = obj.id
        return format_html('<a href="{}/{}">查看</a>',
            obj_id,
            'show_detail',
        )
    show_record_btn.short_description = "调研详情"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['cn_answer', 'question']