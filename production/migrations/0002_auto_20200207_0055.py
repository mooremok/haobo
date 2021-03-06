# Generated by Django 2.1.8 on 2020-02-06 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='con_category', to='production.CateForCon', verbose_name='所属分类'),
        ),
        migrations.AlterField(
            model_name='design',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='des_category', to='production.CateForDesign', verbose_name='所属分类'),
        ),
    ]
