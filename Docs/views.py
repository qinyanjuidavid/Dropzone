from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from Docs.models import Doc


def MainView(request):
    context={

    }
    return render(request,"Docs/main.html",context)
def file_upload_view(request):
    if request.method=="POST":
        my_file=request.FILES.get('file')
        Doc.objects.create(upload=my_file)
        return HttpResponse("")
    return JsonResponse({'post':'false'})
