from django.shortcuts import render
from . models import Question, Answer, Record
from django.http import HttpResponseRedirect
# Create your views here.

def poll(request):
    if request.method == "GET":
        all_data = Question.objects.filter(display_set=0)
        #这部分的逻辑与product.views的逻辑一致，皆为将数据打包成一个自定义的数据模型[{问题： 答案}, ...]
        all_data_list = []
        for data in all_data:            
            q_and_a = {data: data.an_for_question.all()}
            all_data_list.append(q_and_a)

        context = {
            'all_data': all_data,
            'all_data_list': all_data_list,
        }
        return render(request, 'survey/poll.html', context)
    
    if request.method == "POST":
        """
        1、HttpRequest是一个特殊的QueryDict对象，类似于个Queryset，里面的元素均为字典，<QueryDict[dict1, dict2...]> 
        由于客户端中的input使用了无法确定的name，所以这里没办法使用request.POST.get/getlist来获取数据
        故，使用request.POST来获取QueryDict,然后遍历处理

        2、QueryDict.lists()返回的是一个可迭代对象（即下方的post_data），遍历后处理成列表（即下方的data_list）：
        [('csrfmiddlewaretoken', ['2sHuGsEvRd9vAwJTcS21Mg2TsjEnRZD24bVoiHrA8HSPxF6s0VDXuMVyurbbey8s']), ('name', ['金圣运']), ('company', ['浩博广告有限公司']), ('status_choice-4', ['16']), ('status_extra-4', ['4', '发发发']), ('status_choice-5', ['10', '19', '20']), ('status_extra-5', ['5', '发发fffaaa']), ('status_source-6', ['反反复复大所付大付大']), ('status_choice-7', ['13']), ('status_extra-7', [''])]

        3、上方返回的数据比较复杂，直接写入Record的answers字段中，admin中再处理成可视化的数据渲染出来
        """        
        from . import post_processing
        post_data = request.POST.lists()
        #引用post_processing模块对post_data进行处理
        data_list = post_processing.querydict_to_list(post_data)
        dicts = post_processing.get_all_datas(data_list)
        Record.objects.create(**dicts)
        dicts['data_list'] = data_list
        return HttpResponseRedirect('done')

def result(request):
    context = {
        'result': '提交成功',
    }
    return render(request, 'survey/result.html', context)