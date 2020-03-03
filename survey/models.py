from django.db import models

# Create your models here.

class Question(models.Model):
    """
    1、Question作为Answer的外键，配合TabularInline能在admin中实现创建问题时，连带创建问题对应的答案；
    2、status_choice：控制问题的答案时预设的（即后台中设置好的）还是由客户端输入；
    3、status_extra：控制问题在显示完所有答案后，是否再显示一个“其他”选项；
    4、display_set：控制问题是否生效，隐藏或显示。
    """
    CHOICE_TYPE = [
        (1, '单选'),
        (0, '多选'),
    ]
    ANSWER_SHORCE = [
        (0, '预设答案'),
        (1, '客户自定义'),
    ]
    ANSWER_EXTRA = [
        (1, '是'),
        (0, '否'),
    ]
    DISPLAY_STATUS = [
        (0, '显示'),
        (1, '隐藏'),
    ]
    question = models.CharField(max_length=255, verbose_name="请填写问题")
    other_question = models.CharField(max_length=255, help_text="用来给客户做自定义回答，请勿填写", verbose_name="其他", 
                                        null=True, blank=True)
    status_choice = models.IntegerField(default=0, choices=CHOICE_TYPE, verbose_name="类型设置", help_text="默认多选，没啥事不要选择单选")
    status_source = models.IntegerField(default=0, choices=ANSWER_SHORCE, verbose_name="预设答案设置", help_text="默认预设，一道题中需要客户全部自定义回答时请选择【客户自定义答案】，并且下方答案不要设置")
    status_extra = models.IntegerField(default=0, choices=ANSWER_EXTRA, verbose_name="其他回答设置", help_text="默认否，设置为是时，题目会生成一个【其他】的自定义选项")
    display_set = models.IntegerField(default=0, choices=DISPLAY_STATUS, verbose_name='显示设置', help_text="默认显示，设置隐藏时客户将看不到这道题")

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = verbose_name_plural = "问题"

class Answer(models.Model):
    cn_answer = models.CharField(max_length=255, verbose_name="预设答案")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="an_for_question", verbose_name="所属问题")

    def __str__(self):
        return self.cn_answer
    
    class Meta:
        verbose_name = verbose_name_plural = "答案"



class Record(models.Model):
    """这里关于answer所有的field都要重写，使用自定义Field完成，即把数据组织成列表转换成字符写入，读取的时候转换成python对象 """
    name = models.CharField(max_length=20, verbose_name="填写人姓名")
    company = models.CharField(max_length=50, verbose_name="公司名称")
    questions = models.ManyToManyField(Question, verbose_name="所有问题")
    answer_preset = models.TextField(max_length=1024, verbose_name="答案", help_text="由客户提交，无须填写")
    answer_extra = models.TextField(max_length=1024, verbose_name="自定义回答", null=True, blank=True, help_text="由客户提交，无须填写")
    answer_other = models.TextField(max_length=1024, verbose_name="其他回答", null=True, blank=True, help_text="由客户提交，无须填写")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")

    def __str__(self):
        return self.company
    
    class Meta:
        verbose_name = verbose_name_plural = "调研记录表"
    