from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
# Create your views here.
def all_project(req):
    chais=ChaiVariety.objects.all()
    return render(req,'project/all_project.html',{'chais':chais})

def chai_details(req,chai_id):
    chai=get_object_or_404(ChaiVariety,pk=chai_id)
    return render(req,'project/chai_details.html',{'chai':chai})