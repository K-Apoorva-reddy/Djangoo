from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse('hello world')
def sample1(request):
    return HttpResponse('welcome to django')

def sampleInfo(request):
    # data={"name":'apoorva','age':'21'}
    data={'result':[4,6,7,8]}
    return JsonResponse(data)
def dynamicResponse(request):
    name=request.GET.get("name",'appu')
    city=request.GET.get("city",'hyd')

    return HttpResponse(f"hello {name} from {city}")

    # return JsonResponse(data,safe=False)