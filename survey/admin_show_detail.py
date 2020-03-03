from . import models

def get_detail(records):
    """处理客户端提交的问题与答案的数据，返回元素为元祖的列表 [{问题： [答案1，答案2，答案3..]}, ...]"""
    #由于models.Record中的三个answer的字段使用的CharField保存数据，这里使用eval可智能化地把CharField转化为python对象即列表
    answer_preset = eval(records.answer_preset)
    answer_extra = eval(records.answer_extra)
    answer_other = eval(records.answer_other)
    
    #组织answer_prest的问题和答案
    question_answer = []
    for preset in answer_preset:
        q_and_a_prest = {}
        question_id = preset[0].split('-')[1]
        question = models.Question.objects.get(id=question_id).question

        answers = []
        for answer_id in preset[1]:            
            answer = models.Answer.objects.get(id=answer_id).cn_answer
            answers.append(answer)  
        q_and_a_prest[question] = answers
        question_answer.append(q_and_a_prest)
    
    #将answer_extra组织到question_answer中
    for extra in answer_extra:
        q_and_a_extra = {}
        question_id = extra[0].split('-')[1]
        question = models.Question.objects.get(id=question_id).question
        q_and_a_extra[question] = extra[1]
        question_answer.append(q_and_a_extra)
    
    #将answer_other组织到question_answer中
    for other in answer_other:
        question_id = other[0].split('-')[1]
        question = models.Question.objects.get(id=question_id).question
        for tup in question_answer:
            for key, value in tup.items():
                if question == key:
                    value.append(other[1])

    return question_answer