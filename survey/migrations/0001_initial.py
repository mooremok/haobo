# Generated by Django 2.1.8 on 2020-02-14 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_answer', models.CharField(max_length=255, verbose_name='请填写答案')),
            ],
            options={
                'verbose_name': '答案',
                'verbose_name_plural': '答案',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='请填写问题')),
                ('other_question', models.CharField(blank=True, help_text='用来给客户做自定义回答，请勿填写', max_length=255, null=True, verbose_name='其他')),
                ('status', models.BooleanField(choices=[(1, '单选'), (2, '多选')], default=2, help_text='默认多选，没啥事不要选择单选', verbose_name='类型（多选或单选）')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='填写人姓名')),
                ('company', models.CharField(max_length=50, verbose_name='公司名称')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('record', models.ManyToManyField(to='survey.Question', verbose_name='所有问题')),
            ],
            options={
                'verbose_name': '调研记录表',
                'verbose_name_plural': '调研记录表',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='an_for_question', to='survey.Question'),
        ),
    ]
