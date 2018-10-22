from Landlord.models import Member
from django.http import HttpResponse
from django import admin 
def member(request,member_id):
    member = Member.objects.get(id=member_id)

    return HttpResponse('%s %s'%(member.first_name,member.last_name))