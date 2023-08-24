from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    # 在这里实现 增删改查

    return HttpResponse('index')

########################新增数据############################3
from book.models import BookInfo
# 方法1
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 方法2
BookInfo.objects.create(
    name='Flask',
    pub_date='2001-1-1',
    readcount=12
)

#################修改数据#######################
# 1.方法1
book = BookInfo.objects.get(id=6)
book.name = 'Javascript'
book.save()

# 2.方法2
BookInfo.objects.filter(id=6).update(name='Ruby', commentcount=66)


