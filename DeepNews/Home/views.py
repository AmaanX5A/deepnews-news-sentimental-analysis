from django.shortcuts import render
from Home.models import bbc,cnn,sky,article
from django.db.models import Q
from django.template.loader import render_to_string
from itertools import chain
from django.http import HttpResponse
from operator import attrgetter
from django.shortcuts import render_to_response
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

def index(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        SKY = sky.objects.filter(headline__contains=query)
        CNN = cnn.objects.filter(headline__contains=query)
        BBC = bbc.objects.filter(headline__contains=query)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/index.html',data)
    data = {}
    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    print("arha")
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/HOME.html',data)
def LATEST(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        SKY = sky.objects.filter(headline__contains=query)
        CNN = cnn.objects.filter(headline__contains=query)
        BBC = bbc.objects.filter(headline__contains=query)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        newlist=newlist[0:6]
        print(list(newlist))

        data["articles"] = newlist

        return render(request,'DeepNews/LATEST.html',data)
    print("latest")
    data = {}
    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:6]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/LATEST.html',data)
def HOME(request):
    data = {}
    query = request.GET.get('search')
    if query:

        print(query)
        SKY = sky.objects.filter(headline__contains=query)
        CNN = cnn.objects.filter(headline__contains=query)
        BBC = bbc.objects.filter(headline__contains=query)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1

        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/index.html',data)

    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:29]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1


    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/Home.html',data)
def POS(request):
    data = {}
    query = request.GET.get('search')
    if query:

        print(query)
        SKY = sky.objects.filter(headline__contains=query,score__gt=0.0)
        CNN = cnn.objects.filter(headline__contains=query,score__gt=0.0)
        BBC = bbc.objects.filter(headline__contains=query,score__gt=0.0)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/POS.html',data)
    SKY = sky.objects.filter(score__gt=0.0)
    CNN = cnn.objects.filter(score__gt=0.0)
    BBC = bbc.objects.filter(score__gt=0.0)
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1

    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/POS.html',data)
def NEG(request):
    data = {}
    query = request.GET.get('search')
    if query:

        print(query)
        SKY = sky.objects.filter(headline__contains=query,score__lt=0.0)
        CNN = cnn.objects.filter(headline__contains=query,score__lt=0.0)
        BBC = bbc.objects.filter(headline__contains=query,score__lt=0.0)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/NEG.html',data)

    SKY = sky.objects.filter(score__lt=0.0)
    CNN = cnn.objects.filter(score__lt=0.0)
    BBC = bbc.objects.filter(score__lt=0.0)
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1

    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/NEG.html',data)
def NEU(request):
    data = {}
    query = request.GET.get('search')
    if query:

        print(query)
        SKY = sky.objects.filter(headline__contains=query,score=0.0)
        CNN = cnn.objects.filter(headline__contains=query,score=0.0)
        BBC = bbc.objects.filter(headline__contains=query,score=0.0)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/NEU.html',data)

    SKY = sky.objects.filter(score=0.0)
    CNN = cnn.objects.filter(score=0.0)
    BBC = bbc.objects.filter(score=0.0)
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1

    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/NEU.html',data)
