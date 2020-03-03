# Generated by Django 2.1.8 on 2020-02-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20200215_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='answers',
            field=models.ManyToManyField(to='survey.Answer', verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='question',
            name='status_extra',
            field=models.IntegerField(choices=[(1, '是'), (0, '否')], default=0, help_text='默认否，设置为是时，题目会生成一个【其他】的自定义选项', verbose_name='其他回答设置'),
        ),
    ]