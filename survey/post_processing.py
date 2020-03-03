def querydict_to_list(post_data):
    """处理model.Poll中post的数据，将QueryDict.lists处理的可迭代对象变成列表"""
    data_list = []    
    for i in post_data:
        data_list.append(i)
    return data_list

def get_all_datas(data_list):
    """组织组织data_list，按照record的字段返回对应的字典，用来save"""
    name = ''
    company = ''
    answer_preset = []
    answer_extra = []
    answer_other = []
    for record in data_list:
        if 'name' in record[0]:
            name = record[1][0]
        elif 'company' in record[0]:
            company = record[1][0]
        elif 'status_choice' in record[0]:
            answer_preset.append(record)
        elif 'status_extra' in record[0]:
            x = [record[0], record[1][-1]]
            answer_other.append(x)
        elif 'status_source' in record[0]:
            answer_extra.append(record)

    return {
        'name': name,
        'company': company,
        'answer_preset': answer_preset,
        'answer_extra': answer_extra,
        'answer_other': answer_other,
    }




    

