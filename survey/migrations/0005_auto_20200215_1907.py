# Generated by Django 2.1.8 on 2020-02-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20200214_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='cn_answer',
            field=models.CharField(max_length=255, verbose_name='预设答案'),
        ),
        migrations.AlterField(
            model_name='question',
            name='display_set',
            field=models.IntegerField(choices=[(0, '显示'), (1, '隐藏')], default=0, help_text='默认显示，设置隐藏时客户将看不到这道题', verbose_name='显示设置'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status_choice',
            field=models.IntegerField(choices=[(1, '单选'), (0, '多选')], default=0, help_text='默认多选，没啥事不要选择单选', verbose_name='类型设置'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status_extra',
            field=models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, help_text='默认否，设置为是时，题目会生成一个【其他】的自定义选项', verbose_name='置额外回答设置'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status_source',
            field=models.IntegerField(choices=[(0, '预设答案'), (1, '客户自定义')], default=0, help_text='默认预设，一道题中需要客户全部自定义回答时请选择【客户自定义答案】，并且下方答案不要设置', verbose_name='预设答案设置'),
        ),
    ]
