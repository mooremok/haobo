# Generated by Django 2.1.8 on 2020-02-06 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateForCon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '咨询产品分类设置',
                'verbose_name_plural': '咨询产品分类设置',
            },
        ),
        migrations.CreateModel(
            name='CateForDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '设计产品分类设置',
                'verbose_name_plural': '设计产品分类设置',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('status', models.BooleanField(choices=[(1, '显示'), (0, '隐藏')], default=1, verbose_name='产品状态')),
                ('price', models.IntegerField(default=0, verbose_name='产品价格')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='产品说明')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='production.CateForCon', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '1_咨询类产品',
                'verbose_name_plural': '1_咨询类产品',
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('status', models.BooleanField(choices=[(1, '显示'), (0, '隐藏')], default=1, verbose_name='产品状态')),
                ('price', models.IntegerField(default=0, verbose_name='产品价格')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='产品说明')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='production.CateForDesign', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '2_设计类产品',
                'verbose_name_plural': '2_设计类产品',
            },
        ),
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('status', models.BooleanField(choices=[(1, '显示'), (0, '隐藏')], default=1, verbose_name='产品状态')),
                ('price', models.IntegerField(default=0, verbose_name='产品价格')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='产品说明')),
            ],
            options={
                'verbose_name': '4_落地类产品',
                'verbose_name_plural': '4_落地类产品',
            },
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='产品名称')),
                ('status', models.BooleanField(choices=[(1, '显示'), (0, '隐藏')], default=1, verbose_name='产品状态')),
                ('price', models.IntegerField(default=0, verbose_name='产品价格')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='产品说明')),
            ],
            options={
                'verbose_name': '3_营销类产品',
                'verbose_name_plural': '3_营销类产品',
            },
        ),
    ]
