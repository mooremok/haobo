# Generated by Django 2.1.8 on 2020-02-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20200216_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='extra_answer',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='自定义答案'),
        ),
        migrations.AddField(
            model_name='record',
            name='other_answer',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='其他答案'),
        ),
    ]