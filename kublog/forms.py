from django import forms
from kublog.models import Contact, PostOne

class PostOneForm(forms.ModelForm):
    class Meta:
        model = PostOne
        fields = ('title','content','place')
        widgets = {
            'content': forms.Textarea(attrs={'rows':10, 'cols':20}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_name','contact_message','contact_email')
        widgets = {
            'contact_message': forms.Textarea(attrs={'rows':10, 'cols':20}),
        }
    
class PostSearchForm(forms.Form):
    keywords = forms.CharField(max_length=50,)
        