from django.shortcuts import render
from Landlord.models import Member
from django.http import HttpResponse
from django.views import generic
from Landlord.forms import MemberForm
from django.contrib.auth.decorators import login_required






def index(request,name):
    return HttpResponse('Hello %s'%name)

def member(request,num_id):
    member = Member.objects.get(id=num_id)
    response = render(request,'landlord/landlord_detail.html',{
    'member': member})
    return response


def list1(request):
    member = Member.objects.get(id=1)
    member1 = Member.objects.get(id=2)
    member2 = Member.objects.get(id=3)
    member3 = Member.objects.get(id=4)
    member4 = Member.objects.get(id=5)
    
    response = render(request,'landlord/landlord_list.html',{
    'member': member,'member1':member1,'member2' : member2,'member3':member3,'member4':member4})
    return response
    


@login_required
def member_update(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            
            return HttpResponse('Thanks')
        else:
            return HttpResponse('Invalid data')
    form = MemberForm()
    return render(request,'landlord/member_update.html',{
        'form':form
        })   
    