def CNN(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        CNN = cnn.objects.filter(headline__contains=query)
        fresh = list(chain(CNN))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/CNN.html',data)
    data = {}
    CNN = cnn.objects.all()
    fresh = list(chain(CNN))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/CNN.html',data)
def SKY(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        SKY = sky.objects.filter(headline__contains=query)
        fresh = list(chain(SKY))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/SKY.html',data)
    data = {}
    SKY = sky.objects.all()
    fresh = list(chain(SKY))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    i=0
    if not newlist:
        print("khali")
        data["articles"] = newlist
        return render(request,'DeepNews/Empty.html',data)
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/SKY.html',data)
def BBC(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        BBC = bbc.objects.filter(headline__contains=query)
        fresh = list(chain(BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))


        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))
        data["articles"] = newlist
        return render(request,'DeepNews/BBC.html',data)
    data = {}
    BBC = bbc.objects.all()
    fresh = list(chain(BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/BBC.html',data)
def WORLD(request):
    query = request.GET.get('search')
    if query:
        data = {}
        print(query)
        SKY = sky.objects.filter(headline__contains=query)
        CNN = cnn.objects.filter(headline__contains=query)
        BBC = bbc.objects.filter(headline__contains=query)
        fresh = list(chain(SKY,CNN,BBC))
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        newlist=newlist[0:7]
        print(list(newlist))
        if not newlist:
            print("khali")
            data["articles"] = newlist
            return render(request,'DeepNews/Empty.html',data)
        i=0
        print("arha")
        for x in newlist:
            if x.score>0:
                x.score="Positive"

            elif x.score<0:
                x.score="Negative"
            else:
                x.score="Neutral"
            newlist[i]=x
            i=i+1
        i=0
        for x in newlist:
            i=i+1
            if i==7:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1
                print(x.id)
                print(list(x))

        data["articles"] = newlist

        return render(request,'DeepNews/WORLD.html',data)
    data = {}
    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    newlist=newlist[0:7]
    print(list(newlist))
    i=0
    print("arha")
    for x in newlist:
        if x.score>0:
            x.score="Positive"

        elif x.score<0:
            x.score="Negative"
        else:
            x.score="Neutral"
        newlist[i]=x
        i=i+1
    i=0
    for x in newlist:
        i=i+1
        if i==7:
            x.id=5
            x.link=4
            x.headline=3
            x.date=2
            x.image=1
            print(x.id)
            print(list(x))
    data["articles"] = newlist
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/WORLD.html',data)
def noth(request):
    return
def single_post(request, uuid):
    print("length")
    print(len(uuid))
    if(len(uuid)>15):
        mydata = {}
        result=""
        SKY = sky.objects.all()
        CNN = cnn.objects.all()
        BBC = bbc.objects.all()

        for i in SKY:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)
        for i in CNN:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)
        for i in BBC:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)

        print("result")
        print(result.headline)
        ARTICLE=article.objects.all()
        res=""
        for r in ARTICLE:
            res=r.id

        obj = article.objects.get(id=res)
        obj.headline = str(result.id)
        obj.save()
        if result:
            mydata["article"]=result

        #print(mydata)
        #return render(request,'DeepNews/single_post.html',mydata)
        return render(request, 'DeepNews/charts.html', {"customers": 1000})
    else:
        data = {}
        id=int(uuid)
        print(type(id));

        id2=id*6
        print(id)
        SKY = sky.objects.all()
        CNN = cnn.objects.all()
        BBC = bbc.objects.all()
        fresh = list(chain(SKY,CNN,BBC))
        print("fresh")
        print(fresh)
        newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
        print("sorted")
        print((newlist))
        list2=newlist[(id2-6):(id2+1)]
        print("6 only")
        print(list2)
        i=0
        for x in list2:
            i=i+1
            if i==7 and id>4:
                x.id=id+1
                x.link=id
                x.headline=id-1
                x.date=id-2
                x.image=id-1
                print(x.id)
            if i==7 and id<5:
                x.id=5
                x.link=4
                x.headline=3
                x.date=2
                x.image=1


        data["articles"] = list2
        #return render(request,'DeepNews/check.html',data)
        return render(request,'DeepNews/index.html',data)



def Pages(request, uid):
    data = {}
    id=int(uid)
    print(type(id));

    id=id*6
    print(id)
    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    list2=newlist[(id-6):id]
    data["articles"] = list2
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/index.html',data)
def records(request, Bid):
    uid=Bid
    data = {}
    id=int(uid)
    print(type(id));

    id=id*6
    print(id)
    SKY = sky.objects.all()
    CNN = cnn.objects.all()
    BBC = bbc.objects.all()
    fresh = list(chain(SKY,CNN,BBC))
    newlist = sorted(fresh, key=lambda x: x.date, reverse=True)
    list2=newlist[(id-6):id]
    data["articles"] = list2
    #return render(request,'DeepNews/check.html',data)
    return render(request,'DeepNews/index.html',data)
def contact(request):
    return render(request,'DeepNews/contact.html')
def about_us(request):
    return render(request,'DeepNews/about_us.html')
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        ARTICLE=article.objects.all()
        res=""
        for r in ARTICLE:
            res=r.headline
        uuid=res
        mydata = {}
        result=""
        SKY = sky.objects.all()
        CNN = cnn.objects.all()
        BBC = bbc.objects.all()

        for i in SKY:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)
        for i in CNN:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)
        for i in BBC:
            rs=i.id
            rt=str(rs)
            if uuid == rt:
                result=i
                print(rt)
            else:
                print(rt)

        print("result")
        print(result)

        #labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        """link=StringField()
        headline=StringField()
        content=ArrayField(ArrayField(StringField()))
        date=DateField()
        image=StringField()
        magnitude=FloatField()
        score=FloatField()"""
        val=[]
        labels = ["Range", "Polarity","Intensity"]

        values=[result.headline]
        if(result.score>0):
            values.append("Positive")
        elif(result.score<0):
            values.append("Negative")
        else:
            values.append("Neutral")
        print(values)
        count=0
        for x in result.content:
            count=count+1
            values.append(x)
            print(count)
        values.append(result.date)
        values.append(result.image)
        values.append(count)
        print(values)
        print(len(values))
        qs_count=100
        #default = [qs_count, 23, 2, 3, 12, 2]
        default = [qs_count, result.score*100,(result.magnitude*100)%100]
        print(default)
        data = {
                "labels": labels,
                "default": default,
                "values":values,
        }
        return Response(data)
