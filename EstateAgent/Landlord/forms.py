from django import forms 
from Landlord.models import Member 
class MemberForm(forms.ModelForm): 
    class Meta: 
        model = Member 
        exclude=[] 
        
    