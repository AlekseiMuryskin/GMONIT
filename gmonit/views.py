from django.shortcuts import render
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from .models import Worker, Report


# Create your views here.
def index(request):
    search = request.GET.get('search','')

    worker_list=Worker.objects.all()
    if search:
        worker_list =worker_list.filter(name__icontains=search)
    context = {
        'worker_list':worker_list
    }
    return render(request,'index.html',context)

def worker(request,work_id):
    auth=Worker.objects.get(id=work_id)
    print(auth)
    report_list=Report.objects.filter(author_icontains=auth)
    context = {
        'report_list':report_list
    }
    return render(request,'worker.html',context)